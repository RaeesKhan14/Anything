def analyse_sentence(sentence): 
    words = sentence.lower().split()
    total_words = len(words)
    unique_words = len(set(words))
    most_common = Counter(words).most_common(1)[0]

    return total_words, unique_words, most_common
    
