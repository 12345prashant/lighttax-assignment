def tax_lookup(income):
    if income <= 11000:
        return income * 0.10
    elif income <= 44725:
        return income * 0.12
    else:
        return income * 0.22