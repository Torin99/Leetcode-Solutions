# My Solution (Too Slow)
def bulbSwitch(n):
    """
    :type n: int
    :rtype: int
    """
    bulb_list = [False] * n
    half = n/2
    count = 0
    if n%2 != 0:
        half = (n+1)/2

    for i in range(n):
        if (i+1) <= half:
            for j in range(i,n, i+1):
                    bulb_list[j] = not bulb_list[j]
                    if bulb_list[j] == True: count += 1
                    else: count -= 1
        if (i+1) > half: 
            bulb_list[i] = not bulb_list[i]
            if bulb_list[i] == True: count += 1
            else: count -= 1
    return count
# Successful Solution O(1)
def bulbSwitchAnswer(n):
     return int(sqrt(n)) 