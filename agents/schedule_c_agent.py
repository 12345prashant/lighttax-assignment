from agents.base_agent import BaseAgent
from tools.pdf_navigator import PDFNavigator
from models.schemas import ScheduleCOutput


class ScheduleCAgent:

    def __init__(self):
        self.pdf = PDFNavigator("data/i1040sc--2024.pdf")

        
        self.agent = BaseAgent("""
You are IRS Schedule C expert.

IRS Instructions:
{context}

Explain briefly how net profit is computed from income and expenses.
Return JSON:

{{
"citation": "IRS reference used"
}}
""")

    def run(self, taxpayer):

        context = self.pdf.search("net profit")

        #  deterministic calculation 
        income = taxpayer.business_income or 0
        expenses = taxpayer.business_expenses or 0
        net_profit = income - expenses

        print("DEBUG income:", income)
        print("DEBUG expenses:", expenses)
        print("DEBUG net_profit:", net_profit)

        
        result = self.agent.run(context, taxpayer.model_dump())

        return ScheduleCOutput(
            net_profit=net_profit,
            citation=result.get("citation", "IRS Schedule C instructions")
        )