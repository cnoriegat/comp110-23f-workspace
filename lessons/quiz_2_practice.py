"""Quiz practice."""

family: dict[int, str] = {1: "Gustavo", 2: "Valeria", 3: "Camila", 4: "Daniela", 5: "Gustavo Jr."}

input: str = "Gustavo"

if input in family.values():
    print(f"{input} is in the Noriega family.")
else:
    print(f"{input} is not in the Noriega family.")

print("Constanza" in family)
family[1] = "Gustavo mayor"
family[5] = "Gustavo menor"
print(family)
    

def mimic(my_words: str) -> str:
    """Given a string, return the same string."""
    return my_words

phrase: str = "Happy Friday"
output: str = mimic(phrase)
print(output)

friends: list [str] = ["Mateo", "Alejadro", "Isabella", "Melanie", "Chiara", "Micaela"]
friends[1] = "Ale"
friends[2] = "Bella"
friends [3] = "Mel"
friends[0] = "Mofla"
friends[len(friends)-1] = "Mica"
friends.append("Elena")
print(len(friends))
print(friends)

for idx in range(len(friends)-1):
    print(friends[idx])

for idx in friends:
    print(idx) # OJO si aca ponemod friends, se imprime toda la lista, no solo el nombre

for elem in friends:
    print(elem)

def contains(haystack: list[int], needle: int) -> bool:
    """Function to find the needle in the haystack."""
    for idx in range(len(haystack)-1):
        if needle == haystack[idx]:
            return True
    return False

print(contains([1, 4, 34, 58, 30, 45], 35))

def contains1(needle: int, haystack: list[int]) -> bool:
    """Function to find needle in haystack."""
    for idx in range(len(haystack)):
        if needle == haystack[idx]:
            return True
    return False

print(contains1(3, [1, 2, 3]))
