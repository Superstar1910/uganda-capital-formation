"""September article scenario; inherited assumptions, not refreshed actuals.
Amounts USD billions. Annual straight-line interpolation includes 2026..2040.
"""
import csv,sys
POINTS=[(2025,62,.2265),(2030,120,.30),(2035,250,.35),(2040,500,.40)]
def article_scenario(points=POINTS, baseline=.24):
    if not 0<=baseline<=1 or len(points)<2:
        raise ValueError("Invalid assumptions")
    for (y0,g0,r0),(y1,g1,r1) in zip(points,points[1:]):
        if y1<=y0 or g0<=0 or g1<=0 or not 0<=r0<=1 or not 0<=r1<=1:
            raise ValueError("Invalid checkpoints")
        for y in range(y0+1,y1+1):
            w=(y-y0)/(y1-y0);g=g0+(g1-g0)*w;r=r0+(r1-r0)*w
            yield [y,g,g*baseline,g*r,g*(r-baseline),r]
if __name__=='__main__':
    w=csv.writer(sys.stdout);w.writerow(['year','gdp_usd_bn','comparison_investment_usd_bn','scenario_investment_usd_bn','difference_usd_bn','investment_rate']);w.writerows(article_scenario())
