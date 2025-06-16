def num_words(string):
    mylist = string.split()
    return len(mylist)

def char_and_count(string):
    my_string = string.lower()
    char_list = list(my_string)
    my_dict = {}
    for char in char_list:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict

def sort_dict(my_dict):
    return sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
    
