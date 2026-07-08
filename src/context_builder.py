class ContextBuilder:

    def build(self, project_name, metrics, score, rag):

        total_tasks = metrics["total_tasks"]
        completion_ratio = (metrics["completed_tasks"] / total_tasks * 100) if total_tasks > 0 else 0.0
        not_started_ratio = (metrics["not_started_tasks"] / total_tasks * 100) if total_tasks > 0 else 0.0

        context = f"""
Project Name: {project_name}

Overall Project Health

Score: {score}/100

RAG Status: {rag}

Project Metrics

Total Tasks: {total_tasks}

Completed Tasks: {metrics['completed_tasks']} ({completion_ratio:.1f}%)

In Progress Tasks: {metrics['in_progress_tasks']}

Not Started Tasks: {metrics['not_started_tasks']} ({not_started_ratio:.1f}%)

On Hold Tasks: {metrics['on_hold_tasks']}

Average Completion: {metrics['average_completion']}%

Schedule Health

Green Tasks: {metrics['green_schedule']}

Amber Tasks: {metrics['amber_schedule']}

Red Tasks: {metrics['red_schedule']}

Critical Tasks: {metrics['critical_tasks']}

Risk Tasks: {metrics['risk_tasks']}

Average Schedule Variance: {metrics['average_variance']} days

Negative Stakeholder Comments: {metrics['negative_comments']}
"""

        return context
