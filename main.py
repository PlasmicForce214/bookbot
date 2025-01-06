
def word_count(string):
    words = string.split()
    return len(words)


def char_count(myString):
    lower_string = myString.lower()
    chDict = {}
    for char in lower_string:
        if char in chDict:
            chDict[char] += 1
        else:
            chDict[char] = 1
    return chDict


def sort_on(dict):
    return dict["num"]


def conversion(file_contents):
    charDict = char_count(file_contents)
    tempArr = []
    for item in charDict:
        tempDict = {}
        if item.isalpha():
            tempDict["char"] = item
            tempDict["num"] = charDict[item]
            tempArr.append(tempDict)
    return tempArr


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = word_count(file_contents)
        char_array = conversion(file_contents)
        char_array.sort(key=sort_on, reverse=True)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")
        for item in char_array:
            print(f"The {item["char"]} character was found {item["num"]} times")
        print("--- End report ---")


if __name__ == "__main__":
    main()
