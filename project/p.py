sum=0

num=int(input('Give your number : '))

lap=num

while lap>0:
    digit=lap%10
    sum=sum+digit**3
    lap=lap//10

if sum==num:
    print(num,'is an armstrong number')
else:
    print(num,'is not an armstrong number')
    