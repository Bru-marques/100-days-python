# Treasure Map


row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column_number = int(position[0]) - 1
row_number = int(position[1]) - 1

map[row_number][column_number] = "x"


print(f"{row1}\n{row2}\n{row3}")