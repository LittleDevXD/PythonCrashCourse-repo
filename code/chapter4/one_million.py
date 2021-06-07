# List comprehension
one_million = [i for i in range(1, 1_000_001)]

"""
for one in one_million:
    print(one)
"""

print(min(one_million))
print(max(one_million))
print(sum(one_million))

print(f"The first three items in the list are: {one_million[0: 3]}")
print(f"The middle three items in the list are: {one_million[100:103]}")
print(f"The last three items in the list are: {one_million[-3:]}")