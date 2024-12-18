import nltk
from pymorphy3 import MorphAnalyzer


# nltk.download('punkt')


def extract_matching_pairs(text):
    words = nltk.word_tokenize(text)
    pairs = []
    for i in range(len(words) - 1):
        word1, word2 = m.parse(words[i])[0], m.parse(words[i + 1])[0]
        if ((word1.tag.POS == 'NOUN' or word1.tag.POS == 'ADJF') and (word2.tag.POS == 'NOUN' or word2.tag.POS == 'ADJF') and
                (word1.tag.case == word2.tag.case) and (word1.tag.number == word2.tag.number) and (word1.tag.gender == word2.tag.gender)):
            pairs.append((word1.normal_form, word2.normal_form))
    return pairs


with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

m = MorphAnalyzer()
matching_pairs = extract_matching_pairs(text)

with open('output.txt', 'w', encoding='utf-8') as file:
    for pair in matching_pairs:
        file.write(f"{pair[0]} {pair[1]}\n")