# Define a function that returns all the divisors of an integer
from dataclasses import replace
from Book_analysis import punctuation_remove

def divisors(n: int):
    """
    Gets all the divisors of a number provided
    :return: Integer
    """
    divisors = []
    if n == 0:
        return print("Please introduce a value bigger than 0")
    if n < 0:
        return print("Please introduce a positive integer")
    for i in range (1, n+1):
        if n%i == 0:
            divisors.append(i)
    return divisors

print(divisors(64))
print(divisors(28))
print(divisors(-32))

#Write a function that takes the name of a text file as a parameter. Print out the 3-letter words that start with b
import string


def three_lettered_b(file_path: string) -> None:
    """
    Reads a .txt file and prints all three-letter words that start with 'b'.

    Parameters:
        file_path (str): The path to the text file.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()  # Convert text to lowercase
    except FileNotFoundError:
        print(f"Error: {file_path} does not exist")
        return
    punctuation_remove = ",.\"()'-!?"
    cleaned_text = text
    for character in punctuation_remove:
        cleaned_text = cleaned_text.replace(character, "")
    words = cleaned_text.split()
    for word in words:
        if len(word) == 3 and word[0] == 'b':
            print(words)
three_lettered_b("Bs.txt")

#Write a function that forces the user to enter a multiple of 6. Use try and except

def multiple6 (n):
    """
    Function that only works when using a multiple of 6 returning that integer
    :param n: Number
    :return: Wether the number is multiple of 6 or not
    """
    try:
       if n % 6 == 0:
           print(f"{n} is indeed a multiple of 6!")
       else:
           print(f"{n} is not a multiple of 6, please introduce a valid multiple")
    except TypeError:
        print("Please introduce a valid integer")
    return
multiple6(2)
multiple6(12)