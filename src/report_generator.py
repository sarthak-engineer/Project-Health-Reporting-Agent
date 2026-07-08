from pathlib import Path


class ReportGenerator:

    def __init__(self):

        self.output_folder = Path("output/weekly_reports")

        self.output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

    def generate(self, project):

        filename = (
            project["project"]
            .replace(" ", "_")
            .replace("/", "_")
        )

        report_file = (
            self.output_folder /
            f"{filename}.md"
        )

        metrics = project["metrics"]

        with open(report_file, "w", encoding="utf-8") as file:

            file.write("# Weekly Project Health Report\n\n")

            file.write(f"**Project:** {project['project']}\n\n")
            file.write(f"**Health Score:** {project['score']}/100\n\n")
            file.write(f"**RAG Status:** {project['rag']}\n\n")

            file.write("---\n\n")

            file.write("## Executive Summary\n\n")
            file.write(project["analysis"]["executive_summary"])
            file.write("\n\n")

            file.write("---\n\n")

            file.write("## Project Metrics\n\n")

            file.write("| Metric | Value |\n")
            file.write("|--------|------:|\n")

            for key, value in metrics.items():
                file.write(
                    f"| {key.replace('_',' ').title()} | {value} |\n"
                )

            file.write("\n---\n\n")

            file.write("## Key Risks\n\n")

            for risk in project["analysis"]["key_risks"]:
                file.write(f"- {risk}\n")

            file.write("\n---\n\n")

            file.write("## Recommendations\n\n")

            for rec in project["analysis"]["recommendations"]:
                file.write(f"- {rec}\n")

            file.write("\n---\n\n")

            file.write("## Next Week Focus\n\n")

            file.write(
                "- Review all Red and Critical tasks.\n"
            )

            file.write(
                "- Monitor schedule variance.\n"
            )

            file.write(
                "- Update stakeholder communication.\n"
            )

            file.write(
                "- Track completion of pending activities.\n"
            )

        return report_file
