weight = input('Weight: ')
weight_type = input("(L)bs or (K)g: ")
if weight_type.upper() == 'L':
    new_weight = int(weight) / 2.2046
elif weight_type.upper() == 'K':
    new_weight = int(weight) * 2.2046
else: print('That is not a correct selection')
print(f'Your converted weight is {new_weight.__round__()}')