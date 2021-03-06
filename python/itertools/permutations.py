'''
Task
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Input Format
A single line containing the space separated string S and the integer value k.

Constraints
0 < k <= len(S)

The string contains only UPPERCASE characters.

Output Format
Print the permutations of the string  on separate lines.

Sample Input
HACK 2

Sample Output
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''

from itertools import permutations
S, k = input().split()
for permutation in permutations(sorted(S), int(k)):
    print(''.join(permutation))
