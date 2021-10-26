name = input("Please enter you name: ")
age = input("Please enter your age: ")
address = input("Please enter your address: ")

if(name == "" or age == "" or address == ""):
    print("\nEmpty input is invalid.")
else:
    try:
        age_int = int(age)

        if(age_int < 0):
            print("\nInvalid age. Less than 0 inputs are not accepted.")
        else:
            print("\nHi, my name is " + name + ". I am " + age +
                " years old and I live in " + address + ".")

    except ValueError:
        print("\nError. Only whole numbers are accepted.")
