word1 = 'abc'
word2 = 'xyzmmmm'
max_len = max(len(word1), len(word2))
result = []

for i in range(max_len):
    if i < len(word1):
        result.append(word1[i])
    if i < len(word2):
        result.append(word2[i])
    
r = "".join(result)
print(r)


# word1 = "bat"
# word2 = "ball"

# len_word1 = len(word1)
# len_word2 = len(word2)

# if len_word1 == 0 and len_word2 == 0:
#     print("Both the words are empty")
# elif len_word1 > 0 and len_word2 < 0:
#     print(word1)
# elif len_word1 < 0 and len_word2 > 0:
#     print(word2)

# min_len = min(len_word1, len_word2)

# result = ''
# for i in range(min_len):
#     result += word1[i] + word2[i]

# if min_len != len_word1:
#     for i in range(min_len, len_word1):
#         result += word1[i]
# else:
#     for i in range(min_len, len_word2):
#         result += word2[i]      

# print(result)

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.