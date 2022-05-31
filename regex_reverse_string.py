# This is a little project on reversing strings using regular experession
# Importing the regular expression module
import re 

# Creating a function to do the job
def reverse_string(string):
    # This assert function would ensure that the words in the string are not more than 5
    # this assert statement is to ensure consistency in capturing the groups in the string
    assert len(string.split(' ')) == 5, 'The words in the string should not be more than 5'
    # Making sure the string is not alphanumeric
    assert not string.isnumeric(), 'The string shouldn\'t contain any numeric value'
    # Writing out the regular expression that would be used to match the string and capture groups
    regex = r'^(\w*) (\w*) (\w*) (\w*) (\w*)$'
    result = re.search(regex, string)
    print(result)
    # Reversing the string
    reversed_string = "{} {} {} {} {}".format(result[5], result[4], result[3], 
                                              result[2], result[1])
    return reversed_string

reverse_string("My name is Emmanuel Ani")
    

string = "Hello World Hello"
assert len(string.split(' ')) == 4, 'Number of words in string should not be more than 4'
print(string)
    