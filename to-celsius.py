def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = sentence.rindex(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"


# def is_palindrome(input_string):
#     # We'll create two strings, to compare them
#     new_string = input_string.replace(" ", "").lower()
#     reverse_string = new_string[::-1]

#     # Traverse through each letter of the input string
#     if new_string == reverse_string:
#         return True
#     return False


# print(is_palindrome("Never Odd or Even"))  # Should be True
# print(is_palindrome("abc"))  # Should be False
# print(is_palindrome("kayak"))  # Should be True


# exit


# def to_celsius(x):
#     return (x - 32) * (5/9)


# print("Before Formatting")
# for fahrenheit in range(0, 151, 10):
#     print("{} F | {}".format(fahrenheit, to_celsius(fahrenheit)))

# print("After Formatting")
# for fahrenheit in range(0, 151, 10):
#     print("{:>3} F | {:>6.2f}".format(fahrenheit, to_celsius(fahrenheit)))
