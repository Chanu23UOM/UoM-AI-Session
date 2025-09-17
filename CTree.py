#Get input
height = int(input("Enter the height of the Christmas tree: "))

#the tree
for i in range(height):
    
    spaces = " " * (height - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
