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
# show the counts
print("\nWord occurrences:")
for word, count in sorted_counts.items():
    print(f"{word}: {count}")

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

