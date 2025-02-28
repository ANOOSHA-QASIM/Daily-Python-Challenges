# Day 2 - Python String Challenges
print("=" * 60)
print(" DAY 2 - PYTHON STRING CHALLENGES ".center(60, "-"))
print("=" * 60)

# 1. Find the Longest Word
print("\n[ Task 1: Find the Longest Word ]")
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print(f"Longest word: {longest_word}")

# 2. Count Total Words
print("\n[ Task 2: Count Total Words ]")
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print(f"Total words: {word_count}")

# 3. Reverse Words in Sentence
print("\n[ Task 3: Reverse Words in Sentence ]")
sentence = input("Enter a sentence: ")
reversed_sentence = " ".join(sentence.split()[::-1])
print(f"Reversed sentence: {reversed_sentence}")

# 4. Join Words with Hyphen
print("\n[ Task 4: Join Words with Hyphen ]")
sentence = input("Enter a sentence: ")
hyphen_joined = "-".join(sentence.split())
print(f"Hyphen-joined sentence: {hyphen_joined}")

# 5. Count Total Characters (Without Spaces)
print("\n[ Task 5: Count Characters (Without Spaces) ]")
sentence = input("Enter a sentence: ")
char_count = len("".join(sentence.split()))
print(f"Total characters (without spaces): {char_count}")

print("\n" + "=" * 60)
print(" END OF CHALLENGE ".center(60, "-"))
print("=" * 60)
