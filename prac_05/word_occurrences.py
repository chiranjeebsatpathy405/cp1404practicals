# Input any string
text = input("Enter a string: ")

# lowercase conversion to make case insensitive  and split into words
words = text.lower().split()

# empty dictionary creation as word_counts to store word counts
word_counts = {}

# Count each word
for word in words:
    # Remove  commas, periods, etc.
    word = word.strip(".,!?")
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
sorted_counts =dict(sorted(word_counts.items()))

# Determine the longest word for alignment
max_word_length = max(len(word) for word in sorted_counts)

for word, count in sorted_counts.items():
    print(word.ljust(max_word_length), str(count).rjust(5))

    # Enter a string: this is a collection of words of nice words this is a fun thing it is
    # Word occurrences:
   # this: 2
    #is: 3
    #a: 2
    #collection: 1
   # of: 2
   # words: 2
   # nice: 1
   # fun: 1

