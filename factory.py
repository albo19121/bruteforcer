file_name = input("Enter the name you want to give to document: ")
file = open(f'/root/{file_name}.txt', 'a')
info = (input("ENTER INFORMATION (separate words and names by ','): "))
keywords = info.split(',')
ask_sym = input("Enter symbols you want to add (separate symbols by ',') or type d for default: ").lower()
if ask_sym == 'd':
    symbols = ('-', '!', ',', '?', ';', '§', '*', '#', '@', '°', '^', '"', '/', '>', '<', '.', "'", '_')
else:
    symbols = ask_sym.split(',')
name = ''
addition = ''
added_num = ''
count = 0
for word in keywords:
    name = word
    for number in range(0, 99000):
        added_num = number
        product = f"{name}{added_num}\n"
        cap_prod = f"{name.capitalize()}{added_num}\n"
        product1 = f"{added_num}{name}\n"
        cap_prod1 = f"{added_num}{name.capitalize()}\n"
        file.write(product)
        count += 1
        print(count)
        file.write(cap_prod1)
        count += 1
        print(count)
        file.write(cap_prod)
        count += 1
        print(count)
        file.write(product1)
        count += 1
        print(count)
        for symbol in symbols:
            product2 = f"{name}{added_num}{symbol}\n"
            cap_product2 = f"{name.capitalize()}{added_num}{symbol}\n"
            product3 = f"{symbol}{name}{added_num}\n"
            cap_product3 = f"{symbol}{name.capitalize()}{added_num}\n"
            product4 = f"{symbol}{added_num}{name}\n"
            cap_product4 = f"{symbol}{added_num}{name.capitalize()}\n"

            product5 = f"{added_num}{name}{symbol}\n"
            cap_product5 = f"{added_num}{name.capitalize()}{symbol}\n"
            product6 = f"{added_num}{symbol}{name}\n"
            cap_product6 = f"{added_num}{symbol}{name.capitalize()}\n"
            product7 = f"{name}{symbol}{added_num}\n"
            cap_product7 = f"{name.capitalize()}{symbol}{added_num}\n"
            file.write(product2)
            count += 1
            print(count)
            file.write(cap_product2)
            count += 1
            print(count)
            file.write(product3)
            count += 1
            print(count)
            file.write(cap_product3)
            count += 1
            print(count)
            file.write(product4)
            count += 1
            print(count)
            file.write(cap_product4)
            count += 1
            print(count)
            file.write(product5)
            count += 1
            print(count)
            file.write(cap_product5)
            count += 1
            print(count)
            file.write(product6)
            count += 1
            print(count)
            file.write(cap_product6)
            count += 1
            print(count)
            file.write(product7)
            count += 1
            print(count)
            file.write(cap_product7)
            count += 1
            print(count)
