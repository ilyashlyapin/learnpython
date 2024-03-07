# Reverse the order of words in a given sentence (an array of characters).
# "Hello World"
# "World Hello"

def reverse_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse the order of words
    reversed_words = words[::-1]
    # Join the reversed words back into a sentence
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Example usage:
sentence = "Hello world! This is a test."
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)
