import re

content = "Space is a three-dimensional continuum containing positions and directions.[1] In classical physics, physical space is often conceived in three linear dimensions. Modern physicists usually consider it, with time, to be part of a boundless four-dimensional continuum known as spacetime. The concept of space is considered to be of fundamental importance to an understanding of the physical universe. However, disagreement continues between philosophers over whether it is itself an entity, a relationship between entities, or part of a conceptual framework."



"""Normal Search"""
# pattern1 = re.search("^Space.*framework.$", content)

# print(pattern1, "Pattern1")

# if pattern1 == None:

#     print("No match found")

# else:

#     print("Match found")


"""Findall"""

# pattern2 = re.findall("space", content)

# print(pattern2, "pattern2")

# if len(pattern2) > 0:

#     if len(pattern2) == 1:

#         print("1 match found")

#     else:

#         print(f"{len(pattern2)} matches found")

# else:

#     print("No match found")

"""Split"""

# pattern3 = re.split("\s", content)
# pattern3 = re.split("\s", content, 2)

# print(pattern3)

"""Replace Words"""

# pattern4 = re.sub("space", "eternal_space", content)

# print(pattern4)