class ReportGenerator:
    def __init__(self, path_to_file: str):
        self.path_to_file = path_to_file
        self.__num_of_words = 0
        self.__letter_dict = {}
        self.__letter_list = []
        with open(self.path_to_file) as f:
            file_contents = f.read()
        self.file_contents = file_contents

    def __count_words(self):
        words = self.file_contents.split()
        self.__num_of_words = len(words)

    def __count_characters(self):
        letters = {}
        for character in self.file_contents:
            character = character.lower()
            if character not in letters:
                letters[character] = 1
            else:
                letters[character] += 1
        self.__letter_dict = letters

    def __convert_dict_to_list(self):
        letter_list = []
        for letter in self.__letter_dict:
            if letter.isalpha():
                letter_list.append(letter)
        letter_list.sort()

        self.__letter_list = letter_list

    def print_a_report(self):
        self.__count_words()
        self.__count_characters()
        self.__convert_dict_to_list()
        print(f"--- Begin report of {self.path_to_file} ---")
        print(f"{self.__num_of_words} words found in the document")
        print()
        character_dict = self.__letter_dict
        for letter in self.__letter_list:
            print(
                f"The \'{letter}\' character was found {character_dict[letter]} times")

        print("--- End report ---")


def main():
    new_report = ReportGenerator("books/frankenstein.txt")
    new_report.print_a_report()


main()
