from dataclasses import dataclass
from typing import Dict


@dataclass
class ProjectAnalysis:

    project_name: str

    metrics: Dict

    score: int

    rag: str

    context: str

    analysis: Dict

    def __getitem__(self, key):
        if key == "project":
            return self.project_name
        return getattr(self, key)
