import unittest
from Module1.Week2.ExWeek2 import sliding_window, count_chars, count_words_in_text, levenshtein_distance_algorithm


class test_main(unittest.TestCase):
    

    def test_sliding_window(self):
        self.assertListEqual(
            sliding_window([3 , 4 , 5 , 1 , -44], 3), [5, 5, 5]
        )

    def test_count_chars(self):
        self.assertDictEqual(
            count_chars("Baby") , {'B': 1, 'a': 1, 'b': 1, 'y': 1}
        )
    
    def test_count_words(self):
        answer = count_words_in_text("./Module1/Week2/data/P1_data.txt")
        self.assertEqual(
            answer['who'], 3
        )

    def test_leverin_algo(self):
        self.assertEqual(
            levenshtein_distance_algorithm("hi", "hello"), 4
        )
    
if __name__ == "__main__":
    unittest.main()