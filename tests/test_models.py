import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'models'))
from scenario import scenario
from article_scenario import article_scenario
from facility_economics import facility
from mobilisation import reconcile
class Models(unittest.TestCase):
 def test_strategy_reaches_target(self):
  r=list(scenario());self.assertEqual(len(r),17);self.assertAlmostEqual(r[-1][1],500);self.assertAlmostEqual(r[-1][3],200)
 def test_article_endpoints_and_identity(self):
  r=list(article_scenario());self.assertEqual(len(r),15)
  for y,g,i in [(2030,120,36),(2035,250,87.5),(2040,500,200)]:
   v=next(x for x in r if x[0]==y);self.assertAlmostEqual(v[1],g);self.assertAlmostEqual(v[3],i)
  for v in r:self.assertAlmostEqual(v[3]-v[2],v[4])
 def test_comparison_can_be_negative(self):
  self.assertLess(sum(v[4] for v in scenario(rate=.1)),0)
 def test_delayed_recovery_does_not_erase_failures(self):
  r=list(facility());self.assertEqual(r[0]['recovery'],0);self.assertEqual(r[1]['recovery'],0);self.assertAlmostEqual(r[2]['recovery'],.2);self.assertLess(r[-1]['closing_cash'],0)
 def test_cash_roll_forward(self):
  r=list(facility());self.assertAlmostEqual(r[-1]['closing_cash'],sum(v['net_cash'] for v in r))
 def test_investor_participation_not_double_counted(self):
  r=reconcile({'sponsor':20,'dfi':20,'pension':60},70,30);self.assertEqual(r['total_financing'],100);self.assertEqual(r['new_productive_capex'],70)
 def test_unbalanced_sources_rejected(self):
  with self.assertRaises(ValueError):reconcile({'pension':60},70,30)
if __name__=='__main__':unittest.main()
