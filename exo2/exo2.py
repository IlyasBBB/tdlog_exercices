"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""
import unittest

def ends_with(main_str, sub_str):
    return main_str.endswith(sub_str)

class TestEndsWith(unittest.TestCase):
    
    def test_fixed_tests_True(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        )
        
        for main_str, sub_str in fixed_tests_True:
            with self.subTest(main_str=main_str, sub_str=sub_str):
                self.assertTrue(ends_with(main_str, sub_str))

    def test_fixed_tests_False(self):
        fixed_tests_False = (
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        )
        
        for main_str, sub_str in fixed_tests_False:
            with self.subTest(main_str=main_str, sub_str=sub_str):
                self.assertFalse(ends_with(main_str, sub_str))

if __name__ == '__main__':
    unittest.main()

