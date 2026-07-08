import pandas as pd
import re


class ProjectMetricsGenerator:

    def generate(self, df):

        metrics = {}

        # ----------------------------
        # Task Counts
        # ----------------------------
        metrics["total_tasks"] = len(df)

        status = df["Status"].fillna("").astype(str).str.lower()

        metrics["completed_tasks"] = status.eq("completed").sum()
        metrics["in_progress_tasks"] = status.eq("in progress").sum()
        metrics["not_started_tasks"] = status.eq("not started").sum()
        metrics["on_hold_tasks"] = status.eq("on hold").sum()

        # ----------------------------
        # Completion %
        # ----------------------------
        if "% Complete" in df.columns:
            metrics["average_completion"] = round(
                df["% Complete"].fillna(0).mean(), 2
            )
        else:
            metrics["average_completion"] = 0

        # ----------------------------
        # Schedule Health
        # ----------------------------
        schedule = (
            df["Schedule Health"]
            .fillna("")
            .astype(str)
            .str.lower()
        )

        metrics["green_schedule"] = schedule.eq("green").sum()
        metrics["amber_schedule"] = schedule.eq("yellow").sum()
        metrics["red_schedule"] = schedule.eq("red").sum()

        # ----------------------------
        # Critical Tasks
        # ----------------------------
        if "Critical ?" in df.columns:

            critical = pd.to_numeric(
                df["Critical ?"],
                errors="coerce"
            )

            metrics["critical_tasks"] = (
                critical.fillna(0) == 1
            ).sum()

        else:

            metrics["critical_tasks"] = 0

        # ----------------------------
        # Risk Tasks
        # ----------------------------
        if "At Risk?" in df.columns:

            risk = pd.to_numeric(
                df["At Risk?"],
                errors="coerce"
            )

            metrics["risk_tasks"] = (
                risk.fillna(0) == 1
            ).sum()

        else:

            metrics["risk_tasks"] = 0

        # ----------------------------
        # Average Variance
        # ----------------------------
        variance_days = []

        if "Variance" in df.columns:

            for value in df["Variance"].dropna():

                match = re.search(r"-?\d+", str(value))

                if match:

                    variance_days.append(
                        int(match.group())
                    )

        if variance_days:

            metrics["average_variance"] = round(
                sum(variance_days) / len(variance_days),
                2
            )

        else:

            metrics["average_variance"] = 0

        # ----------------------------
        # Negative Comments
        # ----------------------------
        negative_words = [
            "delay",
            "issue",
            "blocked",
            "pending",
            "risk",
            "hold",
            "late",
            "waiting",
            "sign off",
            "signoff"
        ]

        negative = 0

        if "Comments" in df.columns:

            for comment in df["Comments"].fillna(""):

                text = str(comment).lower()

                if any(word in text for word in negative_words):
                    negative += 1

        metrics["negative_comments"] = negative

        return metrics
