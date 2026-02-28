from models.schemas import Form1040Output
from tools.deduction_tool import standard_deduction
from tools.tax_table import tax_lookup


class Form1040Agent:

    def run(self, taxpayer, s1_output):

        total_income = taxpayer.w2_income + s1_output.additional_income

        deduction = standard_deduction(taxpayer.filing_status)

        taxable_income = max(0, total_income - deduction)

        tax = tax_lookup(taxable_income)

        return Form1040Output(
            total_income=total_income,
            taxable_income=taxable_income,
            tax=tax
        )