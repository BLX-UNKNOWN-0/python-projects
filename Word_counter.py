# BLX-UNKNOWN-0
# PROJECT 7 // WORD COUNTER


def count_text(text):
    words = text.split()
    chars = len(text)
    chars_no_space = len(text.replace(" ", ""))
    sentences = text.count(".") + text.count("!") + text.count("?")
    
    print(f"\n... Results ...")
    print(f"Words      : {len(words)}")
    print(f"Characters : {chars}")
    print(f"No spaces  : {chars_no_space}")
    print(f"Sentences  : {sentences}")

def count_file(filename):
    try:
        with open(filename, "r") as f:
            text = f.read()
        print(f"File '{filename}' loaded.")
        count_text(text)
    except FileNotFoundError:
        print("File not found. Check the filename.")

def menu():
    print("...WORD COUNTER...")
    print(" 1 = Type text")
    print(" 2 = Load a .txt file")
    print(" 0 = Quit")

    while True:
        choice = input("\nChoose: ").strip()

        if choice == "1":
            text = input("Enter your text: ")
            count_text(text)

        elif choice == "2":
            filename = input("Enter filename (e.g. notes.txt): ").strip()
            count_file(filename)

        elif choice == "0":
            print("Bye!, Have a nice day!")
            break

        else:
            print("Invalid. Enter 1, 2 or 0.")

menu()