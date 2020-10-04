"""

--Problem 4 - Hand Length--

"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    
    length = 0
    
    for letter in hand:
        length += hand[letter]
    
    return length