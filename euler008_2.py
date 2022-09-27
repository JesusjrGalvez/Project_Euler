# Exploring dictionaries

mydict = {1234: 1000, 2345: 200, 456: 30, 46: 4, 56: 5, 6: 6}

print(mydict)
print(mydict.keys())
print(mydict.values())

print("-----")

max_value = max(mydict.values())
max_key = max(mydict.keys())
key_with_max_value = max(mydict, key=mydict.get)
value_with_max_key = mydict.get(max(mydict.keys()))

print(f"Max value is {max_value}")
print(f"Max key is {max_key}")
print(f"Key with max value is {key_with_max_value}")
print(f"Value with max key is {value_with_max_key}")

tem=mydict.get # This is a method
print(type(tem))

print(mydict.get("hola", 5)) # Will search for key="hola" and if it's not found will return 5