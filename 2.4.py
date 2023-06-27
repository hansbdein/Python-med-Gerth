x = int(input("x: ")) 

low = 0 
high = x + 1

while low + 1 != high:  # low <= sqrt(x) < high 

    mid = (high + low) // 2
    
    print(high,mid,low)
    
    if mid * mid <= x:
        low = mid
    else:
        high = mid
      
    
      
    
print(low)  # low = floor(sqrt(x)