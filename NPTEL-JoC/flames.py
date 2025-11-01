"""
Program to determine the relationship between two people using the FLAMES game logic.
"""


def remove_matching_letters(name1, name2):
    """
    Remove matching letters from both names and return the count of remaining letters.
    """
    name1_list = list(name1.replace(" ", "").lower())
    name2_list = list(name2.replace(" ", "").lower())

    for letter in name1[:]:
        if letter in name2_list:
            name1_list.remove(letter)
            name2_list.remove(letter)

    return len(name1_list) + len(name2_list)


def flames_relationship(name1, name2):
    """
    Determine the relationship between two people based on the FLAMES game logic.
    """
    flames = ["F", "L", "A", "M", "E", "S"]
    count = remove_matching_letters(name1, name2)

    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1 :]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[: len(flames) - 1]

    relationship_dict = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings",
    }

    return relationship_dict[flames[0]]


if __name__ == "__main__":
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    relationship = flames_relationship(name1, name2)
    print(f"The relationship between {name1} and {name2} is: {relationship}")
