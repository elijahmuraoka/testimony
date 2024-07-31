def count_words():
    with open("testimony.md") as f:
        word_count = len(f.read().split())
        print("Word Count:", word_count)
        return word_count


count_words()
