"""Illustrative GDP and investment pathway. Standard library only."""
import argparse,csv,sys

def scenario(start=50, year=2023, target=500, baseline=.24, rate=.40):
    if start<=0 or target<=0 or not 2000<=year<2040 or not 0<=baseline<=1 or not 0<=rate<=1:
        raise ValueError("Invalid scenario assumptions")
    n=2040-year; g=(target/start)**(1/n)-1
    for k in range(1,n+1):
        v=start*(1+g)**k; q=baseline+(rate-baseline)*k/n
        yield [year+k,v,v*baseline,v*q,v*(q-baseline),q]

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--start',type=float,default=50);p.add_argument('--year',type=int,default=2023);p.add_argument('--target',type=float,default=500);p.add_argument('--baseline',type=float,default=.24);p.add_argument('--rate',type=float,default=.40)
    a=p.parse_args();w=csv.writer(sys.stdout);w.writerow(['year','gdp_usd_bn','comparison_investment_usd_bn','scenario_investment_usd_bn','difference_usd_bn','investment_rate']);w.writerows(scenario(**vars(a)))
