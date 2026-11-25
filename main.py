import converter

fileName = "Image path here"

print(r"    ____")
print(r"   /  _/___ ___  ____ _____ ____")
print(r"   / // __ `__ \/ __ `/ __ `/ _ \ ")
print(r" _/ // / / / / / /_/ / /_/ /  __/")
print(r"/___/_/ /_/ /_/\__,_/\__, /\___/")
print(r"                    /____/")
print(r"  ______                                      __        __")
print(r" /_  __/________ _____  _________ ___  __  __/ /_____ _/ /_____  _____")
print(r"  / / / ___/ __ `/ __ \/ ___/ __ `__ \/ / / / __/ __ `/ __/ __ \/ ___/")
print(r" / / / /  / /_/ / / / (__  ) / / / / / /_/ / /_/ /_/ / /_/ /_/ / /")
print(r"/_/ /_/   \__,_/_/ /_/____/_/ /_/ /_/\__,_/\__/\__,_/\__/\____/_/")

while True:
    print("Choose character set:")
    print("1) Detailed (70 chars)")
    print("2) Simple (10 chars)")
    answer= input("Select what set of characters to use (1) or (2): ")
    answer = answer.strip()
    if answer in ("1", "2"):
        moreLevels = answer == "1" 
        break
    else:
        print("Incorrect input detected, we will ask again")
while True:
    print("More features will be added to please our image manipulator overlords")
    print("1) ASCII")
    print("2) SEND TO .TXT")
    print("3) COLOR")
    print("4) EXIT")

    choice = input("Enter a choice: ")
    choice= choice.strip()

    if (choice == "1"):
        ascii_art = converter.image_to_ascii(fileName, moreLevels=moreLevels)
        for fila in ascii_art:
            print(fila)

    elif (choice == "2"):
        ascii_art = converter.image_to_ascii(fileName, moreLevels=moreLevels)
        with open("output.txt", "w") as f:
            for fila in ascii_art:
                print(fila, file=f)

        ascii_color = converter.image_to_ascii(fileName, moreLevels=moreLevels, color=True)
        with open("output_color.txt", "w") as f:
            for fila in ascii_color:
                print(fila, file=f)

        print("output.txt and output_color.txt have been created")

    elif (choice == "3"):
        ascii_art = converter.image_to_ascii(fileName, moreLevels=moreLevels, color=True)
        for fila in ascii_art:
            print(fila)
    elif (choice == "4"):
        print("Thx for using the ASCII converter see ya :)")
        break
    else:
        print("Invalid option pls try again <3")