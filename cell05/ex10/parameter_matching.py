import sys

def main():
  
    if len(sys.argv) != 2:
        print("none")
        return

    para = sys.argv[1]

    w = input("What was the parameter? ")

    if w == para:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()
