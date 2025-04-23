for i in range(1, 15+1):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(f'{i}')
