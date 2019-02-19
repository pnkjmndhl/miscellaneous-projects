import re
import sys

#next dictionary
next_letter = {1:[2,5,6], 2:[1,5,6,7,3], 3:[2,6,7,8,4], 4:[3,7,8], 5:[1,2,6,10,9], 6:[1,2,3,7,11,10,9,5], 7:[2,3,4,6,8,10,11,12], 8:[3,4,7,11,12], 9:[5,6,10,13,14], 10:[5,6,7,9,11,13,14,15], 11:[6,7,8,10,12,14,15,16], 12:[8,7,11,15,16], 13:[9,10,14], 14:[13,9,10,11,15], 15:[14,10,11,12,16], 16:[15,11,12]}

words = sys.argv[1]
words = 'sljpeoragyoeutee'

set_word = "".join(set(words))

all_words = open("new.txt",'r').read().replace('\n',"  ")

subset_dictionary = re.findall('(['+set_word+'])',all_words)

def next_index_in_matrix(pos): # position(pos) is the index+1
    word_list = []
    position = next_letter[pos]
    for values in position:
        letter = words[values-1] # arrays start from 0
        word_list.append(values)
    return next_letter[pos]

def get_str_from(arr_list):
    str = ""
    for value in arr_list:
        str = str + get_letter_from(value)
    return str


def get_letter_from(pos):
    return words[pos-1]


def get_letters_from_indexes(list):
    str = ""
    for value in list:
        str = str + words[value-1]
    return str


#checks if the word is in dictionary
def next_letters_in_dict(letters):
    next_letter_list = re.findall('\s'+letters+'([a-z\s])',all_words)
    #next_letter_list = re.findall(letters+'(\w)',all_words)
    return list(set(next_letter_list))

found_words = []
# def find_next_cumulative_index_in_matrix(array_list): #finds next letter in matrix
#     global found_words
#     #print("Current Found Words: {0}".format(found_words))
#     print("Called Array: {0}".format(array_list))
#     str_list = get_str_from(array_list)
#     print("string list:  "+str_list)
#     print("{0} diff {1}".format(list(set(next_letter[array_list[-1]])),array_list))
#     new_index = list(set(next_letter[array_list[-1]]).difference(set(array_list)))
#     letters_in_new_index = get_letters_from_indexes(new_index)
#     print("new_index: {0}".format(new_index))
#     print("letters_in_new_index: {0}".format(letters_in_new_index))
#     print("next_letters_in_dict: {0}".format(next_letters_in_dict(str_list)))
#     for letter in next_letters_in_dict(str_list): #if any from dictionary
#         print("for {0}".format(letter))
#         if letter in letters_in_new_index: # is in matrix
#             print("*")
#             index = letters_in_new_index.index(letter)
#             print str_list + letter + " @ " + str(new_index[index])
#             if " " in next_letters_in_dict(str_list+letter):
#                 print("{0} added to list".format(str_list+letter))
#                 found_words.append(str_list+letter)
#             print("Calling recursively: " + str_list+letter)
#             array_list.append(new_index[index])
#             if find_next_cumulative_index_in_matrix(array_list) == 0:
#                 continue
#         else:
#             print("Not found in matrix")
#             continue
#     return 0

def get_next_index_list(index): #get next index letter in matrix
    return next_letter[index]


global_index_list = []

def create_index_list(index):
    global global_index_list
    local_index_list = []
    for i in next_letter[index[-1]]:
        local_index_list.append(local_index_list + [i])
    print(local_index_list)
    for value in next_letter[index[-1]]:
        global_index_list.append(local_index_list)
    create_index_list(local_index_list)


for i in range(8):
    index = []
    index.append(next_letter[i])




#print("Dictionary: ")
#print(all_words)


for i in range(1,16):
    print("**************************************")
    find_next_cumulative_index_in_matrix([i])


found_words.sort(key = len)
found_words.reverse()

found_words = [x for x in found_words if len(x)>2]

print("Found Words:")
for x in found_words:
    print x


