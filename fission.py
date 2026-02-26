# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")

# inp=int(input("enter number"))
# print(inp)
# # from collections impo
# li=[1,2,3,4,5,1,2,3,1,2,4]


# for i in li:
    
# temp={}
# for i in range(0,len(li)):
#     count=1
#     if li[i] not in temp:
#         for k in range(i,len(li)):
#             if li[i]==li[k]:
#                 count+=1
#         temp[li[i]]=li.count(i)
#     else:
#         continue
# print(temp) 
# print(temp[inp])

    
# li.pop(True)
# print(li)


# from fastapi import FastAPI
# from pydantic import BASEMODEL



# app=FastAPI()

# class inprequst(BASEMODEL):
#     userid: int
#     username: str
#     age: int

# app.post("/adduser")
# sync def adduser(request:inprequest):
#     print(request.userid)
#     print(request.username)
#     print(request.age)
    


nums = [1,2,3,2,1]
nums=[1, 2, 3, 2, 1]
# nums=[4]
k = 6
# Valid subarrays:
# [1,2,3] = 6
# [3,2,1] = 6
i=0
temp=[]
while(i<len(nums)):
    print(i)
    for j in range(0,len(nums)):
        if i==0 and j==0:
            j+=1
        # for i in range(0,len(nums),3):
        # print(nums[i:i+j])
        # if len(nums[i:i+1])<3:
        #     break
        if sum(nums[i:i+j])==k:
            if nums[i:i+j] not in temp:
                temp.append(nums[i:i+j])
    i+=1
print(temp)  
    
    
    