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

no_words = word_count(file_contents)
frequency_char = char_count(file_contents)

#char_list = []
#for character in frequency_char:
#    new_dict = {character:frequency_char[character]}
#    char_list.append(new_dict)

#char_list.sort(reverse=True)
print(char_list)
#print(f"{no_words} words found in the document")