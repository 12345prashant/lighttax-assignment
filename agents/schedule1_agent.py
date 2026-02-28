from agents.base_agent import BaseAgent
from tools.pdf_navigator import PDFNavigator
from models.schemas import Schedule1Output


class Schedule1Agent:

    def __init__(self):
        self.pdf = PDFNavigator("data/i1040s1--2024.pdf")

        self.agent = BaseAgent("""
You are Schedule 1 tax expert.

IRS Instructions:
{context}

Explain why business profit is included in additional income.

Return JSON:
{{
"citation": "IRS reference"
}}
""")

    def run(self, sc_output):

        context = self.pdf.search("additional income")

        # deterministic logic
        additional_income = sc_output.net_profit
        adjustments = 0

        result = self.agent.run(context, sc_output.model_dump())

        return Schedule1Output(
            additional_income=additional_income,
            adjustments=adjustments,
            citation=result.get("citation", "IRS Schedule 1 instructions")
        )