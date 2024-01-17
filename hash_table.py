#in python, 'dict' is a hash table

#create an empty hash table
hash_table = {}

#add a key-value pair to the hash table
hash_table["one"] = 1
hash_table["two"] = 2
hash_table["three"] = 3
hash_table["four"] = 4
hash_table["five"] = 5
hash_table["danil"] = "kryuchkov"

#access a key-value pair in the hash table
print(hash_table["danil"])

#access a key-value pair in the hash table
print(hash_table["one"])

#remove a key-value pair from the hash table
del hash_table["one"]

#get a size/length of a hash table
print(len(hash_table))

#check if a key is in the hash table
print("one" in hash_table)
print("danil" in hash_table)

#iterate over the keys in the hash table
for key in hash_table:
    print(key)

#iterate over the values in the hash table
for key in hash_table:
    print(hash_table[key])

#iterate over the key-value pairs in the hash table
for key in hash_table:
    print(key, hash_table[key])

#Counter() - a subclass of dict for counting hashable objects

#example 1
from collections import Counter

word = "remember"
letter_counts = Counter(word)
print(f"Letter counts for '{word}': {letter_counts}")
print(f"how many 'e' in '{word}': {letter_counts['e']}")

print(f"most common letter in '{word}': {letter_counts.most_common(1)}")
print(f"unique letters in '{word}': {len(letter_counts)}")

