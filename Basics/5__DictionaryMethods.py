laptop = {
    "brand": "Dell",
    "model": "Inspiron 3542",
    "launched_year": 2013
}

print(laptop)


# Accessing

print(laptop["brand"])


# Updating

laptop['model'] = "Dell Inspiron 3542"

print(laptop)


# View Keys

print(laptop.keys())


# View values

print(laptop.values())


# Add new key value pair

laptop['default_ram'] = "4GB"

print(laptop)


# Deleting last key value pair

laptop.popitem()

print(laptop)


# Deleting selected key value pair

laptop.pop("brand")

print(laptop)

# Remove all elements from dictionary

laptop.clear()

print(laptop)