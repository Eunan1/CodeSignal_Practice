# Function to count the frequency of each letter in a given sentence
def count_letter_frequency(sentence):
    letter_count = {}
    
    for letter in sentence:
        # TODO: If the character is a letter, update its count in the dictionary
        if letter in letter_count and letter.isalpha():
            letter_count[letter] += 1
        elif letter.isalpha():
            letter_count[letter] = 1 
        # or add it with a count of 1 if it's not already there
    return letter_count

# Example usage with a predefined sentence
sentence = "Once upon a time in a faraway library"
# TODO: Call the function with the sentence variable and print the result

ans = count_letter_frequency(sentence)
print(ans)