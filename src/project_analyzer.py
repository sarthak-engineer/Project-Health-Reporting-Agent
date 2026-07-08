from src.parser import ProjectParser
from src.metrics_generator import ProjectMetricsGenerator
from src.rag_engine import RAGEngine
from src.models import ProjectAnalysis
from src.context_builder import ContextBuilder
from src.ai_reasoning import AIReasoning


class ProjectAnalyzer:

    def __init__(self):

        self.parser = ProjectParser()

        self.metrics = ProjectMetricsGenerator()

        self.rag = RAGEngine()

        self.context_builder = ContextBuilder()

        self.ai = AIReasoning()

    def analyze_projects(self):

        projects = self.parser.load_projects()

        results = []

        for project in projects:

            df = project["data"]

            metrics = self.metrics.generate(df)

            score = self.rag.calculate(metrics)

            rag = self.rag.determine_rag(score)

            context = self.context_builder.build(
                project["sheet_name"],
                metrics,
                score,
                rag
            )

            analysis = self.ai.generate(context)

            results.append(
                ProjectAnalysis(
                    project_name=project["sheet_name"],
                    metrics=metrics,
                    score=score,
                    rag=rag,
                    context=context,
                    analysis=analysis
                )
            )

        return results