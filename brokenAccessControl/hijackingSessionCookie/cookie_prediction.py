jSESSIONID="dVD2iRJXLGbolu7uYc6frWr4vZYZuR-TjZ3LEFI5"
hijack_cookie="2338673462221919916-1705652464016"
1705652464016
1705652464016
import time
for char in jSESSIONID:
    print(ord(char),end=",")
print("\n")
for char in hijack_cookie:
    print(ord(char),end=",")
print("\n")  
print(time.time())