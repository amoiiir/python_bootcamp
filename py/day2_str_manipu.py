# text1 = "Hello world"

# # Slicing
# print(text1[0:5]) # start slicing from 0 to 4
# print(text1[3:]) # From index 3 to the end
# print(text1[:6]) # From start to index 5
# print(text1[-1])

# String formating
# name = "Amir Hamzah"
# age = 30

# message1 = f"Hello my name is {name} and my age is {age}"
# message2 = "My name is {} and my age is {}".format(name,age) #str.format()
# message3 = "My name is %s and I am %d years old" %(name, age)

# print(message1)
# print(message2)
# print(message3)

# Exercise
text = """Python is a powerful programming language. It's easy to learn and versatile! You can use Python for web development, data science,  andautomation. The syntax is clean and readable. This makes Python perfect for beginners and experts alike."""

num_words = len(text.split())
num_char = len(text.replace(" ", ""))
num_sentences = len(text.split("."))
sentence_count = text.count(".") + text.count("!") + text.count("?")

print(f"Number of words: {num_words}")
print(f"Number of characters: {num_char}")
print(f"Number of sentences: {num_sentences}")
print(f"Number of sentences using punctuation count: {sentence_count}")
