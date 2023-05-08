def diagonalSum(mat):
    """
    :type mat: List[List[int]]
    :rtype: int
    """

    sum = 0
    last = len(mat) - 1

    for i in range(len(mat)):
        sum += mat[i][i]
        if last-i != i:
            sum += mat[i][last-i]


    return sum