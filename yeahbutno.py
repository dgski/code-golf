'''
Input: 0
Output:


Input: 1
Output:
Yeah
But

Input: 2
Output:
Yeah
But
No

Input: 10
Output:
Yeah
But
No
But
Yeah
But
No
Yeah
But
No
But
Yeah
'''

# 89 bytes:
f=lambda n:f(n-1)+'Yeah\n'*((n-1)%3<1)+'But\n'*((n-1)%2<1)+'No\n'*((n-1)%3==1)if n else""