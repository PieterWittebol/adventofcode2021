puzzle_input = './Day 3 - Puzzle - Input - simple.txt'
puzzle_contents_line_count = 0
binary_list = []
binary_character_list = []
binary_dictionary = {}

def most_common(lst):
    return max(set(lst), key=lst.count)

def least_common(lst):
    return min(set(lst), key=lst.count)

with open(puzzle_input, 'r') as f:
    puzzle_contents = f.readlines()
    binary_character_list = []
    for puzzle_contents_line in puzzle_contents:
        puzzle_contents_line = puzzle_contents_line.strip()
        puzzle_contents_line_count += 1
        binary_list = [digit for digit in puzzle_contents_line]
        enumerated_binary_list = list(enumerate(binary_list))
        print(puzzle_contents_line_count, enumerated_binary_list)
        binary_dictionary = {puzzle_contents_line_count}
#        for item in enumerated_binary_list:
#            binary_dictionary_primary_key = puzzle_contents_line_count
#            binary_dictionary_key = item[0]
#            binary_dictionary_value = item[1]
#            print("Primary key: {}\nKey: {}\nValue: {}".format(binary_dictionary_primary_key, binary_dictionary_key, binary_dictionary_value))
#            binary_dictionary[binary_dictionary_primary_key] = {binary_dictionary_key: binary_dictionary_value}
print(binary_dictionary)
#        for binary_list_item in binary_list[0]:
#            binary_character_list.append(binary_list_item)
#    print("Most common character is {}".format(most_common(binary_character_list)))
#    print("Least common character is {}".format(least_common(binary_character_list)))
#    print(binary_character_list)