def standard_deduction_lookup(status: str):
    table = {
        "single": 14600,
        "married": 29200
    }
    return table.get(status.lower(), 14600)


def tax_table_lookup(taxable_income: float):
    # simplified fake table
    if taxable_income <= 10000:
        return taxable_income * 0.1
    elif taxable_income <= 50000:
        return taxable_income * 0.2
    else:
        return taxable_income * 0.3