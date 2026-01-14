harorat = int(input("Haroratni kiriting (°C): "))

if harorat < -20:
    print("Juda sovuq")

elif harorat < 0:
    print("Sovuq")

elif harorat < 15:
    print("Salqin")

elif harorat < 30:
    print("Iliq")

else:
    print("Issiq")
