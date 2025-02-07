from practice import hamming_distance, is_permutation, most_vowels
import unittest


class TestHamming(unittest.TestCase):
    def test_1(self):
        """Test 1: Half of elements are different"""
        h1 = [2, 3, 4, 5, 4, 3, 2, 1]
        h2 = [2, 5, 5, 5, 4, 3, -10, 0]
        expected = 4
        actual = hamming_distance(h1, h2)
        self.assertEqual(actual, expected)

    def test_2(self):
        """Test 2: No differences for lists of length 5"""
        h1 = [0, 0, 0, 0, 0]
        h2 = [0, 0, 0, 0, 0]
        expected = 0
        actual = hamming_distance(h1, h2)
        self.assertEqual(actual, expected)

    def test_3(self):
        """Test 3: All elements differ"""
        h1 = [1, 2, 3]
        h2 = [4, 5, 6]
        expected = 3
        actual = hamming_distance(h1, h2)
        self.assertEqual(actual, expected)

    def test_4(self):
        """Test 4: Lists with negative numbers"""
        h1 = [-1, -2, -3]
        h2 = [-1, -2, -4]
        expected = 1
        actual = hamming_distance(h1, h2)
        self.assertEqual(actual, expected)

    def test_5(self):
        """Test 5: Longer lists with one difference"""
        h1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        h2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        expected = 1
        actual = hamming_distance(h1, h2)
        self.assertEqual(actual, expected)

    def test_6(self):
        """Test 6: Longer lists with no differences"""
        h1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        h2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        expected = 0
        actual = hamming_distance(h1, h2)
        self.assertEqual(actual, expected)

    def test_7(self):
        """Test 7: Alternating differences"""
        h1 = [1, 1, 1, 0, 1, 0]
        h2 = [0, 1, 0, 1, 0, 1]
        expected = 5
        actual = hamming_distance(h1, h2)
        self.assertEqual(actual, expected)

    def test_8(self):
        """Test 8: Lists with zeros and ones"""
        h1 = [1, 1, 1, 1]
        h2 = [0, 0, 0, 0]
        expected = 4
        actual = hamming_distance(h1, h2)
        self.assertEqual(actual, expected)

    def test_9(self):
        """Test 9: Identical lists with mixed positive and negative numbers"""
        h1 = [-100, 200, -300, 400]
        h2 = [-100, 200, -300, 400]
        expected = 0
        actual = hamming_distance(h1, h2)
        self.assertEqual(actual, expected)

    def test_10(self):
        """Test 10: One Difference"""
        h1 = [1, 2, 14, 2, 4, 1, 8, 9, 100]
        h2 = [1, 2, 14, 2, 4, 4, 8, 9, 100]
        expected = 1
        actual = hamming_distance(h1, h2)
        self.assertEqual(actual, expected)

    def test_11(self):
        """Test 11: Lists with large integer values"""
        h1 = [2147483647, 2147483647]
        h2 = [2147483647, 2147483646]
        expected = 1
        actual = hamming_distance(h1, h2)
        self.assertEqual(actual, expected)

    def test_12(self):
        """Test 12: Lists with small integer values"""
        h1 = [-2147483648, -2147483648]
        h2 = [-2147483647, -2147483648]
        expected = 1
        actual = hamming_distance(h1, h2)
        self.assertEqual(actual, expected)

    def test_13(self):
        """Test 13: Lists with mix of large and small integer values"""
        h1 = [2147483647, -2147483648]
        h2 = [-2147483648, 2147483647]
        expected = 2
        actual = hamming_distance(h1, h2)
        self.assertEqual(actual, expected)


class TestPermutation(unittest.TestCase):
    def test_1(self):
        """Test 1: Simple permutation"""
        a = [1, 2, 3]
        b = [3, 1, 2]
        expected_bool = True
        actual_bool = is_permutation(a, b)
        self.assertEqual(actual_bool, expected_bool)

    def test_2(self):
        """Test 2: Same lists, same order"""
        a = [1, 2, 3, 3, 2]
        b = [1, 2, 3, 3, 2]
        expected_bool = True
        actual_bool = is_permutation(a, b)
        self.assertEqual(actual_bool, expected_bool)

    def test_3(self):
        """Test 3: Same elements, different frequencies"""
        a = [1, 2, 2]
        b = [2, 1, 1]
        expected_bool = False
        actual_bool = is_permutation(a, b)
        self.assertEqual(actual_bool, expected_bool)

    def test_4(self):
        """Test 4: Different lengths"""
        a = [1, 2, 3]
        b = [1, 2, 3, 4]
        expected_bool = False
        actual_bool = is_permutation(a, b)
        self.assertEqual(actual_bool, expected_bool)

    def test_5(self):
        """Test 5: Both lists empty"""
        a = []
        b = []
        expected_bool = True
        actual_bool = is_permutation(a, b)
        self.assertEqual(actual_bool, expected_bool)

    def test_6(self):
        """Test 6: Single element, same"""
        a = [1]
        b = [1]
        expected_bool = True
        actual_bool = is_permutation(a, b)
        self.assertEqual(actual_bool, expected_bool)

    def test_7(self):
        """Test 7: Single element, different"""
        a = [1]
        b = [2]
        expected_bool = False
        actual_bool = is_permutation(a, b)
        self.assertEqual(actual_bool, expected_bool)

    def test_8(self):
        """Test 8: Lists with negative numbers"""
        a = [-1, -2, -3]
        b = [-3, -2, -1]
        expected_bool = True
        actual_bool = is_permutation(a, b)
        self.assertEqual(actual_bool, expected_bool)

    def test_9(self):
        """Test 9: Lists with mixed positive and negative numbers"""
        a = [-1, 2, -3]
        b = [2, -1, -3]
        expected_bool = True
        actual_bool = is_permutation(a, b)
        self.assertEqual(actual_bool, expected_bool)

    def test_10(self):
        """Test 10: Lists with zeros"""
        a = [0, 1, 2]
        b = [2, 1]
        expected_bool = False
        actual_bool = is_permutation(a, b)
        self.assertEqual(actual_bool, expected_bool)

    def test_11(self):
        """Test 11: Lists with repeated elements"""
        a = [1, 1, 1, 2, 2, 3]
        b = [2, 1, 3, 1, 2, 1]
        expected_bool = True
        actual_bool = is_permutation(a, b)
        self.assertEqual(actual_bool, expected_bool)

    def test_12(self):
        """Test 12: Lists with duplicate zero values"""
        a = [0, 0, -1, 2, 3, 1]
        b = [3, 2, 1, 0, 0, -1]
        expected_bool = True
        actual_bool = is_permutation(a, b)
        self.assertEqual(actual_bool, expected_bool)

    def test_13(self):
        """Test 13: One list is a permutation, other is not"""
        a = [1, 2, 3, 4]
        b = [1, 2, 3, 3, 4]
        expected_bool = False
        actual_bool = is_permutation(a, b)
        self.assertEqual(actual_bool, expected_bool)


class TestVowels(unittest.TestCase):
    def test_1(self):
        """Test 1: Most Vowels"""
        list_of_strings = [
            None,
            "AaE",
            None,
            None,
            "CS313E",
            None,
            None,
            "iiiiii",
            None,
            "!@#$$%%%",
            None,
            "aeiou",
            None,
        ]
        expected_result = 7
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)

    def test_2(self):
        """Test 2: String with 1 vowel"""
        list_of_strings = ["A1", "2948294", "!L!:JK!:LKJ!"]
        expected_result = 0
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)

    def test_3(self):
        """Test 3: Multiple strings, one with most vowels"""
        list_of_strings = ["NaNI", "LOT", "YuGt", "@LLCAPS"]
        expected_result = 0
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)

    def test_4(self):
        """Test 4: All strings have no vowels"""
        list_of_strings = ["gym", "HHHHHHHHHHHHHHHHHH", "Y;LWWWWWWWWWW"]
        expected_result = 0
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)

    def test_5(self):
        """Test 5: Empty strings"""
        list_of_strings = ["", "", ""]
        expected_result = 0
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)

    def test_6(self):
        """Test 6: One empty string, others with vowels"""
        list_of_strings = ["", "abc", "def"]
        expected_result = 1
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)

    def test_7(self):
        """Test 7: Multiple strings with the same number of vowels"""
        list_of_strings = ["g0rn", "l3s3", "tie", "pie", "lie"]
        expected_result = 2
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)

    def test_8(self):
        """Test 8: Case sensitivity in vowels"""
        list_of_strings = ["Apple", "ORANGE", "banana"]
        expected_result = 1
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)

    def test_9(self):
        """Test 9: Mixed case and one vowel"""
        list_of_strings = ["XYZ", "abc", "NOP", "IT'S NOT ME", "hahaha"]
        expected_result = 3
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)

    def test_10(self):
        """Test 10: Single character strings"""
        list_of_strings = ["a", "b", "c"]
        expected_result = 0
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)

    def test_11(self):
        """Test 11: Strings with special characters"""
        list_of_strings = ["@pple", "#banana", "!orange"]
        expected_result = 1
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)

    def test_12(self):
        """Test 12: Strings with numbers"""
        list_of_strings = ["h3llo", "w0rldli", "t3st1ng", "g4rb4ge"]
        expected_result = 0
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)

    def test_13(self):
        """Test 13: Strings with special characters and numbers"""
        list_of_strings = ["@pple123", "b@n@n@", None, "0r@ngeses"]
        expected_result = 3
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)

    def test_14(self):
        """Test 14: Mixture of empty strings, None, and normal strings"""
        list_of_strings = ["", None, "apple", "banana", "    "]
        expected_result = 3
        actual_result = most_vowels(list_of_strings)
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
