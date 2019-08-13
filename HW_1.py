a = {i for i in range(1, 101)}
for i in a:
    if not i % 3:
        if not i % 15:
            print(f'{i} FizzBuzz')
        else:
            print(f'{i} Fizz')
    elif not i % 5:
        print(f'{i} Buzz')
    else:
        print(i)

a = {'key1': 'value1', 'key2': 'value2'}
a = {v: k for k, v in a.items()}
print(a)

a = [1, 1, 2, 3, 5, 4, 5, 5, 6]
a = list(set(a))
print(a)
