num=int(input())
mid=0
if num>=100 and num<999:
    mid=num//10
    mid=mid%10
    if(mid%3==0):
        print("Trendy Number")
    else:
        print("Not a Trendy Number")
    
