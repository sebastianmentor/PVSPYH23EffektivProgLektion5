from itertools import islice

def get_index_of_words_in_file(file_handler):
    current_pos = 0
    for line in file_handler:
        if line:
            yield current_pos
        for letter in line:
            current_pos += 1
            if letter == " ":
                yield current_pos

    
with open("test1.txt", "r") as f:
    iterator = get_index_of_words_in_file(f)
    results = islice(iterator,3, 9)
    print(list(results))