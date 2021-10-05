import unittest
from rlang.src.grounding import Domain
from rlang.src.exceptions import RLangGroundingError

class DomainTest(unittest.TestCase):
    def test_from_name(self):
        self.assertEqual(Domain.from_name("ACTION"), Domain.ACTION)
        self.assertEqual(Domain.from_name("REWARD"), Domain.REWARD)
        self.assertEqual(Domain.from_name("STATE_ACTION_NEXT_STATE"), Domain.STATE_ACTION_NEXT_STATE)
    
    def test_add(self):
        dom0 = Domain.STATE + Domain.ACTION
        self.assertEqual(dom0, Domain.STATE_ACTION)
        # dom1 = Domain.STATE + Domain.STATE_NEXT_STATE
        # self.assertEqual(dom1, Domain.STATE)
        # QUESTION: should _add_ be communtative?
        dom2 = Domain.STATE_NEXT_STATE + Domain.STATE
        self.assertEqual(dom2, Domain.STATE_NEXT_STATE)
        self.assertRaises(RLangGroundingError, lambda: Domain.FACTOR_STATE + Domain.STATE)

    def test_lt(self):
        self.assertFalse(Domain.STATE < Domain.ACTION)
        self.assertTrue(Domain.ACTION < Domain.STATE_ACTION_NEXT_STATE)
        self.assertTrue(Domain.STATE < Domain.STATE_NEXT_STATE)
        self.assertTrue(Domain.STATE_ACTION < Domain.STATE_ACTION_NEXT_STATE)

    def test_gt(self):
        self.assertTrue(Domain.STATE_NEXT_STATE > Domain.STATE)
        self.assertFalse(Domain.REAL_VALUE > Domain.STATE_ACTION)
        self.assertFalse(Domain.STATE_ACTION > Domain.FACTOR_STATE)
        self.assertTrue(Domain.STATE_ACTION_NEXT_STATE > Domain.ACTION)

if __name__ == '__main__':
    unittest.main()