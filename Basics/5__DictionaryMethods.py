laptop = {
    "brand": "Dell",
    "model": "Inspiron 3542",
    "launched_year": 2013
}


# Accessing

laptop['brand']


# Updating

laptop['model'] = "Dell Inspiron 3542"


# View Keys

laptop.keys()


# View values

laptop.values()


# Add new key value pair

laptop['default_ram'] = "4GB"


# Deleting last key value pair

laptop.popitem()


# Deleting selected key value pair

laptop.pop("brand")


# Remove all elements from dictionary

laptop.clear()