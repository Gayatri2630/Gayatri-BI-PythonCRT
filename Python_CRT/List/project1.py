'''
   Write a Python program to:
   --> Add confirmed guests to a list
   --> Remove a guest who cancels
   --> Check if a friend is on the list
   --> Sort and print the final guest list
'''
Guest_List=[]
while(True):
    print("************Menu************")
    print("1.Add the Guest")
    print("2.Remove the Guest who cancels")
    print("3.Check if a Guest is Attending the party or not")
    print("4.View the Final Guest List")
    print("5.Exit")
    print("-------------------------------------")
    Choice=int(input("Enter your Choice:"))
    if(Choice>=1 and Choice<=5):
        if(Choice==1):
            GuestName=input("Enter the Guest Name:")
            Guest_List.append(GuestName)
            print(f"{GuestName} is Added to Guest List...!")
        elif(Choice==2):
            CancelledGuest=input("Enter the Cancelled Guest Name:")
            if (CancelledGuest in Guest_List):
                Guest_List.remove(CancelledGuest)
                print(f"{CancelledGuest} is Removed from Guest List...!")
            else:
                print(f"{CancelledGuest} is not in  Guest List...!")
        elif(Choice==3):
            CheckGuest=input("Enter the Guest Name to Check:")
            if CheckGuest in Guest_List:
                print(f"{CheckGuest} is Attending the Party...!")
            else:
                print(f"{CheckGuest} is Not Attending the Party...!")
        elif(Choice==4):
            if len(Guest_List)==0:
                print("Guest List is Empty...!")
            else:
                Guest_List.sort()
                print("Hurray Here's your Guest List")
                print(Guest_List)
        else:
            print("Enjoy Your Party.....!")
            break
    else:
        print("In-Valid Input")