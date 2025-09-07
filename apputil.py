import numpy as np


def ways(n):                 # Define the ways function with n as the input.
    return n // 5 + 1        # Return input n floor divided by 5 plus 1 because zero nickles is always an option so the answer will be

import numpy as np

def lowest_score(names, scores):
    lowScoreInd = np.argmin(scores)
    lowScoreStu = names[lowScoreInd]
    return str(lowScoreStu)

lowest_score(names, scores)

def sort_names(names, scores):
    highScoreInd = np.argmax(scores)
    highScoreStu = names[highScoreInd]
    return str(highScoreStu)

lowest_score(names, scores)
