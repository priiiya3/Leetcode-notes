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

# Testcase 2
Testcase2 = Output.maxScoreWords(["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10])
print(Testcase2) # Expected Output: 27

# Testcase 3
Testcase3 = Output.maxScoreWords(["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0])
print(Testcase3) # Expected Output: 0




# Approacg 2 (Yet to check)
"""
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        W = len(words)
        # Count how many times each letter occurs
        self.max_score = 0
        freq = [0 for i in range(26)]
        subset_letters = [0 for i in range(26)]
        for c in letters:
            freq[ord(c) - 97] += 1

        # Check if adding this word exceeds the frequency of any letter
        def is_valid_word(subset_letters):
            for c in range(26):
                if freq[c] < subset_letters[c]:
                    return False
            else:
                return True
        
        def check(w, words, score, subset_letters, total_score):
            if w == -1:
                # If all words have been iterated, check the score of this subset
                self.max_score = max(self.max_score, total_score)
                return
            # Not adding words[w] to the current subset
            check(w - 1, words, score, subset_letters, total_score)
            # Adding words[w] to the current subset
            L = len(words[w])
            for i in range(L):
                c = ord(words[w][i]) - 97
                subset_letters[c] += 1
                total_score += score[c]

            if is_valid_word(subset_letters):
                # Consider the next word if this subset is still valid
                check(w - 1, words, score, subset_letters, total_score)
                
            # Rollback effects of this word
            for i in range(L):
                c = ord(words[w][i]) - 97
                subset_letters[c] -= 1
                total_score -= score[c]

        check(W - 1, words, score, subset_letters, 0)
        # Return max_score as the result
        return self.max_score

# ALGORITHM:
Approach 2: Backtracking
Intuition
Suppose the set of usable letters in a given input does not contain the letter "d", and the set of words is ["abcd", "acc", "abb", "bc"]. Note that any subset containing the word "abcd" is always invalid, because the word contains letter "d". The iterative approach will continue to check every subset that contains "abcd", which results in a considerable amount of unnecessary computation. What if we had a way to prune all subsets containing the word "abcd"? This is where a recursive solution comes into play.

Rather than iteratively checking every subset of words, we can use a recursive function to choose whether we include or exclude the current word in a candidate subset. If we pass the subsetLetters array as a parameter throughout every recursive call, after the addition of a word to a subset, we can check if there is a letter c where subsetLetters[c] exceeds freq[c] (see the isValidWord method). Once a recursive call terminates, we can roll back any changes made by the current recursive call to extensively search for all possibilities.

This approach is called backtracking, which is a search strategy that visits states and rolls back changes to return to a previous state. Doing so allows you to explore all branches from one state. For more details, see our backtracking explore card.

The base case is when all words have been considered for the subset, which is handled by comparing maxScore with totalScore and updating maxScore if totalScore is larger. The recursive case considers two choices: adding the ithi^{\texttt{th}}i 
th
  word or not adding the ithi^{\texttt{th}}i 
th
  word. This generates the subsets that will eventually either reach the base case or get pruned because that subset is not valid.

One notable merit of this backtracking solution lies in the pruning of bad subsets. If there is a set of subsets that share the same words that break the limits imposed by the given letters, the recursive algorithm can choose not to continue the search down this branch. For example, if the first word cannot be constructed, this recursive algorithm would immediately cut out any subset containing the first word, whereas an iterative solution would still check every subset that contains the first word.

Algorithm
Generate a frequency array where freq[c] is the number of times letter c appears in letters.
Initialize maxScore to store the largest score among valid subsets.
Call a recursive subroutine check that passes w (the index of the current word), words, score, subsetLetters, and totalScore (the sum of word scores in the subset) as parameters. Steps 4-10 describe the check method.
If w equals −1-1−1, all words have been considered, and we should update maxScore to totalScore if maxScore is less than totalScore.
Otherwise, we need to consider two possible recursive calls: one that adds words[w] to the subset, and one that doesn't.
To account for not adding a word, call check(w - 1, words, score, subsetLetters, totalScore).
To add words[w] to the subset, update subsetLetters and totalScore to include the word.
If the addition of words[w] does not violate letter limits imposed by freq, make the recursive call check(w - 1, words, score, subsetLetters, totalScore). To check for validity, we define the isValidWord method as follows:
For each character in the alphabet, check if freq[c] < subsetLetters[c]. If there exists such c, return false.
Return true if the subset can be built out of the given letters.
Roll back the changes to subsetLetters and totalScore immediately after making this recursive call.
Call check(W - 1, words, score, subsetLetters, 0), where subsetLetters is initially all zeros.
Return maxScore as the result.
Implementation

"""