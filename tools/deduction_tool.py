def standard_deduction(status: str):
    table = {
        "single": 14600,
        "married": 29200
    }
    return table.get(status.lower(), 14600)