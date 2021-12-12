puzzle_input = './Day 3 - Puzzle - Input - simple.txt'

with open(puzzle_input, 'r') as input_file:
    for puzzle_contents_line in input_file:
        lines = input_file.readlines()
        for line in lines:
            print(int(line, 2))

#        reports = [int(line, 2) for line in lines]

#counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#for report in reports:
#    i = 0
#    num_of_bits = len(counts)
#    while i < num_of_bits:
#        counts[num_of_bits-1-i] += report >> i & 1
#        i += 1