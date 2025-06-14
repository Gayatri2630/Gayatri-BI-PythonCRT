''' 
  write a python program to:
  -->Add 10 songs to Playlist
  --> Show the PLaylist in normal and reverse order
'''
size=10
Song_List=[]
for i in range(size):
    temp=input(f"Enter the element at {i} index:")
    Song_List.append(temp)
print(Song_List)
print(Song_List[::-1])