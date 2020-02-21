'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # If the word has less than 2 characters then return 0.
    if len(word) < 2:
        return 0

    # Increase the counter by 1 if two adjacent characters have 'th' in them and continue searching through the word.
    elif word[0:2] == 'th':
        return count_th(word[1:]) + 1

    # Continue searching through the word if the elif statement doesn't work
    else:
        return count_th(word[1:])
