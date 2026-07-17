'''
Code to explore List, Tuple, Set & Generators
'''

def check_mutable():
    x = [1, 2, 3, 5]
    print(f'Address of list: {id(x)}')
    x.append(6)
    print(f'Address of list after append: {id(x)}')
    print('*' * 30)

    y = (100, 101, 102, 103)
    print(f'Address of Tupple: {id(y)}')
    try:
        y[1] = 105
    except Exception as exp:
        print(f'While modifing tupple:\n {exp}')
    else:
        print('Sweet success!')
    print('*' * 30)

    z = {1, 2, 3, 5, 5, 6}
    print(f'Address of set: {id(z)}')
    z.add(9)
    print(f'Address of set after append: {id(z)}')
    print('*' * 30)

check_mutable()



def sample_gen():
    '''Generator for a long sequence'''
    for i in range(10000):
        yield i

result_gen = sample_gen()
print(next(result_gen)) 
print(next(result_gen))

