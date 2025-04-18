def select_coffee_type():
    selection = input("Seçiminizi daxil edin (1-3): ")
    
    if selection == "1":
        return "latte"
    elif selection == "2":
        return "cappuccino"
    elif selection == "3":
        return "espresso"
    else:
        return "espresso"


def select_size():
    selection = input("Seçiminizi daxil edin (1-2): ")
    
    if selection == "1":
        return "single"
    elif selection == "2":
        return "double"
    else:
        return "single"


def brew_coffee(coffee_type, size):
    if size == "double":
        qram = 50
    else:
        qram = 25
    
    if coffee_type == "latte" or coffee_type == "cappuccino":
        milk = True
    else:
        milk = False
    
    print(f"\nKofe Hazirlanir: {coffee_type.capitalize()}")
    print(f"Seçdiyiniz ölçü: {size.capitalize()}")
    print(f"İstifadə olunan miqdar: {qram} qram")
    
    if milk:
        print("Süd əlavə olunur.")
    else:
        print("Süd əlavə edilmir.")
    
    print("\nKofe hazirdir.Növbəti sifarişinizi gözləyirik.")


def main():
    coffee_type = select_coffee_type()
    size = select_size()
    brew_coffee(coffee_type, size)


main()
