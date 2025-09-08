import numpy as np


def ways(n):                 # Define the ways function with n as the input.
    return n // 5 + 1        # Return input n floor divided by 5 plus 1 because zero nickles is always an option so the answer will be

import numpy as np

def lowest_score(names, scores):
    lowScoreInd = np.argmin(scores)
    lowScoreStu = names[lowScoreInd]
    return lowScoreStu


def sort_names(names, scores):
    namesArray = np.array(names)
    scoresArray = np.array(scores)
    sortedInd = np.argsort(scoresArray)[::-1]
    sortedNames = namesArray[sortedInd]
    return list(sortedNames)