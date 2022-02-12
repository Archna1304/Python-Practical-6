# Archana Vyas
# 20CE157
# AIM: You are given n words. Some words may repeat.
# For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word.
# See the sample input/output for clarification.
# Git Repository

# import counter from collections
from collections import Counter
# integer input
n_archana = int(input())
# make an empty list
l = list()
for _ in range(n_archana):
    # append input into list
    l.append(input())
# starting counter list of l
x = Counter(l)
# print(x)
# to print number of unique strings/distinct words
print(len(x))
# to print the values or number of occurrence on same line
for i in x.values():
    print(i, end=" ")
# or we can also use unpack operator
# print(*x.values())
