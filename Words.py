import random

def dictionaryPick(s):
    d = {}
    words = s.split()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def assign_binary_keys(d):
    binary_dict = {}
    for word in d:
        binary_key = format(random.randint(0, 15), '04b')
        binary_dict[binary_key] = (word, d[word])
    return binary_dict

s = ("A well-organized paragraph supports or develops a single controlling idea, "
     "which is expressed in a sentence called the topic sentence. A topic sentence has several important "
     "functions: it substantiates or supports an essay’s thesis statement; it unifies the content of a paragraph "
     "and directs the order of the sentences; and it advises the reader of the subject to be discussed and how the "
     "paragraph will discuss it. Readers generally look to the first few sentences in a paragraph to determine the "
     "subject and perspective of the paragraph. That’s why it’s often best to put the topic sentence at the very beginning "
     "of the paragraph. In some cases, however, it’s more effective to place another sentence before the topic sentence—for "
     "example, a sentence linking the current paragraph to the previous one, or one providing background information.")

# Get the dictionary
word_dict = dictionaryPick(s)

# Assign random 4-digit binary numbers to the keys
binary_word_dict = assign_binary_keys(word_dict)

print(word_dict)

# Print the binary dictionary
print("Binary Key : (Word, Count)\n")
for binary_key, word_info in binary_word_dict.items():
    print(f"{binary_key} : {word_info}")

