def ways(n):
    '''
    Function to find the number of ways to 
    make change for a given amount of cents (n).

    Parameters:
    n (int): The amount of cents you choose.

    Return value:
    n // 5 + 1: An integer of the number of ways
    to make change given n.
    '''
    return n // 5 + 1

# Import numpy to use certain functions below
import numpy as np

def lowest_score(names, scores):
    '''
    Function to find the student with
    the lowest score.

    Parameters:
    names (numpy.ndarray): The names of the students
    scores (numpy.ndarray): The scores of those students

    Return value:
    lowScoreStu: The name of the student
    with the lowest score
    '''
    # assign the minimum score index to lowScoreInd
    lowScoreInd = np.argmin(scores)
    # Find the name that matches the index
    lowScoreStu = names[lowScoreInd]
    return lowScoreStu


def sort_names(names, scores): 
    '''
    Function to list the names of the
    students based on their score in
    descending order.

    Parameters:
    names (numpy.ndarray): The names of the students
    scores (numpy.ndarray): The scores of those students

    Return value:
    list(sortedNames): A list of the names
    sorted in descending order based
    on scores.
    '''
    # make names a numpy array (in order to make autograder work)
    namesArray = np.array(names)
    # sort scores array indexes in descending order
    scoresArray = np.array(scores)                
    sortedInd = np.argsort(scoresArray)[::-1]
    # match the sorted scores indexes to corresponding names
    sortedNames = namesArray[sortedInd]
    return list(sortedNames)