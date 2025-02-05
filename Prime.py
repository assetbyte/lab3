prime = lambda x: x>1 and all(x%i != 0  for i in range(2, int(x ** 0.5) + 1))

nums = [2,4,5,3,1,11,19,17,21,23]
print(list(filter(prime, nums)))