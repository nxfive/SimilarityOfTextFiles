from statistics import mean


def create_sentences_from_text(txt):
    '''
    Function deletes special characters and numbers from the text also tab and next line char.
    Split the text into sentences lists.
    '''

    special_characters = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '/', ':', ';', '<', '=',
                          '>', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~', '\t', '\n']
    numbers = [str(i) for i in range(10)]

    for i in special_characters:
        txt = txt.replace(i, '')
    for i in numbers:
        txt = txt.replace(i, '')

    sentences = txt.split(". ")
    return sentences


def create_words_from_sentence(sentence):
    '''Function returns sentence as a list of words'''
    return sentence.split(" ")


def calc_words_repetition(words1, words2):
    '''Function counts amount of words from sentence is also in second sentence'''

    the_same_words = 0
    for word1 in words1:
        for word2 in words2:
            if word1 == word2:
                the_same_words += 1
                break
    return the_same_words / max(len(words1), len(words2))


def calc_similarity(sent1, sent2):
    '''Function calculates the words similarity coefficient in the sentence.
    Function calls calc_words_repetition.'''

    # create list of words from sentence
    words1 = create_words_from_sentence(sent1)
    words2 = create_words_from_sentence(sent2)

    words_similarity_coefficient = calc_words_repetition(words1, words2)

    main_similarity_coefficient = words_similarity_coefficient
    return main_similarity_coefficient


def calc_similarity_in_texts(txt1, txt2):
    '''The function calculates similarity coefficient for
     the two given texts.'''

    sentences1 = create_sentences_from_text(txt1)
    sentences2 = create_sentences_from_text(txt2)

    sentences_indicators = []

    for i, sent1 in enumerate(sentences1):
        sim_max_val = 0
        for j, sent2 in enumerate(sentences2):
            sim_val = calc_similarity(sent1, sent2)

            if sim_val > sim_max_val:
                sim_max_val = sim_val

        sentences_indicators.append({"similarity": sim_max_val})
    return sentences_indicators


def print_stats(list_of_indicators):
    '''The function calculates the average similarity of all indicators '''

    stats = {'mean_similarity': mean([indicator["similarity"] for indicator in list_of_indicators])}
    print(f"Mean similarity: {stats['mean_similarity']}")


def main():
    try:
        txt1 = open("lorem.txt").read()
        txt2 = open("lorem2.txt").read()

        list_of_indicators = calc_similarity_in_texts(txt1, txt2)
        print_stats(list_of_indicators)

    except FileNotFoundError:
        print("File not found")


main()
