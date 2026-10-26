def simple_interest(principal, annual_rate, years):
    if principal < 0 or annual_rate < 0 or years < 0:
        raise ValueError("Inputs must be non-negative")
    return principal * annual_rate * years
