'''
Write a python program 
i)To display a menu of food items(list)
ii) Create a tuple of prices with respect to food items list
iii)read the input from the user for ordering the food including the quantity
       if it exits in the menu --- conform order
       if nor ptint a message
iv)while billing ,read phone no,feedback,read tip amount
v)add 18% gst to the bill and print the bill if bill>0
'''
menu=('manchuria','dragon chicken','panner curry','Biryani')
price=(100,200,170,350)
print("**Menu Card**")
print(menu)
i=1
j=1
total=0
while(i<len(menu)):
       word=menu[i]
       index=menu.index(word)
       print(f"{word}-{price[index]}")
       i+=1
m=int(input("Enter the number of food items you wamt to order:"))
while j<=m:
       food=input("Enter name of food:")
       if food in menu:
              qty=int(input(f"Enter the quantity for {food}:"))
              index=menu.index(food)
              item_price=price[index]*qty
              print(f"{food} x {qty}={item_price}")
              total+=item_price
       else:
              print("Sorry, item is not available in the menu")
       j+=1
print("\n------Billing Information-------")
phone=int(input("Enter your mobile number:"))
feedback=input("Please provide your feedback:")
tip=float(input("Enter the tip amount:"))
gst=total*0.18
final_amount=total+gst+tip
print("\n-----Final Bill Summary-----")
print(f"Phone Number:{phone}")
print(f"Food Bill:{total}")
print(f"GST(18%):{gst}")
print(f"Tip:{tip}")
print(f"Total amount to pay:{final_amount}")
print(f"Feedback:{feedback}")
print("Thank you for your order")