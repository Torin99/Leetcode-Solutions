def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    answer = 0
    for i in range(len(s)):
        if i < len(s)-1:
            if s[i] == 'I':
                if s[i+1] == 'V' or s[i+1] == 'X':
                    answer -= 2
            if s[i] == 'X':
                if s[i+1] == 'L' or s[i+1] == 'C':
                    answer -= 20
            if s[i] == 'C':
                if s[i+1] == 'D' or s[i+1] == 'M':
                    answer -= 200
        if s[i] == 'I': answer += 1
        if s[i] == 'V': answer += 5
        if s[i] == 'X': answer += 10
        if s[i] == 'L': answer += 50
        if s[i] == 'C': answer += 100
        if s[i] == 'D': answer += 500
        if s[i] == 'M': answer += 1000

    return answer
        
print(romanToInt("X"))
        