from itertools import permutations

def convert(grams):
    print(grams, "grams =", 28.3495231*grams, "ounces")
convert(20)

def Fahrenheit(temp):
    print("C = ", (5/9)*(temp - 32))
Fahrenheit(0)

def solve(numheads, numlegs):
    for chickens in range(numheads):
        rabbits = numheads - chickens
        
        if 2*chickens + 4*rabbits == numlegs: 
            return chickens, rabbits
        
    print("No solution")

print(solve(35, 94))


def filter_prime(numbers):
    return list(filter(lambda x: x>1 and all(x%i != 0  for i in range(2, int(x ** 0.5) + 1)), numbers))
print(filter_prime([2,4,5,11]))


def permutation(some_string):
    return ', '.join(''.join(i) for i in permutations(some_string))
print(permutation("asset"))

def reverse(reversed_string):
    return " ".join(reversed_string.split()[::-1])
print(reverse("We are ready"))

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i] == nums[i+1]:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
    
def spy_game(nums):
    for i in range(len(nums)): 
        nums[i] = str(nums[i])
    nums = ''.join(nums)
    return '007' in nums

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


def sphere(radius):
    return 4/3 *(radius*radius*radius)
print(sphere(1))


def unique_elements(lst):
    unique_list = []
    for num in lst:
        if num not in unique_list: 
            unique_list.append(num) 
    return unique_list
print(unique_elements([1, 2, 2, 3, 4, 4, 5])) 


def is_palindrome(some_str):
    some_str = "".join(some_str.lower().split())
    return some_str == some_str[::-1]
print(is_palindrome("racecar"))       
print(is_palindrome("A man a plan a canal Panama")) 


def histogram(lt):
    for x in lt:
        print('*' * x)
histogram([4,9,7])
    