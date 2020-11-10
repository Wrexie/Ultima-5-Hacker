
def editFile(new_val, offset, filename):
    with open(filename, 'r+b') as f:
        f.seek(offset)
        f.write(bytes([new_val]))
        f.close()


def main():
    # TODO: Implement map for storing offsets?
    while True:
        choice = int(input("Ultima 5 - Game Hacker\nWhat would you like to modify?\n"
              "1.Edit stats for player\n2.Edit stats for companions\n3.Edit items\n"))

        if choice == 1:
            filename = "ULTIMA_5\SAVED.GAM"
            choice = int(input("What stat would you like to modify?\n1.Str\n2.Int\n3.Dex\n"
                               "4.HP\n5.Max HP\n6.Exp\n7.Gold\n0.Max ALL stats\n"))

            if choice == 1:
                stat = int(input("Enter a number between 0 and 99:\n"))
                offset = 0x0E

            elif choice == 2:
                stat = int(input("Enter a number between 0 and 99:\n"))
                offset = 0x10

            elif choice == 3:
                stat = int(input("Enter a number between 0 and 99:\n"))
                offset = 0x0F

            elif choice == 4:
                stat = int(input("Enter a number between 0 and 999:\n"))
                offset = 0x12

            elif choice == 7:
                stat = int(input("Enter a number between 0 and 9999:\n"))
                offset = 0x204

            editFile(stat, offset, filename)

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

    # file = open("Ultima_5\SAVED.GAM", "wb")
    # file.write(data_arr)


main()