try:
    money = float(input("Please enter the amount of money you have: "))
    apple = float(
        input("Please enter the price of an apple that you would like to buy: "))

    if(money < 0 or apple < 0):
        print("Error. Less than 0 inputs are invalid.")
    else:
        max_apple = str(int(money//apple))
        change = str(money % apple)

        print("You can buy " + max_apple +
              " apples and your change is " + change + " pesos.")

except ValueError:
    print("Invalid input. Please input a number.")