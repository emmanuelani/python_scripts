# Write your code here

def flower_dict(filename):
    flower_dict = {}
    #using the with statement, I open and read the "Flower.txt" file
    with open(filename) as f:
        print(f)
        for line in f:
            letter = line.split(': ')[0].lower()
            print(letter)
            flower = line.split(': ')[1].strip()
            print(flower)
            flower_dict[letter] = flower
    return flower_dict

# HINT: create a function to ask for user's first and last name
def user_input():
    #asks the user to input their name
    flowers_t = flower_dict('flowers.txt')
    username = input("Enter your first and last name: ")
    #parse the username to get the first letter of the first name
    first_name = username[0].lower()
    first_letter = first_name[0]
    
    print('Unique flower name with the first letter: {}'.format(flowers_t[first_letter]))


# print the desired output
user_input()
