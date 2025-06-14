Mail_ID=input("Enter the Mail ID:")
List=Mail_ID.split('@')
print(f"User Name:{List[0]}")
org=List[1]
List=org.split('.')
print(f"Org Name:{List[0]}") 
# another way using removeprefix and removesuffix