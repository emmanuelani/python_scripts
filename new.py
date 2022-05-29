#return true if the two words in a string start with the samme letter

string1 = 'Hello world'
string2 = 'Hey Hello'

#step 1
#convert to string using split fucntion
string1_list = string1.split() #converting the first word to a list
print(string1_list)

string2_list = string2.split() #converting the second word to a list
print(string2_list)

def compare_words(string):
        word_list = string.split()
        print(word_list)
        for words in word_list:
            print(words)
            if word_list[0][0] == word_list[1][0]:
                return True
            else:
                return False

print('-------')
print(compare_words(string1))
print('-------')
print(compare_words(string2))


# list1 = ['Emma', 'Fidelis']

# for name in list1:
#     print(name[0])
#     if nam



