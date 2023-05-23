str1 = "hello"
str2 = "world"
concat15 = '{} {} {}'.format(str1,str2,15)
# print(concat15)# hello world 15
# print(str1.capitalize()) # first upper case remaining lower case
#print(str1.rjust(7)) # padded with spaces at the front ##   hello
#print(str1.center(7)) # padd spaces by printing strint at the centre
#print(str1.replace('l','(ell)')) # he(ell)(ell)o

# id function is used to get memory address of the varibale
#print(id(str1)) # 2550086596

# user input and modification
name = str(input("enter name :"))
age = int(input("enter age :"))
print ("my name is ", name," i am ", age," years old and this is silly writing of thanvi and manvi. dont believe it")
# to check if input name is an string and not a number
# isalpha checks if input is an alphabet
nums = input("write a name:")
if(not nums.isalpha()):
    print("you did not write a name!")
print(nums)

numbers = [1,2,3,4,5]
for num in numbers:
    if num == 3:break
    print ("break statement: ",num)

for num in numbers:
    if num ==3:
        continue
    print("continue statement: ",num)

