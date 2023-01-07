
#   By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:             Samantha Merton
# Section:          Engineering 102 556
# Assignment:   kaprekars_constant (7.28)
# Date:               6 October 2022

#comments made directly after writing this code after been sugar coated
knum_list = [] #setting up for new integer input
knum = input('Enter a four-digit integer:\n') #user input for 4 digit number
knum_list.append(knum) #adding number to list
end_num = int(knum) #setting up to keep original number for end output
if (len(knum)) > 4: #making sure input viable for formula
    print("Invalid integer")
if (len(knum)) != 4: #converting integer to 4 digit number 
    a = (len(knum))
    a = int(a)
    x = 4 - a
    z = a + x
    knum = str(knum).zfill(z) #adding zeros
    knum = "".join(sorted(str(knum), reverse=True)) #reversing number to calculate number when entering loop
    
num = int(knum) #converting to intefer

i = 0  #setting up to count iterations
   
while num <=10000: #best i could come up with
    asc_num ="".join(sorted(str(num)))
    desc_num ="".join(sorted(str(num), reverse=True)) #loop iterates through converting new number
    asc_num = int(asc_num) #to string and then to ascending and descending interger values
    desc_num = int(desc_num)
    num = (desc_num - asc_num)
    new_num = num
    knum_list.append(new_num) #adding new number to list for end result
    i += 1
    if num == 0:
        break #if resulting value end in zero break
    if num < 1000:
        num = str(num) #if num < 1000 means need to add zeros again (thanks zybook)
        m = (len(num)) #no middle finger emoji. Lucky you
        m = int(m)
        n = 4 - m 
        q = m + n
        num = str(num).zfill(q)
        num = "".join(sorted(str(num), reverse=True)) #sorting so enter loop of doom again
        num = int(num) #you  know what time it is, integer time - converting string back to integer
    if num == 6174: #when reaches 6174 break
        break   
if num == 0:
    print(f'{end_num} > 0')
    print(f"{end_num} reaches 0 via Kaprekar's routine in {i} iterations")
else:
    for j in range ((len(knum_list)-1)):
        print(knum_list[j], end=' > ') #printing newlist values in pretty print format -Thanks Ritchey
        
    print(knum_list[-1])
    print(f"{end_num} reaches 6174 via Kaprekar's routine in {i} iterations") #tada freaking da I'm tired





