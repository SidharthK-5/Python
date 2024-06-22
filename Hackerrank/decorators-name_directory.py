"""
This program is a solution for a problem on Hackerrank.
It implements a decorator function called `person_lister` and
a formatting function called `name_format`.
The `person_lister` decorator sorts a list of people by their age and applies
a given function to each person.
The `name_format` function formats a person's name based on their gender and name.

Usage:
1. Enter the number of people.
2. Enter the details of each person (first name, last name, age, gender).
3. The program will sort the list of people by age and format their names accordingly.
4. The formatted names will be printed in the console.
"""


def person_lister(function: callable) -> callable:
    """
    A decorator function that sorts a list of people by their age and applies
    a given function to each person.

    Args:
        function (callable): The function to be applied to each person.

    Returns:
        callable: The decorated function.
    """

    def inner(people: list[tuple[str, str, int, str]]) -> list[str]:
        """
        The inner function that sorts the list of people by age and applies
        the given function to each person.

        Args:
            people (list[tuple[str, str, int, str]]): The list of people.

        Returns:
            List[str]: The formatted names of the people.
        """
        return list(map(function, sorted(people, key=lambda x: int(x[2]))))

    return inner


@person_lister
def name_format(person: tuple[str, str, int, str]) -> str:
    """
    A formatting function that formats a person's name based on their gender and name.

    Args:
        person (Tuple[str, str, int, str]): The details of the person.

    Returns:
        str: The formatted name of the person.
    """
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == "__main__":
    people = [input().split() for _ in range(int(input()))]
    print(*name_format(people), sep="\n")
