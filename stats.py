def num_words(string):
    words = string.split()
    count = 0
    for word in words:
        count += 1
    return count

def characters_found(string):
    char_dict = {}
    for char in string:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
        #print (f"updated {char}")
    return char_dict

def sort_dict(dictionary):
    list_of_char_info = []
    for char, count in dictionary.items():
        char_dict = {"char":char, "count": count}
        list_of_char_info.append(char_dict)
    list_of_char_info.sort(reverse=True, key=lambda x: x["count"])
    for item in list_of_char_info:
        character = item["char"]
        if character.isalpha() == True:
            print(f"{character}: {item['count']}")