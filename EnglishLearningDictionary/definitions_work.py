import random


data_file_path = "./data/dictionary.txt"


def get_definitions_for_table():
    definitions = []
    with open(data_file_path, "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[0:]:
            word, definition, translation, sphere, source = line.split(";")
            definitions.append([cnt, word, definition, translation, sphere])
            cnt += 1
    return definitions


def write_definition(new_word, new_definition, new_translation, sphere, user):
    utility.set_quantity_in_sphere(sphere)
    old_definitions = []
    new_definition_lines = []
    new_definition = [new_word, new_definition, new_translation, sphere, user]
    with open(data_file_path, "r", encoding="utf-8") as f:
        existing_definitions_lines = [line.strip("\n") for line in f.readlines()]
    old_definitions_lines = existing_definitions_lines[0:]
    for definitions in old_definitions_lines:
        old_definitions.append(definitions.split(";"))
    old_definitions.append(new_definition)
    definitions_sorted = old_definitions
    definitions_sorted.sort(key=lambda _sphere: _sphere[3])
    for definition in range(len(definitions_sorted)):
        new_definition_lines.append(";".join(definitions_sorted[definition]))
    with open(data_file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_definition_lines))


class ForGame:
    __sphere_quantity = {}

    def __init__(self):
        self.__answer = 'none'
        with open(data_file_path, "r", encoding="utf-8") as f:
            file_list = f.readlines()
        for definitions in file_list:
            existing_definition = definitions.split(";")
            sphere = existing_definition[3]
            if sphere not in self.__sphere_quantity:
                self.__sphere_quantity[sphere] = 0
            self.__sphere_quantity[sphere] += 1

    def get_definition_for_game(self):
        with open(data_file_path, "r", encoding="utf-8") as f:
            file_list = f.readlines()
        size = len(file_list)
        choice = random.randint(0, size - 1)
        word, definition, *_ = file_list[choice].split(";")
        self.__answer = word
        return word, definition

    def get_definition_in_sphere_for_game(self, sphere):
        with open(data_file_path, "r", encoding="utf-8") as f:
            file_list = f.readlines()
        size = len(file_list)
        choice = random.randint(0, self.__sphere_quantity[sphere] - 1)
        if sphere == "IT":
            word, definition, *_ = file_list[choice].split(";")
        elif sphere == "Physics":
            word, definition, *_ = file_list[size - choice - 1].split(";")
        elif sphere == "Math":
            word, definition, *_ = file_list[choice + self.__sphere_quantity["IT"]].split(";")
        else:
            word, definition, *_ = file_list[size - choice - self.__sphere_quantity["Physics"] - 1].split(";")
        self.__answer = word
        return word, definition

    def set_quantity_in_sphere(self, sphere):
        self.__sphere_quantity[sphere] += 1
        print(self.__sphere_quantity)

    def answer_check(self, answer):
        return answer == self.__answer


utility = ForGame()
