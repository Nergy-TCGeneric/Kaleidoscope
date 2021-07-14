import unittest
import codepacker

class CodePackerTest(unittest.TestCase):
    def setUp(self):
       self.meta = codepacker.get_meta("STUB", "x = 5\n" + \
        	                                   "if x == 5:\n" + \
        	                                   "    x = 4")

    def tearDown(self):
        pass

    def testCreateMeta(self):
        self.assertTrue("x" in self.meta.var, "#1. Variable name existence")
        t = self.meta.var["x"]
        self.assertEqual(t[0], type(1), "#2. Type Equivalence")
        self.assertEqual(t[1], 5, "#3. Actual value/type Equivalence")
        
if __name__ == "__main__":
    unittest.main()