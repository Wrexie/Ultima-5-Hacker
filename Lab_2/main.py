'''
CECS-378: Lab #2
By: Andrew Baltazar
ID: 016348512
Due: 11/13/2020
'''


def edit_file(new_val, offset, filename):
    with open(filename, 'r+b') as f:
        f.seek(offset)
        f.write(bytes([new_val]))
        f.close()


def main():
    # Use appropriate file directory and file name
    filename = "ULTIMA_5\SAVED.GAM"
    choice = 0
    player_stats_and_items = {
        1 : 0x0E, 2 : 0x10, 3 : 0x0F, 4 : [0x12, 0x13], 5 : [0x14, 0x15], 6 : [0x16, 0x17],
        7 : [0x204, 0x205], 8 : 0x206, 9 : 0x20B, 10 : 0x207, 11 : 0x218, 12 : 0x20A, 13 : 0x240
    }
    companion_stats = {
        # Shamino
        1 : { 1 : 0x2E, 2 : 0x30, 3 : 0x2F, 4 : [0x32, 0x33], 5 : [0x34, 0x35], 6 : [0x36, 0x37] },
        # Iolo
        2 : { 1 : 0x4E, 2 : 0x50, 3 : 0x4F, 4 : [0x52, 0x53], 5 : [0x54, 0x55], 6 : [0x56, 0x57] },
        # Mariah
        3 : { 1 : 0x6E, 2 : 0x70, 3 : 0x6F, 4 : [0x72, 0x73], 5 : [0x74, 0x75], 6 : [0x76, 0x77] },
        # Geoffrey
        4 : { 1 : 0x8E, 2 : 0x90, 3 : 0x8F, 4 : [0x92, 0x93], 5 : [0x94, 0x95], 6 : [0x96, 0x97] },
        # Jaana
        5 : { 1 : 0xAE, 2 : 0xB0, 3 : 0xAF, 4 : [0xB2, 0xB3], 5 : [0xB4, 0xB5], 6 : [0xB6, 0xB7] },
        # Julia
        6 : { 1 : 0xCE, 2 : 0xD0, 3 : 0xCF, 4 : [0xD2, 0xD3], 5 : [0xD4, 0xD5], 6 : [0xD6, 0xD7] },
        # Dupre
        7 : { 1 : 0xEE, 2 : 0xF0, 3 : 0xEF, 4 : [0xF2, 0xF3], 5 : [0xF4, 0xF5], 6 : [0xF6, 0xF7] },
        # Katrina
        8 : { 1 : 0x10E, 2 : 0x110, 3 : 0x10F, 4 : [0x112, 0x113], 5 : [0x114, 0x115], 6 : [0x116, 0x117] },
        # Sentri
        9 : { 1 : 0x12E, 2 : 0x130, 3 : 0x12F, 4 : [0x132, 0x133], 5 : [0x134, 0x135], 6 : [0x136, 0x137] },
        # Gwenno
        10 : { 1 : 0x14E, 2 : 0x150, 3 : 0x14F, 4 : [0x152, 0x153], 5 : [0x154, 0x155], 6 : [0x156, 0x157] },
        # Johne
        11 : { 1 : 0x16E, 2 : 0x170, 3 : 0x16F, 4 : [0x172, 0x173], 5 : [0x174, 0x175], 6 : [0x176, 0x177] },
        # Gorn
        12 : { 1 : 0x18E, 2 : 0x190, 3 : 0x18F, 4 : [0x192, 0x193], 5 : [0x194, 0x195], 6 : [0x196, 0x197] },
        # Maxwell
        13 : { 1 : 0x1AE, 2 : 0x1B0, 3 : 0x1AF, 4 : [0x1B2, 0x1B3], 5 : [0x1B4, 0x1B5], 6 : [0x1B6, 0x1B7] },
        # Toshi
        14 : { 1 : 0x1CE, 2 : 0x1D0, 3 : 0x1CF, 4 : [0x1D2, 0x1D3], 5 : [0x1D4, 0x1D5], 6 : [0x1D6, 0x1D7] },
        # Saduj
        15 : { 1 : 0x1EE, 2 : 0x1F0, 3 : 0x1EF, 4 : [0x1F2, 0x1F3], 5 : [0x1F4, 0x1F5], 6 : [0x1F6, 0x1F7] }
    }

    # Main Menu
    while True:
        try:
            choice = int(input("Ultima 5 - Game Hacker\nWhat would you like to modify?\n"
                               "1.Edit stats and items for player\n2.Edit stats for companions\n3.Exit\n"))
        except ValueError:
            print("Please enter a valid menu selection.\n")
        else:
            if choice < 1 or choice > 3:
                print("Please make sure you are entering a valid menu entry.\n")

        # Edit stats and items for player
        if choice == 1:
            while True:
                try:
                    sub_choice = int(input("What stat would you like to modify?\n1.Str\n2.Int\n3.Dex\n"
                                           "4.HP\n5.Max HP\n6.Exp\n7.Gold\n8.Keys\n9.Skull Keys\n10.Gems\n"
                                           "11.Black Badge\n12.Magic Carpet\n13.Magic Axes\n0.Max ALL stats\n"))
                    if isinstance(sub_choice, int) == True and (sub_choice < 14 and sub_choice >= 0):
                        break
                except ValueError:
                    print("Please enter a valid menu selection.\n")
                else:
                    if sub_choice < 0 or sub_choice > 13:
                        print("Please make sure you are entering a valid menu entry.\n")

            # Str, int and dex
            if sub_choice == 1 or sub_choice == 2 or sub_choice == 3:
                offset = player_stats_and_items[sub_choice]
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

                edit_file(stat, offset, filename)

            # HP and Max HP
            elif sub_choice == 4 or sub_choice == 5:
                offset1 = player_stats_and_items[sub_choice][0]
                offset2 = player_stats_and_items[sub_choice][1]
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
                edit_file(high, offset1, filename)
                edit_file(low, offset2, filename)

            # Exp. and Gold
            elif sub_choice == 6 or sub_choice == 7:
                offset1 = player_stats_and_items[sub_choice][0]
                offset2 = player_stats_and_items[sub_choice][1]
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
                edit_file(high, offset1, filename)
                edit_file(low, offset2, filename)

            # Keys, skull keys, gems, black badge, magic carpet and magic axes
            elif sub_choice == 8 or sub_choice == 9 or sub_choice == 10 or sub_choice == 11 or sub_choice == 12\
                    or sub_choice == 13:
                offset = player_stats_and_items[sub_choice]
                while True:
                    try:
                        count = int(input("Enter a number between 0 and 100:\n"))
                        if isinstance(count, int) == True and (count < 101 and count >= 0):
                            break
                    except ValueError:
                        print("Please enter a valid integer value.\n")
                    else:
                        if count < 0 or count > 100:
                            print("Please make sure you are entering a value between 0 and 100.\n")

                edit_file(count, offset, filename)

            # Max all stats and items for player
            elif sub_choice == 0:
                # str
                edit_file(99, player_stats_and_items[1], filename)
                # int
                edit_file(99, player_stats_and_items[2], filename)
                # dex
                edit_file(99, player_stats_and_items[3], filename)
                # hp
                low, high = divmod(999, 0x100)
                edit_file(high, player_stats_and_items[4][0], filename)
                edit_file(low, player_stats_and_items[4][1], filename)
                # max hp
                low, high = divmod(999, 0x100)
                edit_file(high, player_stats_and_items[5][0], filename)
                edit_file(low, player_stats_and_items[5][1], filename)
                # exp
                low, high = divmod(9999, 0x100)
                edit_file(high, player_stats_and_items[6][0], filename)
                edit_file(low, player_stats_and_items[6][1], filename)
                # gold
                low, high = divmod(9999, 0x100)
                edit_file(high, player_stats_and_items[7][0], filename)
                edit_file(low, player_stats_and_items[7][1], filename)

                # keys
                edit_file(100, player_stats_and_items[8], filename)
                # skull keys
                edit_file(100, player_stats_and_items[9], filename)
                # gems
                edit_file(100, player_stats_and_items[10], filename)
                # black badge
                edit_file(100, player_stats_and_items[11], filename)
                # magic carpet
                edit_file(100, player_stats_and_items[12], filename)
                # magic axes
                edit_file(100, player_stats_and_items[13], filename)

        elif choice == 2:
            while True:
                try:
                    sub_choice = int(input("What companion would you like to modify stats for?\n"
                                           "1.Shamino\n2.Iolo\n3.Mariah\n4.Geoffrey\n5.Jaana\n6.Julia\n"
                                           "7.Dupre\n8.Katrina\n9.Sentri\n10.Gwenno\n11.Johne\n"
                                           "12.Gorn\n13.Maxwell\n14.Toshi\n15.Saduj\n"))
                    if isinstance(sub_choice, int) == True and (sub_choice < 16 and sub_choice > 0):
                        break
                except ValueError:
                    print("Please enter a valid menu selection.\n")
                else:
                    if sub_choice < 1 or sub_choice > 15:
                        print("Please make sure you are entering a valid menu selection.\n")

            while True:
                try:
                    stat_choice = int(input("What stat would you like to modify?\n1.Str\n2.Int\n3.Dex\n"
                                             "4.HP\n5.Max HP\n6.Exp\n0.Max ALL stats\n"))
                    if isinstance(stat_choice, int) == True and (stat_choice < 7 and stat_choice >= 0):
                        break
                except ValueError:
                    print("Please enter a valid menu selection.\n")
                else:
                    if stat_choice < 0 or stat_choice > 6:
                        print("Please make sure you are entering a valid menu selection.\n")

            if stat_choice == 4 or stat_choice == 5:
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


                offset1 = companion_stats[sub_choice][stat_choice][0]
                offset2 = companion_stats[sub_choice][stat_choice][1]
                low, high = divmod(stat, 0x100)
                edit_file(high, offset1, filename)
                edit_file(low, offset2, filename)

            elif stat_choice == 6:
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

                offset1 = companion_stats[sub_choice][stat_choice][0]
                offset2 = companion_stats[sub_choice][stat_choice][1]
                low, high = divmod(stat, 0x100)
                edit_file(high, offset1, filename)
                edit_file(low, offset2, filename)

            elif stat_choice == 0:
                # str
                edit_file(99, companion_stats[sub_choice][1], filename)
                # int
                edit_file(99, companion_stats[sub_choice][2], filename)
                # dex
                edit_file(99, companion_stats[sub_choice][3], filename)
                # hp
                low, high = divmod(999, 0x100)
                edit_file(high, companion_stats[sub_choice][4][0], filename)
                edit_file(low, companion_stats[sub_choice][4][1], filename)
                # max hp
                low, high = divmod(999, 0x100)
                edit_file(high, companion_stats[sub_choice][5][0], filename)
                edit_file(low, companion_stats[sub_choice][5][1], filename)
                # exp
                low, high = divmod(9999, 0x100)
                edit_file(high, companion_stats[sub_choice][6][0], filename)
                edit_file(low, companion_stats[sub_choice][6][1], filename)

            else:
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

                offset = companion_stats[sub_choice][stat_choice]
                edit_file(stat, offset, filename)

        elif choice == 3:
            break


main()
