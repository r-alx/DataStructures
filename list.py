card = ["One Piece","Skibidi","Mini"]

card.append("Naruto")
card.append("Mini")

copy = card.copy()
print(copy.count("Naruto"))

print(card)

print(dir(card))

card.extend(["no","yes","???"])


print(card)

print("-------------------Älex presentation below--------------------------")
print(card)
print(card.index("no"))

card.insert(5,"temp")
print(card)