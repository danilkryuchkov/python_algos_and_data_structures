#python's 'set' data structure is a hash table with only keys and no values

word = "remember"
set_of_letters = set(word)

print(f"set of letters in '{word}': {set_of_letters}")
print(f"is there a letter 'b' in {word}? {'a' in set_of_letters}")
print(f"is there a letter 'e' in {word}? {'e' in set_of_letters}")

#lest add random letters to a set
set_of_letters.add('z')

print(f"set of letters: {set_of_letters}")
print(f"is there a letter 'z' in {word}? {'z' in set_of_letters}")

#lets discard a letter from a set
set_of_letters.discard('m')
print(f"set of letters: {set_of_letters}")

#userful in DFS and BFS on graphs