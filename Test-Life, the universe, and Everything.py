# while True:
#     x = int(input())
#     if x == 42:
#         break
#     print(x)
    
    
#________________same problem using function___________

def find_number():
    while True:
        number=int(input())
        
        #check the number
        if number == 42:
            break
       #print the number
        print(number)
            
if __name__ == '__main__':
    find_number()

    