#3. Написать функцию thesaurus()
def key_maker(strings_for_key):
    key = strings_for_key[0]
    return key

def thesaurus(*unsorted_strings):
    keys = []
    sorted_strings = []
    thesaurus_dict = {}

    for i in range(len(unsorted_strings)):
        keys.append(key_maker(unsorted_strings[i]))
        sorted_strings.append(unsorted_strings[i])

    sorted_strings.sort()
    keys.sort()
    i = 1
    while i < len(keys):
        if keys[i] == keys[i - 1]:
            del keys[i]
        i += 1

    for i in range(len(keys)):
        same_surnames = []
        for j in range(len(sorted_strings)):
            if sorted_strings[j][0] == keys[i]:
                same_surnames.append(sorted_strings[j])
            thesaurus_dict[keys[i]] = same_surnames

    return thesaurus_dict

surnames_dict = thesaurus("Иван", "Мария", "Петр", "Илья")
for item in surnames_dict.items():
    print("\"" + item[0] + "\":", item[1])