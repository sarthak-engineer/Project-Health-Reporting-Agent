from src.project_analyzer import ProjectAnalyzer
from src.report_generator import ReportGenerator
from src.presentation_generator import PresentationGenerator

print("=" * 70)
print("AI PROJECT HEALTH REPORTING AGENT")
print("=" * 70)

analyzer = ProjectAnalyzer()
report_generator = ReportGenerator()
presentation_generator = PresentationGenerator()

results = analyzer.analyze_projects()

for project in results:

    print("\n" + "=" * 60)

    print(f"Project : {project['project']}")

    print("\nMetrics")

    for key, value in project["metrics"].items():

        print(f"{key:25}: {value}")

    print(f"\nScore : {project['score']}")
    print(f"RAG   : {project['rag']}")

    print("\nExecutive Summary")

    print(project["analysis"]["executive_summary"])

    print("\nTop Risks")

    for risk in project["analysis"]["key_risks"]:
        print(f"- {risk}")

    print("\nRecommendations")

    for rec in project["analysis"]["recommendations"]:
        print(f"- {rec}")

    report_path = report_generator.generate(project)

    print(f"\nWeekly report saved to: {report_path}")

presentation_path = presentation_generator.generate(results)

print("\n" + "=" * 70)
print(f"Executive presentation saved to: {presentation_path}")