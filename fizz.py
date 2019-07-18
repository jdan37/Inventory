

def fb (x,y,z):


    print("\n\n\n")
    m = int(input("Enter First: "))
    n = int(input("Enter second: "))

    print("\n\n")

    for num in range(m,n):

        if num % 3==0 and num % 5 == 0:
            print('FizzBuzz')
            x = 1+x
        elif num % 3 == 0:
            print('Fizz')
            y = 1+y
        elif num % 5 == 0:
            print('Buzz')
            z = 1+z
        else:
            print(num)

    return x,y,z


a = fb(x=0,y=0,z=0)

print('\n\n')

print('fizzbuzz count:', a[0])
print('fizz count:', a[1] )
print('buzz count:', a[2])