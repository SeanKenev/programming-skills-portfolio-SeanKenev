usb1 = int(input("Amount of money: "))
usb2 = int(input("Price of USB sticks: "))
 
result = usb1 / usb2
print("The girl can buy {2} USB sticks" .format(usb1, usb2, result)) 

b1 = int(input("Amount of USB sticks that can be bought: "))
b2 = int(input("Price of USB sticks: "))

price = b2 * b1 
print("The change is {2}" .format(b1, b2, price))
