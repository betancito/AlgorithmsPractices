#Algorithm to find maximun number
# nums = [3, 7, 2, 9, 5]
# max_num = 0
# for num in nums:
#     if num >= max_num:
#         max_num=num
    
# print(max_num)


#Algorithm to see if word is a palindrome
# is_palindromo = "radar"
# word = ""
# for i in is_palindromo:
#     word = i + word

# if (word==is_palindromo):
#     print(True)
# else:
#     print(False)  


#Algorithm to print numbers, if multiple of 3 prints fizz, if multiple of 5 prints buzz, if multiple of both prints fizzbuzz
# for i in range(1,20):
#     mod3 = i%3
#     mod5 = i%5 
#     if(mod3==0 and mod5==0):
#         print("FizzBuzz")
#     elif(mod3==0):
#         print("Fizz")
#     elif(mod5==0):
#         print("Buzz")
#     else:
#         print(i)

#Algorithm to sum only even numbers

# numbers = [1,5,7,3,8,2,3,2]
# sum = 0

# for number in numbers:
#     if number % 2 == 0:
#         sum = sum+number
        
# print (sum)
        

#Bubble sort
nums = [5,3,8,4,21,1,9,2]
n = len(nums)

for i in range(n-1):
    for j in range(n-1-i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1]= nums[j+1], nums[j]
print(nums)
