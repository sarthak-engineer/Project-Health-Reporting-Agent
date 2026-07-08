import pandas as pd


class SignalExtractor:

    def extract(self, row):

        return {

            "schedule_health": row.get("Schedule Health"),

            "completion": row.get("% Complete"),

            "status": row.get("Status"),

            "critical": row.get("Critical ?"),

            "risk": row.get("At Risk?"),

            "variance": row.get("Variance"),

            "comments": row.get("Comments"),

            "status_comment": row.get("Status Comment"),

            "task_name": row.get("Task Name"),

            "owner": row.get("Assigned To")

        }