"""Illustrative underwriting sensitivities. Rates are fractions, not percentages."""
def dscr(cfads, service, haircut=0):
    if cfads < 0 or service <= 0 or not 0 <= haircut <= 1:
        raise ValueError('Invalid cash flow, service or haircut')
    return cfads*(1-haircut)/service

def expected_loss(exposure, pd, lgd):
    if exposure < 0 or not 0 <= pd <= 1 or not 0 <= lgd <= 1:
        raise ValueError('Invalid credit assumptions')
    return exposure*pd*lgd

def usd_growth(real_growth, domestic_deflator, fx_depreciation):
    """FX depreciation is the annual rise in local currency per USD."""
    if min(real_growth, domestic_deflator, fx_depreciation) <= -1:
        raise ValueError('Growth factors must be positive')
    return (1+real_growth)*(1+domestic_deflator)/(1+fx_depreciation)-1

def recovery_per_close(initial_count, initial_cost, advanced_count, advanced_cost, closes):
    if min(initial_count,initial_cost,advanced_count,advanced_cost)<0 or closes<=0:
        raise ValueError('Invalid preparation cohort')
    if closes>advanced_count or advanced_count>initial_count:
        raise ValueError('Inconsistent preparation funnel')
    return (initial_count*initial_cost+advanced_count*advanced_cost)/closes
