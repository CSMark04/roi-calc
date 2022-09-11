import unittest
from main import User_info

class TestCal(unittest.TestCase):

    def test_name(self):
        test_name = User_info(' ','mark',' ',' ',' ')
        self.assertIn('mark',test_name.name )

    def test_curr(self):
        test_curr = User_info('mark',' ',' ',' ',' ')
        self.assertIn('mark',test_curr.curr_user )

    def test_property(self):
        test_property = User_info(' ','',' house',' ',' ')
        self.assertIn('house',test_property.property )

    def test_investment(self):
        test_investment = User_info(' ',' ',' ',' ', '100000')
        self.assertIn('100000',test_investment.investment )

    

if __name__ == '__main__':
    unittest.main()