d = {} # empty dictionary
print(d)

eng_to_spa = {"one": "uno", "two": "dos", "three": "tres" }
print(eng_to_spa)
print(eng_to_spa["one"]) # Prints one single translation
eng_to_spa["LeBron"] = "Árbol" # It's arbol!!!
print(eng_to_spa["LeBron"])
eng_to_spa.update({"yes": "si", "no": "no"})
print(eng_to_spa) # Overwritten the first dictionary
# How to delete from the dictionary?
del eng_to_spa["yes"]
print(eng_to_spa)

#Iteration over dictionary
for key in eng_to_spa: # if put .keys[] would also work
    print(f"{eng_to_spa[key]} means {key}")

print(dir(eng_to_spa))
# Useful ones:
#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'.
# eng_to_spa.clear will clear the dictionary
# Creates a copy of the dictionary
eng_to_spa2 = eng_to_spa.copy()
eng_to_spa.clear()
print(eng_to_spa2)
# Fromkeys substitutes translation with a single word
new_d = eng_to_spa2.fromkeys(eng_to_spa2, "YES")
print(new_d)
# Get is one of the most useful
print(f"car in Spanish is {eng_to_spa2.get('car', 'unknown')}")
#Items
print(list(eng_to_spa2.items())) #separates them in different items by key and value
#Delete the word given from the dictionary (POP)
print(eng_to_spa2.pop('one'))
print(eng_to_spa2.popitem()) #Pop in the reverse order that you have added
eng_to_spa2.setdefault('red', 'rojo') #Adding the key and the value
print(eng_to_spa2)