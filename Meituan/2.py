"""
http://blog.sina.com.cn/s/blog_bb0476c10102vre8.html
"""

import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s : %(message)s"
)

def rotate_matrix(n):
    # creation matrix
    matrix = [[(j + i * n) for j in range(1, n + 1)] for i in range(n)]

    # print original matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print("")

    # up
    for i in range(n - 1):
        for j in range(i + 1):
            # logging.debug(j)
            # logging.debug(n - 1 + j)
            print(matrix[j][n - i - 1 + j], end=" ")
        print("")

    # middle
    for i in range(n):
        print(matrix[i][i], end=" ")
    print("")

    # bottom
    for i in range(n - 1):
        for j in range(n - i - 1):
            logging.debug([i + 1 + j])
            print(matrix[i + 1 + j][j], end=" ")
        print("")

rotate_matrix(3)
