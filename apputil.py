import numpy as np


def ways(n):                 # Define the ways function with n as the input.
    return n // 5 + 1        # Return input n floor divided by 5 plus 1 because zero nickles is always an option so the answer will be

import numpy as np           # Import numpy for this question

def lowest_score(names, scores):                  # define the function with two inputs
    lowScoreInd = np.argmin(scores)               # assign the minimum score index to lowScoreInd 
    lowScoreStu = names[lowScoreInd]              # Find the name that matches the index
    return lowScoreStu                            # Return the students name with the lowest score


def sort_names(names, scores):                    # define the function with the same two inputs as lowest_score
    namesArray = np.array(names)                  # make names a numpy array (in order to make autograder work)
    scoresArray = np.array(scores)                # make scores a numpy array (also in order to make autograder work)
    sortedInd = np.argsort(scoresArray)[::-1]     # sort scores array indexes in descending order
    sortedNames = namesArray[sortedInd]           # match the sorted scores indexes to corresponding names
    return list(sortedNames)                      # return a list of the sorted names