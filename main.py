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

def sort_on(dict):
    return dict["num"]

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

no_words = word_count(file_contents)
frequency_char = char_count(file_contents)

#print("a".isalpha())

char_list = []
for character in frequency_char:
    temp_dict = {}
    if character.isalpha():
        temp_dict["name"] = character
        temp_dict["num"] = frequency_char[character]
        char_list.append(temp_dict)

char_list.sort(reverse=True, key=sort_on)
#print(char_list)

print(f"{no_words} words found in the document\n")
for entry in char_list:
    print(f"The '{entry['name']}' was found {entry['num']} times")
print("--- End report ---")