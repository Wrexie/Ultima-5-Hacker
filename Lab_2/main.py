
def editFile(new_val, offset, filename):
    with open(filename, 'r+b') as f:
        f.seek(offset)
        f.write(bytes([new_val]))
        f.close()

def main():
    filename = "ULTIMA_5\SAVED.GAM"
    choice = 0

    # Main Menu
    while True:
        try:
            choice = int(input("Ultima 5 - Game Hacker\nWhat would you like to modify?\n"
                "1.Edit stats for player\n2.Edit stats for companions\n3.Edit items\n4.Exit\n"))
        except ValueError:
            print("Please enter a valid menu selection.\n")
        else:
            if choice < 1 or choice > 4:
                print("Please make sure you are entering a valid menu entry.\n")

        # Edit stats for player
        if choice == 1:
            while True:
                try:
                    sub_choice = int(input("What stat would you like to modify?\n1.Str\n2.Int\n3.Dex\n"
                                    "4.HP\n5.Max HP\n6.Exp\n7.Gold\n0.Max ALL stats\n"))
                    if isinstance(sub_choice, int) == True and (sub_choice < 8 and sub_choice >= 0):
                        break
                except ValueError:
                    print("Please enter a valid menu selection.\n")
                else:
                    if sub_choice < 0 or sub_choice > 7:
                        print("Please make sure you are entering a valid menu entry.\n")

            # Str
            if sub_choice == 1:
                offset = 0x0E
                while True:
                    try:
                        stat = int(input("Enter a number between 0 and 99:\n"))
                        if isinstance(stat, int) == True and (stat < 100 and stat >= 0):
                            break
                    except ValueError:
                        print("Please enter a valid integer value.\n")
                    else:
                        if stat < 0 or stat > 99:
                            print("Please make sure you are entering a value between 0 and 99.\n")

                editFile(stat, offset, filename)

            # Int
            elif sub_choice == 2:
                offset = 0x10
                while True:
                    try:
                        stat = int(input("Enter a number between 0 and 99:\n"))
                        if isinstance(stat, int) == True and (stat < 100 and stat >= 0):
                            break
                    except ValueError:
                        print("Please enter a valid integer value.\n")
                    else:
                        if stat < 0 or stat > 99:
                            print("Please make sure you are entering a value between 0 and 99.\n")

                editFile(stat, offset, filename)

            # Dex
            elif sub_choice == 3:
                offset = 0x0F
                while True:
                    try:
                        stat = int(input("Enter a number between 0 and 99:\n"))
                        if isinstance(stat, int) == True and (stat < 100 and stat >= 0):
                            break
                    except ValueError:
                        print("Please enter a valid integer value.\n")
                    else:
                        if stat < 0 or stat > 99:
                            print("Please make sure you are entering a value between 0 and 99.\n")

                editFile(stat, offset, filename)

            # HP
            elif sub_choice == 4:
                offset1 = 0x12
                offset2 = 0x13
                while True:
                    try:
                        stat = int(input("Enter a number between 0 and 999:\n"))
                        if isinstance(stat, int) == True and (stat < 1000 and stat >= 0):
                            break
                    except ValueError:
                        print("Please enter a valid integer value.\n")
                    else:
                        if stat < 0 or stat > 999:
                            print("Please make sure you are entering a value between 0 and 999.\n")

                low, high = divmod(stat, 0x100)
                editFile(high, offset1, filename)
                editFile(low, offset2, filename)

            # Max HP
            elif sub_choice == 5:
                offset1 = 0x14
                offset2 = 0x15
                while True:
                    try:
                        stat = int(input("Enter a number between 0 and 999:\n"))
                        if isinstance(stat, int) == True and (stat < 1000 and stat >= 0):
                            break
                    except ValueError:
                        print("Please enter a valid integer value.\n")
                    else:
                        if stat < 0 or stat > 999:
                            print("Please make sure you are entering a value between 0 and 999.\n")

                low, high = divmod(stat, 0x100)
                editFile(high, offset1, filename)
                editFile(low, offset2, filename)

            # Exp.
            elif sub_choice == 6:
                offset1 = 0x16
                offset2 = 0x17
                while True:
                    try:
                        stat = int(input("Enter a number between 0 and 9999:\n"))
                        if isinstance(stat, int) == True and (stat < 10000 and stat >= 0):
                            break
                    except ValueError:
                        print("Please enter a valid integer value.\n")
                    else:
                        if stat < 0 or stat > 9999:
                            print("Please make sure you are entering a value between 0 and 9999.\n")

                low, high = divmod(stat, 0x100)
                editFile(high, offset1, filename)
                editFile(low, offset2, filename)

            # Gold
            elif sub_choice == 7:
                offset1 = 0x204
                offset2 = 0x205
                while True:
                    try:
                        stat = int(input("Enter a number between 0 and 9999:\n"))
                        if isinstance(stat, int) == True and (stat < 10000 and stat >= 0):
                            break
                    except ValueError:
                        print("Please enter a valid integer value.\n")
                    else:
                        if stat < 0 or stat > 9999:
                            print("Please make sure you are entering a value between 0 and 9999.\n")

                low, high = divmod(stat, 0x100)
                editFile(high, offset1, filename)
                editFile(low, offset2, filename)

            elif sub_choice == 0:
                # str
                editFile(99, 0x0E, filename)
                # int
                editFile(99, 0x10, filename)
                # dex
                editFile(99, 0x0F, filename)
                # hp
                low, high = divmod(999, 0x100)
                editFile(high, 0x12, filename)
                editFile(low, 0x13, filename)
                # max hp
                low, high = divmod(999, 0x100)
                editFile(high, 0x14, filename)
                editFile(low, 0x15, filename)
                # exp
                low, high = divmod(9999, 0x100)
                editFile(high, 0x16, filename)
                editFile(low, 0x17, filename)
                # gold
                low, high = divmod(9999, 0x100)
                editFile(high, 0x204, filename)
                editFile(low, 0x205, filename)


        elif choice == 2:
            choice = int(input("What companion would you like to edit stats for?\n"
                               "1.Shamino\n2.Iolo\n3.Gwenno\n4.Julia\n5.Toshi\n6.Jaana\n"
                               "7.Mariah\n8.Katrina\n9.Geoffrey\n10.Maxwell\n11.Sentri\n"
                               "12.Dupre\n13.Johne\n14.Gorn\n15.Saduj\n0.Max ALL Companions\n"))

            stat_choice = int(input("What stat would you like to modify?\n1.Str\n2.Int\n3.Dex\n"
                               "4.HP\n5.Max HP\n6.Exp\n7.Gold\n0.Max ALL stats\n"))

        elif choice == 3:
            choice = int(input("What item would you like to edit?\n1.Keys\n2.Skull Keys\n"
                               "3.Gems\n4.Black Badge\n5.Magic Carpets\n6.Magic Axes\n"))

        elif choice == 4:
            break

    # file = open("Ultima_5\SAVED.GAM", "wb")
    # file.write(data_arr)


main()