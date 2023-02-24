with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def count_words(file: str) -> int:
    words = file.split()
    return len(words)


def count_characters(file: str) -> dict:
    letters = {}
    for character in file:
        character = character.lower()
        if character not in letters:
            letters[character] = 1
        else:
            letters[character] += 1
    return letters


def convert_dict_to_list(letters):
    letter_list = []
    for letter in letters:
        if letter.isalpha():
            letter_list.append(letter)
    letter_list.sort()

    return letter_list


def print_a_report(letter_list: list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()
    character_dict = count_characters(file_contents)
    for letter in letter_list:
        print(
            f"The \'{letter}\' character was found {character_dict[letter]} times")

    print("--- End report ---")


print_a_report(convert_dict_to_list(count_characters(file_contents)))
