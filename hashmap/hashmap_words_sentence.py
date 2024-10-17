# Initialize a HashMap to store the word counts
word_counts = {}

# List of words to count
words_to_count = ["apple", "banana", "cherry"]

# String in which to count words
string_to_search = "apple banana apple cherry apple banana"

# Split the string into individual words
words_in_string = string_to_search.split()

# TODO: Count the appearances of each word in the string
for word in words_in_string:
    if word in words_to_count:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    else:
        continue

# Output the counts of each word
print(word_counts)