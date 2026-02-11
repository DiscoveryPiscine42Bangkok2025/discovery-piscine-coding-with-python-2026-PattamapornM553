import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 9:
        print(f"Table de {i} : ", end="")
        j = 0
        while j <= 9:
            print(f"{i * j}", end=" ")
            j += 1
        print()
        i += 1
