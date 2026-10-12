"""Illustrative recoverable-preparation facility. USD millions, not a budget.
Only direct preparation costs of successful projects are recovered. No management
or success fees assumed. Recoveries are delayed; failed costs remain losses.
"""
import csv,sys

def facility(years=5,grant=1.0,overhead=.5,annual_studies=10,study_cost=.1,close_rate=.2,recovery_share=1.0,lag=2):
    if years<1 or min(grant,overhead,annual_studies,study_cost,lag)<0 or not 0<=close_rate<=1 or not 0<=recovery_share<=1:
        raise ValueError("Invalid assumptions")
    cash=0.;due={}
    for year in range(1,years+1):
        spend=annual_studies*study_cost
        due[year+lag]=due.get(year+lag,0)+spend*close_rate*recovery_share
        recovered=due.get(year,0);opening=cash;net=grant+recovered-overhead-spend;cash+=net
        yield {'year':year,'opening_cash':opening,'grant':grant,'recovery':recovered,'overhead':overhead,'preparation_spend':spend,'net_cash':net,'closing_cash':cash,'funding_shortfall':max(0,-cash)}
if __name__=='__main__':
    rows=list(facility());w=csv.DictWriter(sys.stdout,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
