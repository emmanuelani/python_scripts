import random

nums_list = random.randint(0, 20)
nums = nums_list.split(',')


def generate_password():
   return random.choice(nums) + random.choice(nums)  + random.choice(nums)

my_password = generate_password()
print(my_password)




   
