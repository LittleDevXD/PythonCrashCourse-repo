languages = ["English", "Japanese", "Portugese", "German", "Korean"]

# Append
languages.append("Mongolia")
print(languages)

# Pop
print(languages.pop())

# Insert 
languages.insert(1, "Arbic")
print(languages)

# Remove
languages.remove("Arbic")
print(languages)

# Delete
del languages[-1]
print(languages)

# Temporary sort
print(sorted(languages))

# Temporary sort with reverse order
print(sorted(languages, reverse=True))

# Permanent sort
languages.sort()
print(languages)

# Permanent reverse sort
languages.sort(reverse=True)
print(languages)

# Reversing the list
languages.reverse()
print(languages)

