#
for i in range(1, 101):
    #print(i, i%3)
    
    if i%3 ==0:
        if i%5 ==0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif i%5 ==0:
        if i%3 ==0:
            print('FizzBuzz')
        else:
            print('Buzz')
    else:
        print (i)
    