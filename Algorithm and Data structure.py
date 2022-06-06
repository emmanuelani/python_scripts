# ALGORITHMS
# linear search
def linear_search(list, target):
    """
    return the linear position of the target if found, else return None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print('Target found at index:', index)
    else:
        print('Target not found in list')
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(numbers, 1)
verify(result)

#binary search
def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if midpoint == target:
            return midpoint
        elif midpoint < target:
            first =  midpoint + 1
        else:
            last = midpoint - 1
    
    return None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1])
numbers[2] = 78
print(numbers)
numbers.append(3)
print(numbers)

if 34 in numbers:
    print('34 found')
else:
    print('34 not found')
# alternative
for i in numbers:
    if i == 34:
        print('34 is present in the list')
    else:
        print('34 not present in list')

print(numbers.insert(0, 4))

#merge_sort algorithn

def merge_sort(list):
    """
    This algorithm sorts a list recursively in ascending order by breaking it 
    into subunits and sorting the sublists.
    It returns a new sorted list
    Divide: find the midpoint of the list and divide into subist
    Conquer: recursively sort the sublist created in the previous step
    Combine: merge the sorted sublist created in the previous step
    """
    if len(list) <= 1:
        return list
    else: