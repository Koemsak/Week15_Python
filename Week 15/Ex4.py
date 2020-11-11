word = input()
charDictionary = {}
for char in word:
    if char != " ":
        if char in charDictionary:
            charDictionary[char] += 1
        else:
            charDictionary[char] = 1
print(charDictionary)