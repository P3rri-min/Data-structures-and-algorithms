# Name:Irene Ndinda
# Date:19/03/2026
# Description:string reversal and character frequency

# string reversal method 1:slicing
def reverse_string_slicing(text):
    return text[::-1]
text = "Hello, World!"
reversed_text = reverse_string_slicing(text)
print("reversed string (slicing):", reversed_text)

# string reversal method 2: loop
def reverse_string_loop(text):
    reversed_text = ""
    for char in text :
        reversed_text = char + reversed_text
    return reversed_text
reversed_text_loop = reverse_string_loop(text)
print("reversed string (loop):", reversed_text_loop)

# character frequency method 1: using a dictionary
def char_frequency_dict(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
        return frequency
    text = "Hello, world!"
    frequency_result = char_frequency_dict(text)
    print("character frequency (dictionary):", frequency_result)


    

