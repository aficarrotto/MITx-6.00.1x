"""

--Problem 3 - Printing Out all Available Letters--
Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, 
lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase 
English letters that are not in lettersGuessed.

Note that this function should return the letters in alphabetical order, as in the example above.

For this function, you may assume that all the letters in lettersGuessed are lowercase.

Ex.
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz

"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    string = "abcdefghijklmnopqrstuvwxyz"
    temp = ""
    for i in string:
        if i not in lettersGuessed:
            temp += i
    return temp