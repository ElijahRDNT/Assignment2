apple_price = 20
orange_price = 25

try:
    apples = int(input("Please enter the number of apples you want to buy: "))
    oranges = int(input("Please enter the number of oranges you want to buy: "))

    if(apples < 0 or oranges < 0):
        print("Invalid order. Less than 0 inputs are not accepted.")
    else:
        total_amount = str((apples*apple_price) +
                           (oranges*orange_price))
        print("The total amount is " + total_amount + ".")

except ValueError:
    print("Error. Please enter whole numbers.")