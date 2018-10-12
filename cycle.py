'''
To write a program that outputs either another program, or s depending on n. If n = 1, Then your code should output code which outputs s. If n = 2, Your code should output code which outputs code which outputs s and so on.
'''


# 55 bytes:
c=lambda s,n:c("(lambda:"+repr(s)+")()",n-1)if n else s
