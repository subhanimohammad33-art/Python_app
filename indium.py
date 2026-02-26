# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

# Test Case 1: [1, [10, [1,3], [4,5,6], [7,8,9]], [[11,12,[13,14],15,[27,28,29]]]]
# output: 203
# Test Case 2: []
# Output: 0
# Test Case 3: [None, [None]]
# Output: 0
# Test Case 4:
# [10, [1,2,3], [4,5,6], [None, 7,8,9], [[11,12,[13,14],[[[15]]],[27,[[[28]],29]]]]]
# Output: 204


# def func(s):
#     if s==None:
#         return 0
#     if type(s)==int:
#         # print(isinstance(s,int))
#         # print(s)
#         return s
#     elif len(s)==0:
#         return 0
#     else:
#         # print(s)
#         return func(s[0])+func(s[1:])

# a=[1, [10, [1,3], [4,5,6], [7,8,9]], [[11,12,[13,14],15,[27,28,29]]]]
# a=[]
# a=[None, [None]]
# a=[10, [1,2,3], [4,5,6], [None, 7,8,9], [[11,12,[13,14],[[[15]]],[27,[[[28]],29]]]]]
# sum=0
# for i in a:
#     print(i)
#     if type(i)==int:
#         sum+=i
#     else:
#         sum+=func(i)
#     print(sum)
# print(sum)



# Given a list of keywords and a sentence, write a Python script that finds the positions (indices) of each keyword in the sentence (case-insensitive match, but preserve original casing in output), and return a dictionary sorted by the frequency (ascending) of each matched word. Try to solve this in O(n) time complexity. (10 mins)
input_list = ['manspider', 'spiderman', 'love']
strings =  "manSpider is my favorite he is Spiderman and i love Spiderman and I love watching Spiderman movies"
 
# output = {'manSpider': [0], 'love': [9, 13], 'Spiderman': [6, 10, 15]}
temp={}
for i in input_list:
    # print(i in strings.lower())
    # print(strings.lower().split(" "))
    split_str=strings.split(" ")
    for k in range(0,len(split_str)):
        if i==split_str[k].lower():
            if split_str[k] not in temp:
                temp[split_str[k]]=[k]
            else:
                temp[split_str[k]].append(k)

    
                
print(temp)
print(dict(sorted(temp.items(),key=lambda item:len(item[1]))))
            
    


    
