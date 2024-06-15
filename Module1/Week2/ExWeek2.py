from typing import List, Dict
from collections import deque
from pathlib import Path

def sliding_window(input_list: List[int], k: int) -> List[int]:
    if len(input_list) <= 0 or k <= 0: 
        return []
    
    result = []
    window = deque() 

    for i in range(len(input_list)):
        if window and window[0] < i - k + 1: 
            window.popleft()
        while window and input_list[window[-1]] < input_list[i]: 
            window.pop()
        window.append(i) 

        if i >= k - 1: 
            result.append(input_list[window[0]])
    return result



def count_chars(string:str) -> Dict[str, int]:

    """
    Count the frequency of each character in a string

    Args:
        • string: the given string

    Returns:
        • a dictionary counting the number of letters occurring in a word
    """
    char_frequency = {}
    for char in string:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    return char_frequency


def count_words_in_text(file_name: str) -> Dict[str, int]:

    word_count = {}

    path = Path(file_name)

    with path.open('r') as file:
        for line in file:
            words = line.strip().lower().split()

            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    return word_count


def levenshtein_distance_algorithm(word1: str, word2: str) -> int:
    dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

    for col in range(len(dp)):
        dp[col][0] = col
    
    for row in range(len(dp[0])):
        dp[0][row] = row

    for row in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            if word1[col - 1] == word2[row - 1]:
                dp[row][col] = dp[row-1][col-1]
            else:
                dp[row][col] = min(
                    dp[row][col-1],
                    dp[row-1][col],
                    dp[row-1][col-1]
                ) + 1
    
    return dp[-1][-1]


