import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'models'))
from underwriting import dscr,expected_loss,usd_growth,recovery_per_close
class Underwriting(unittest.TestCase):
 def test_stress_breaks_debt_coverage(self):
  self.assertGreater(dscr(20,15,.2),1)
  self.assertLess(dscr(20,15,.3),1)
 def test_credit_buffer_stress(self):
  self.assertEqual(expected_loss(100,.05,.4),2)
  self.assertEqual(expected_loss(100,.15,.6),9)
 def test_currency_can_offset_domestic_growth(self):
  self.assertAlmostEqual(usd_growth(.06,.04,.1024),0)
  with self.assertRaises(ValueError):usd_growth(.06,.04,-1)
 def test_one_close_must_bear_failed_studies(self):
  self.assertEqual(recovery_per_close(10,1,4,4,1),26)
  self.assertEqual(recovery_per_close(10,1,4,4,4),6.5)
  with self.assertRaises(ValueError):recovery_per_close(10,1,4,4,0)
if __name__=='__main__':unittest.main()
