def readFile(fileLocation):
    with open(fileLocation) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def countWords(someString):
    words = someString.split()
    return len(words)

def countLetters(someString):
    estadisticas = {}
    lowered_string = someString.lower()
    for caracter in lowered_string:
        if caracter in estadisticas:
            estadisticas[caracter] += 1
        elif caracter.isalpha():
            estadisticas[caracter] = 1
    
    #Convert to a list
    ls_estadisticas = []
    for item in estadisticas:
        new_item = {"char":item,"num":estadisticas[item]}
        ls_estadisticas.append(new_item)

    #Sort using sort_on function
    ls_estadisticas.sort(key=sort_on, reverse=True)
    return ls_estadisticas

def main():
    bookToRead = "books/frankenstein.txt"
    file_contents = readFile(bookToRead)
    print("--- Begin report of books/frankenstein.txt ---")
    wordcount = countWords(file_contents)
    print(f"{wordcount} words found in the document\n")
    ls_chars = countLetters(file_contents)
    for item in ls_chars:
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    print("--- End report ---")

main()