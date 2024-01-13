"""
From the input a string, create a dictionary of alphabets in the string and their count
"""


def count_alphabets(string_input: str) -> dict:
    """
    Create a dictionary of alphabets in the string and their count

    Args:
        string_input (str): Input string whose alphabets are to be counted

    Returns:
        dict: Dictionary with count of the alphabets in the string
    """

    alphabet_dict = {}
    for letter in string_input:
        if letter in alphabet_dict:
            alphabet_dict[letter] += 1
        else:
            alphabet_dict[letter] = 1

    # Return dictionary object
    return alphabet_dict


# Read the string input
string_input = input()

# Call the function
alphabet_dict = count_alphabets(string_input)

# Display the dictionary
print(alphabet_dict)
