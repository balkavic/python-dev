def english_words():
    word_file = open("words.english.txt", 'r')
    all_words = word_file.read().splitlines()
    word_file.close()
    return all_words

