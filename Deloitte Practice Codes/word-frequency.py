"""
Counts the no. of words in a given string and display in the form of dictionary
"""


def count_words(input_string: str) -> dict:
    """
    Counts the no. of words in input_string

    Args:
        input_string (str): String whose no. of words are to be counted

    Returns:
        dict: key value pairs of words and their frequency
    """
    word_counter = {}
    input_string = input_string.split()
    for word in input_string:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    # return dictionary object
    return word_counter


# Read a string
input_string = input()

# Function call
words_counter = count_words(input_string)

# Display the dictionary object
print(words_counter)
