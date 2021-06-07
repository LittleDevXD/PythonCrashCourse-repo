places = ["Silicon Valley", "Maldives", "Bagan", "Tokyo", "London"]

print(f"Original Array: {places}")

print(f"Temporarily sorted: {sorted(places)}")

print(f"Back to original array: {places}")

print(f"Sorted again: {sorted(places, reverse=True)}")

print(f"Back to original: {places}")

places.reverse()
print(f"Reversing the array: {places}")

places.sort()
print(f"Permanently sorted: {places}")

places.sort(reverse=True)
print(f"Reversing the sort: {places}")



