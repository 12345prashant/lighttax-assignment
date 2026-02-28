from pydantic import BaseModel

class TaxPayer(BaseModel):
    name: str
    filing_status: str

    w2_income: float

    business_income: Optional[float] = 0
    business_expenses: Optional[float] = 0

    unemployment_compensation: Optional[float] = 0
    student_loan_interest_paid: Optional[float] = 0

    has_self_employment: bool


class ScheduleCOutput(BaseModel):
    net_profit: float
    citation: str | None = None


class Schedule1Output(BaseModel):
    additional_income: float
    adjustments: float
    citation: str | None = None


class Form1040Output(BaseModel):
    total_income: float
    taxable_income: float
    tax: float