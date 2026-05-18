# Armstrong Number: 153: 

num = 153
temp = num
sum = 0

while temp != 0:
    rem = temp % 10
    sum += rem ** 3
    num = num // 10

if temp == sum:
    print("armstrong")
else:
    print("not armstrong")