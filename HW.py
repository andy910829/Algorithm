list = []
cnt = 1
while(cnt < 10):
    list.append(int(input("Please input a series of numbers:")))
    cnt+=1
    
    
def insertion_sort(list):
    for i in range(1 , len(list)):
        j  = i-1
        while(j>=0):
            if (list[j] > list[i]):
                m = list[j]
                list[j] = list[i]
                list[i] = m
                i-=1
                j-=1
            else:
                break
    print("The result of insertion sort: ", list)
    return list
    
#參考課本

def bubble_sort(list):
    for i in range(len(list)-2):
        for j in range(len(list)-i-1):
            if (list[j] > list[j+1]):
                m = list[j]
                list[j] = list[j+1]
                list[j+1] = m
    print("The result of bubble sort: ", list)
    return list

#參考:https://ithelp.ithome.com.tw/articles/10202160跟課本

list2 = insertion_sort(list)
bubble_sort(list)

def binary_search(user_input, list2):
    low = 0
    upper = len(list2)-1
    while(low <= upper):
        mid = (low + upper)//2
        if (list2[mid] > user_input):
            upper = mid -1
        
        elif(list2[mid] < user_input):
            low = mid +1
        
        elif (list2[mid] == user_input):
            return mid           
    return -1
            
#參考https://ithelp.ithome.com.tw/articles/10206818跟課本            
   
user_input = int(input("Please specify a number:"))
ans = 1
while(ans):
    if (binary_search(user_input, list2) != -1):
        print(f"The target number {user_input} found by binary search at location", binary_search(user_input, list2))
    else:
        print(f"The target number {user_input} cannot be found by binary search")
    keep = input("Want to keep going (y/n):")
    if (keep == "y"):
        user_input = int(input("Please specify a number:"))
        ans = True
    else:
        ans = False


