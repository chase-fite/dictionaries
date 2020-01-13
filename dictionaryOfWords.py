"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

word_definitions['crazy'] = "mentally deranged, especially as manifested in a wild or aggressive way"
word_definitions['melancholy'] = "a feeling of pensive sadness, typically with no obvious cause"

print(word_definitions, "\n")

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

print(word_definitions['crazy'], "\n")
print(word_definitions['melancholy'], "\n")

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for key in word_definitions:
    print(f'The definition of {key} is {word_definitions[key]}\n')