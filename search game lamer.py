from nltk.corpus import words

with open('search game lamer.txt', 'r') as f_in:
    table = []
    for line in f_in:
        table.append(line.strip().split(' '))
print(table)


def word_checker(letters):
    true_words = []
    letters_len = len(letters)
    # print(letters_len)
    for iteration in range(3, letters_len + 1):
        # print(iteration)
        for word_range in range(0, letters_len - iteration + 1):

            candidate = ''
            addr = tuple()
            # start = tuple(tuple[word_range, iteration])
            start = letters[word_range][-1]
            end = None
            for char in range(word_range, word_range + iteration):
                candidate += letters[char][0]
                if char == word_range + iteration - 1:
                    end = letters[char][-1]

            # print(candidate)
            candidate2 = candidate[::-1]
            if candidate.lower() in words.words('en'):
                true_words.append(tuple([candidate, start, end]))
            if candidate2.lower() in words.words('en'):
                true_words.append(tuple([candidate2, end, start]))
        # print()
    return true_words


print(word_checker(table[2]))


def normalize(table_in):
    table_out = []
    for i in range(len(table_in)):
        put_in = []
        for j in range(len(table_in[0])):
            # addr = tuple([i, j])
            put_in.append(tuple([table_in[i][j], tuple([i, j])]))
        table_out.append(put_in)
    return table_out


for x in normalize(table):
    print(x)


def row_checker(a_table):
    answer = []
    for row in a_table:
        answer.append(word_checker(row))
    return answer


def col_checker(a_table):
    answer = []

    for j in range(0, len(a_table[0])):
        col = []
        for i in range(0, len(a_table)):
            col.append(a_table[i][j])

        answer.append(word_checker(col))
    return answer


def diagonal_checker_LtR(a_table):
    answer = []
    for k in range(len(a_table[0])):
        diagonal = []
        i = 0
        j = k
        while True:
            diagonal.append(a_table[i][j])
            i += 1
            j += 1
            if i >= len(a_table) or j >= len(a_table[0]):
                break
        answer.append(word_checker(diagonal))

    for k in range(1, len(a_table)):
        diagonal = []
        j = 0
        i = k
        while True:
            diagonal.append(a_table[i][j])
            j += 1
            i += 1
            if i >= len(a_table) or j >= len(a_table[0]):
                break
        answer.append(word_checker(diagonal))

    return answer


def diagonal_checker_RtL(a_table):
    answer = []
    for k in range(len(a_table[0]) - 1, -1, -1):
        diagonal = []
        i = 0
        j = k
        while True:
            diagonal.append(a_table[i][j])
            i += 1
            j -= 1
            if i >= len(a_table) or j < 0:
                break
        answer.append(word_checker(diagonal))

    for k in range(1, len(a_table)):
        diagonal = []
        j = len(a_table[0]) - 1
        i = k
        while True:
            diagonal.append(a_table[i][j])
            j -= 1
            i += 1
            if i >= len(a_table) or j < 0:
                break
        answer.append(word_checker(diagonal))

    return answer


# print(word_checker(normalize(table)[-1]))

# print(col_checker(normalize(table)))
# print(row_checker(normalize(table)))
# print(diagonal_checker_LtR(normalize(table)))
# print(diagonal_checker_RtL(normalize(table)))

def game_lamer(word_table):
    word_table = normalize(word_table)
    results = [row_checker(word_table), col_checker(word_table), diagonal_checker_RtL(word_table),
               diagonal_checker_LtR(word_table)]
    return results


for result in (game_lamer(table)):
    print(result)
