# find anagram pairs in word_set and put the answer in result as tuple pairs

word_set = {'plea', 'ape', 'leap', 'pea', 'pale', 'medical', 'listen'
            , 'silent', 'decimal'}

result = set()

print('Printing word pairs:')

for word1 in word_set:
    for word2 in word_set:
        if word1 != word2 and sorted(word1) == sorted(word2):
            pair = tuple(sorted((word1, word2)))
            result.add(pair)

for pair in result:
    print(pair)

# 2. Plagiarism check between two strings 
import re 

str1 = "The quick brown fox"
str2 = "The quick brown fox jumps over the lazy dog"

w1 = re.findall(r'\w+', str1.lower())
w2 = re.findall(r'\w+', str2.lower())

s1 = set(w1)
s2 = set(w2)

common = s1 & s2
print(common)
unique = s1 | s2
print(unique)

ratio = len(common) / len(unique)

print(f"Jaccardian Similarity ratio is: {ratio : .2f}")
