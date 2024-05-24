# Day 4
# Leetcode Problem 1255: Maximum Score Words Formed by Letters

# Problem Statement:
"""
Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

 

Example 1:

Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.
Example 2:

Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.
Example 3:

Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.
"""

# Approach
"""

Approach simple hai. Apan ek map bnayenge letters ka taaki jaise jaise words k letters match hote jaye, ham uss letter ka count decrese karde
and apan ek aur map bnayenge words k har ek subsets ka.
But before that, ham Yha bhi Masking technique use krenge. So if we have array ["dog","cat","dad","good"]
Then for subset [dad, good] mask will be 1100. ((https://leetcode.com/problems/maximum-score-words-formed-by-letters/Figures/1255/1255_words_example_updated.png))

To ham basically brute force type appraoch use kar rhe, ham har possible subsets k set bna k dekhenge kiska score max hai, total (2 ** len(words) - 1) times yani apan check krenge.

for for each mask, apan words array k jo jo subset bn rhe uska subset bnayenge aur score calculate krenge.
letters ka subset isliliye bna rhe qki isse ye check krna easy padega ki jitni freq kisi letter ki word me hai utni letters array me hai ya ni
aur score bhi easily calculate hoga.
For example, good word me o ki freq 2 hai to if we check ki letters me o ki freq 2 se jyada ho, if hai then score will we score[ord('o)] * freq_of_letter[ord('o')]

"""


# Solution:
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        counts = [0 for i in range(26)]
        for i in range(len(letters)):
            counts[ord(letters[i]) - ord('a')] += 1

        def subsetScore(subset, score, counts):
            total = 0

            for i in range(26):
                total += subset[i] * score[i]
                if subset[i] > counts[i]:
                    return 0
            return total

        
        maxScore = 0
        for mask in range(1 << len(words)): # yha ham har ek possibiliy dekhne k liye loop kar rhe
        # yani agar [dog, god, cat, good] hai to isme sirf [dog, god] ka score kya hoga,, then [good] ya [good, dog] ka.
        # and for this we are using mask. yani 0 & 1 me represent krna. So we can represent subset [dog, cat] as : 0101 and [cat, good] as 1100
        # refer this image to understand better: (https://leetcode.com/problems/maximum-score-words-formed-by-letters/Figures/1255/1255_words_example_updated.png)

            chars_map = [0 for i in range(26)]

            for i in range(len(words)):
                # check ki ye word already ek baar apan calculate na kar chuke ho, using masking and & operarot
                if (mask & (1 << i)) > 0:

                    for j in range(len(words[i])):
                        chars_map[ord(words[i][j]) - ord('a')] += 1

            maxScore = max(maxScore, subsetScore(chars_map, score, counts))

            # print(counts, maxScore, subsetScore(chars_map, score, counts))

        return maxScore


# Driver's Code
Output = Solution()

# Testcase 1
Testcase1 = Output.maxScoreWords(["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])
print(Testcase1) # Expected Output: 23


Testcase2 = Output.maxScoreWords(["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10])
print(Testcase2) # Expected Output: 27