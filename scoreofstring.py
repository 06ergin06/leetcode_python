# https://leetcode.com/problems/score-of-a-string/description/
def scoreOfString(s):
    y = 0
    for i in range(0,(len(s) - 1)):
        y += abs(ord(s[i]) - ord(s[i+1])) 
        
    return y
print(scoreOfString("hello"))