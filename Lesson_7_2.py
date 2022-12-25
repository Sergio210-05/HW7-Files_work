
def decomposition(*files):
    file_dictionary = {}
    for file in files:
        with open(file, 'rt', encoding='utf8') as text:
            lines = text.readlines()
            file_dictionary[len(lines)] = {file: lines}
    return file_dictionary


def concatenate(decomp, result_file):
    with open(result_file, 'w', encoding='utf8') as f:
        for lines_number in sorted(list(decomp.keys())):
            file_name = list(decomp[lines_number].keys())[0]
            f.write(file_name + '\n')
            f.write(str(lines_number) + '\n')
            f.write(''.join(decomp[lines_number][file_name]) + '\n')


dictionary = decomposition('1.txt', '2.txt', '3.txt')
concatenate(dictionary, 'result.txt')
