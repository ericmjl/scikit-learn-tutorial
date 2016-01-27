"""
Author: Eric J. Ma
Date: 2015-03-17
"""

isoelectric_points = {
    'A':6.11,
    'R':10.76,
    'N':10.76,
    'D':2.98,
    'C':5.02,
    'E':3.08,
    'Q':5.65,
    'G':6.06,
    'H':7.64,
    'I':6.04,
    'L':6.04,
    'K':9.74,
    'M':5.74,
    'F':5.91,
    'P':6.30,
    'S':5.68,
    'T':5.60,
    'W':5.88,
    'Y':5.63,
    'V':6.02,
    'X':7.00,  # unknown so assign neutral
    'B':6.87,  # the average of D and N
    'Z':4.35,  # the average of E and Q
}

def get_isoelectric_point(aa):
    return isoelectric_points[aa]