test_path = [['h', 'f'], ['h', 'f'], ['s', 'd']]
test_check = [['s', 'd'], ['a', 'b'], ['x', 'e'], ['h', 'f']]
test_check2 = [['h', 'f'], ['x', 'e'], ['s', 'd'], ['a', 'b']]
test_set_check = set(map(tuple, test_check))
test_set_path = set(map(tuple, test_path))
p_test_dif = test_set_path.symmetric_difference(test_set_check)
print(p_test_dif)
p_test = (len(test_check) - len(p_test_dif))/len(test_check)
print(p_test)

test_set_check2 = set(map(tuple, test_check2))
p_test_dif2 = test_set_path.symmetric_difference(test_set_check2)
print(p_test_dif2)
p_test2 = (len(test_check2) - len(p_test_dif2))/len(test_check2)
print(p_test2)
