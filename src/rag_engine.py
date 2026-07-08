class RAGEngine:

    def calculate(self, metrics):

        score = 0

        # -----------------------
        # Completion (20)
        # -----------------------

        completion = metrics["average_completion"]

        if completion >= 80:
            score += 20
        elif completion >= 60:
            score += 15
        elif completion >= 40:
            score += 10
        else:
            score += 5

        # -----------------------
        # Schedule (25)
        # -----------------------

        total = (
            metrics["green_schedule"] +
            metrics["amber_schedule"] +
            metrics["red_schedule"]
        )

        if total > 0:

            green_ratio = metrics["green_schedule"] / total

            if green_ratio >= 0.9:
                score += 25

            elif green_ratio >= 0.75:
                score += 20

            elif green_ratio >= 0.5:
                score += 12

            else:
                score += 5

        # -----------------------
        # Critical Tasks (15)
        # -----------------------

        critical = metrics["critical_tasks"]

        if critical <= 5:
            score += 15

        elif critical <= 20:
            score += 10

        else:
            score += 5

        # -----------------------
        # Risk Tasks (10)
        # -----------------------

        risk = metrics["risk_tasks"]

        if risk == 0:
            score += 10

        elif risk <= 5:
            score += 7

        else:
            score += 3

        # -----------------------
        # Variance (10)
        # -----------------------

        variance = metrics["average_variance"]

        if variance >= 0:
            score += 10

        elif variance >= -5:
            score += 8

        elif variance >= -10:
            score += 5

        else:
            score += 2

        # -----------------------
        # Negative Comments (10)
        # -----------------------

        comments = metrics["negative_comments"]

        if comments == 0:
            score += 10

        elif comments <= 2:
            score += 7

        else:
            score += 3

        # -----------------------
        # On Hold Tasks (10)
        # -----------------------

        hold = metrics["on_hold_tasks"]

        if hold == 0:
            score += 10

        elif hold <= 2:
            score += 7

        else:
            score += 3

        return round(score)

    def determine_rag(self, score):

        if score >= 80:
            return "Green"

        elif score >= 60:
            return "Amber"

        return "Red"
