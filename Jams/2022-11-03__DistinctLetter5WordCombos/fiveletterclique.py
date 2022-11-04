import numpy as np
import time


english_dictionary_filename = 'words_alpha.txt'
output_path = 'fiveletterclique.txt'

start_time = time.perf_counter()

with open(english_dictionary_filename, 'r') as english_dictionary_file:

    # Omit the newline character from the end of each word.
    # Filter the list of words to contain only words that have five letters.
    words = np.array([
        word[:-1]
        for word in english_dictionary_file
        if len(word) == 6
    ])


letter_numerosity = np.array([0, 18, 11, 12,  1, 20, 16, 13,  3, 23, 17,  8, 14,  7,  4, 15, 25,
                              5,  2,  9,  6, 21, 19, 24, 10, 22])

# This casts words from int64 to int32
words_as_ascii_numbers = words.view('int32').reshape((-1, 5))
words_as_0_based_numbers = words_as_ascii_numbers - 97

words_with_letters_mapped_to_numerosity = letter_numerosity[words_as_0_based_numbers]

#
duplicates = (
    (
        words_with_letters_mapped_to_numerosity.reshape((-1, 1, 5))
        == words_with_letters_mapped_to_numerosity.reshape((-1, 5, 1))
    ).sum(axis=(1, 2)) < 6
)


rmduplicates = words_with_letters_mapped_to_numerosity[duplicates, :]
balist = (2**rmduplicates).sum(axis=1)
balist2, counts = np.unique(balist, return_counts=True)
words2 = words[duplicates][np.argsort(balist)]
anagramsl = np.concatenate([[0], np.cumsum(counts)])


def K(A, B):
    return np.logical_not(B & A.reshape((-1, 1)))


exp = 2**np.array(range(0, 27))
dexp = 2**26-exp
rs = np.searchsorted(balist2, exp)


def addtaboo(words):
    words = words[(2**26*words[:, 1]+words[:, 0]).argsort()]
    index = words[:, 1].sum()
    n_words = np.concatenate([words[-index:], words])
    n_words[:index, 1] = 0
    qs = np.searchsorted(n_words[:index, 0], dexp)
    for i in range(25, -1, -1):
        n_words[qs[i+1]:qs[i], 0] += 2**i
        if qs[i] == index:
            break
    return n_words


def addword(words):
    words = words[words[:, 0].argsort()]
    qs = np.searchsorted(words[:, 0], dexp)
    l = words.shape[0]
    words_list = []
    for i in range(25, -1, -1):
        uniq, index, counts = np.unique(
            words[qs[i+1]:qs[i], 0], return_index=True, return_counts=True)
        nz = np.nonzero(K(uniq, balist2[rs[i]:rs[i+1]]))
        if len(nz[0]) == 0:
            continue
        repeats = counts[nz[0]]
        balistinds = rs[i]+np.repeat(nz[1], repeats)
        currinds = qs[i+1]+np.repeat(index[nz[0]]+np.cumsum(repeats),
                                     repeats)-np.arange(1, sum(repeats)+1)
        newarr = np.hstack(
            (words[currinds], balist2[balistinds].reshape((-1, 1))))
        newarr[:, 0] += newarr[:, -1]
        words_list.append(newarr.copy())
        if qs[i] == l:
            break
    n_words = np.concatenate(words_list)
    return n_words


G = np.array([[0, 1]])
for i in range(5):
    G = addword(addtaboo(G))
outputs = G[:, 2:]
outputs2 = np.searchsorted(balist2, outputs)
V = anagramsl[1:]-anagramsl[:-1]
wordsquarelist = np.zeros((V[outputs2].prod(axis=1).sum(), 5), dtype='<U5')
t = 0
for i in range(len(outputs)):
    word = np.array(list(np.ndindex(tuple(V[outputs2[i]]))))
    index = anagramsl[outputs2[i]]+word
    wordsquarelist[t:t+word.shape[0]] = words2[index]
    t += word.shape[0]
lines = [' '.join(word) for word in wordsquarelist]
with open(output_path, 'w') as english_dictionary_file:
    english_dictionary_file.write('\n'.join(lines))
print(time.perf_counter()-start_time)
