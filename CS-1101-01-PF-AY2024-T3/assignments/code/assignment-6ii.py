def sentence_to_reversed_wordlist(sentence):
    """Converts a sentence into a word list and then reverses the word list.
    Args:
    sentence: The input sentence as a string.
    Returns:
    A list containing the words of the sentence in reverse order.
    """
    # Split the sentence into words using the split() method
    word_list = sentence.split()
    
    # Reverse the word list using slicing
    reversed_word_list = word_list[::-1]
    return reversed_word_list

# Example usage
sentence = "This is a sample sentence."
reversed_words = sentence_to_reversed_wordlist(sentence)
print("Original Sentence:", sentence)
print("Reversed Words:", reversed_words)