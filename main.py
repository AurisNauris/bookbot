def word_count(my_string):
    return len(my_string.split())

def char_count(my_string):
    my_string = my_string.lower()
    char_dict = {}
    for char in my_string:
        if not char in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char]+=1
    return char_dict


with open("books/frankenstein.txt") as f:
    file_contents = f.read()

frequency_char = char_count(file_contents)
#print (word_count(file_contents))

print (frequency_char)