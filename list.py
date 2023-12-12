"""Ïmplementation of the list methods"""

# our list sample
card = ["One Piece","Skibidi","Mini"]

#Append:Put item in the list
card.append("Naruto")
#Copy: make a copy of the list.
copy = card.copy()
#Extend: put the items to the original list by unpacking the collection.
card.extend(["no","yes","???"])
#Index:Finds the index of the specified item.
print(card.index("no"))
#Insert: Put the items on the specified index.
card.insert(5,"temp")
#Pop:remove the item on the specified index.
card.pop(2)
#Remove:remove the item from the list
card.remove("temp")
#Reverse:reverse the item from the list
card.reverse()
#Sort:sort the item in a descending or ascending  
n_list = [5,2,6,3,4,1,7,0,9,8]
n_list.sort(reverse=True)
print(n_list)
# help(n_list.sort)