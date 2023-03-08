import sys
names = []
name = input("Name: ")
if name in names:
    print("Found")
    sys.exit(0)
print("Not Found")
sys.exit(1)