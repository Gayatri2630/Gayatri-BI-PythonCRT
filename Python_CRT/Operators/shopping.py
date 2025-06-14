'''
Write a python program 
i)Display the list of items in sorted and to take input from the user and add items to cart and view 
the cart items
   update the quantity or the item  present in the cart
   generate a bill including item names,item quantity,price and if the final amount is greater than 1000
   then the user will get 10% discount 

ii)If the user purchases any item more than 10 kg's reduce the amount of 1 kg from that particular items price.

iii)If the  user purchases any particular items add buy 1 and get 1 offer

iv)Add 25% gst to overall bill and print the bill.
v)
'''
items=['Carrot','Orange','Rice','Dal']
bogo_items=['Milk','Chocolate','Biscuits']
price=(20,100,90,40)
print("Grocery Items")
sort_items=sorted(items)
print(sort_items)
i=0
while(i<len(sort_items)):
       word=sort_items[i]
       index=sort_items.index(word)
       print(f"{word}-{price[index]}")
       i+=1
m=int(input("Enter the no.of items needed:"))
j=1
total=0
cart=[]
while(j<=m):
       item=input("Enter the item:")
       if item in items:
              cart.append(item)
              qty=int(input(f"Enter the quantity in(kg/count):"))
              index=cart.index(item)
              item_price=price[index]*qty
              print(f"{item} x {qty}={item_price}")
              total+=item_price
       else:
              print("Item not available in List.")
       j+=1
print("Cart Items")
print(cart)
while True:
      while True:
        print("\nShopping Cart Menu:")
        print("1. Display Available Items")
        print("2. Add Item to Cart")
        print("3. Update Item Quantity in Cart")
        print("4. View Cart")
        print("5. Calculate Bill")
        print("6. Exit")
       choice=input("Enter Choice:")
       if choice=='1':
              item=input("Enter item name to add/update:")
              if item  in items:
                     qty=int(input(f"Enter quantity (in kg/count) for {item}:"))
                     if qty>0:
                            for i in range(len(cart)):
                                   if cart[i][0]==item:
                                          cart[i]=(item,cart[i][1]+qty)
                            cart=cart.append(i)
                            print(f"{item} added/update in cart.")
                     else:
                            print("Quantity must be positive.")
              else:
                     print("Item not available.")
       elif choice=='2':
               print("\nCart Items:")
               print(cart)
       elif choice=='3':
              if not cart:
                     print("Cart is Empty.Exiting.")
                     break
              total=0
              for item in cart:
                     index=items.index(item)
                     rate=price[index]
                     effective_qty=qty
                     if item in bogo_items:
                            effective_qty=qty/2
                            print(f"{item}(Buy 1 Get 1 Free Applied)")
                     if qty>10:
                            effective_qty=-1
                            print(f"{item}(1 kg Free for >10kg)")
                     item_total=effective_qty*rate
                     total+=item_total
                     print(f"\nItems:{item} \n Quantity:{qty}\nPrice:{rate} \nTotal_price{item_total}")
              if total>1000:
                     discount=total*0.10
                     print(f"\n !0% dicscount applied:{discount:.2f}")
                     total-=discount
              gst=total*0.25
              print(f"GST (25%):{gst:.2f}")
              print(f"\n Final Amount to Pay:{total:.2f}")
              print("Thank you for Shopping!")
       else:
              print("In-valid input")




