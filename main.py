def count_words(str_file):
    words = str_file.split()
    return len(words)

def add_letter_to_dict(add_char, dict_letters):
    try:
        dict_letters[add_char] += 1
    except:
        dict_letters[add_char] = 1
    return dict_letters

def sort_on(dict):
    return dict["num"]   

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words_number = count_words(file_contents)

dict1 = {}
for letter in file_contents:
    add_letter_to_dict(letter.lower(),dict1)

list_report =[]
for letter in dict1:
    if letter.isalpha():
        list_report.append({"char": letter, "num": dict1[letter]})
#        list_report.append({letter: dict1[letter]})
list_report.sort(reverse=True, key=sort_on)
#print(list_report)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{words_number} words found in the document")
for entry in list_report:
    print(f"The '{entry["char"]}' character was found {entry["num"]} times")
print("--- End report ---")
