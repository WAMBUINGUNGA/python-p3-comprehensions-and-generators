#!/usr/bin/env python3

def return_evens(num_list):
    # Use a list comprehension to filter out even elements
    even_elements = [num for num in num_list if num % 2 == 0]
    return even_elements

# Test the function
result = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result)  # Output: [0, 8]


def make_exclamation(sentence_list):
     # Use a list comprehension to add an exclamation mark to each string
    exclamation_list = [sentence + "!" for sentence in sentence_list]
    return exclamation_list

# Test the function
result = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(result)  # Output: ["Hello!", "I'm doing great!", "Python is fun!"]