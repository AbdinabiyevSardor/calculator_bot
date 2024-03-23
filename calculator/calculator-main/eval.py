a = input().strip()

b = 0
ind = int()
for i in a:
    if i == '+' or i == '-' or i == '*' or i == '/':
        ind = b
        break
    b += 1

if i == '+':
    print(int(a[0:b]) + int(a[b+1:]))
    
elif i == '-':
    print(int(a[0:b]) - int(a[b+1:]))
    
elif i == '*':
    print(int(a[0:b]) * int(a[b+1:]))
  
elif i == '/':
    try:
        
        nat = str(int(a[0:b]) / int(a[b+1:]))
        c = nat.index('.')
        

    except ZeroDivisionError:
        print("ERROR!!!")
 
else:
    print("ERROR!!!")
