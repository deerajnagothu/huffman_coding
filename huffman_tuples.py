# Deeraj Nagothu
# Homework 6, Information theory
# Python 2.7
# huffman coding for tuples


import math
import operator
import re
filename = "google-10000-english.txt"




def assign_Codeword(x,y, codewords):
    listx = re.findall('..',x)
    listy = re.findall('..',y)
    for every in listx:
        codewords[every] = "0"+codewords[every]
    for every1 in listy:
        codewords[every1] = "1"+codewords[every1]
    return codewords

def add_probability(tuple, child_prob, codewords):
    letter_list = []
    freq_list = []
    for each in tuple:
        letter_list.append(each[0])
        freq_list.append(each[1])

    combination_of_letters = letter_list[0]+letter_list[1]
    combination_of_frequency  = float(freq_list[0])+float(freq_list[1])
    #print "* "+letter_list[0]+" with "+letter_list[1]+" =" +str(combination_of_frequency)
    codewords = assign_Codeword(letter_list[0],letter_list[1], codewords)
    del child_prob[letter_list[0]]
    del child_prob[letter_list[1]]
    child_prob[combination_of_letters] = combination_of_frequency
    sum_freq = combination_of_frequency
    return child_prob, sum_freq, codewords

def split_into_tuple(word):  # function to split a word into combination of 2
    letters = list(word)
    comb_of_two = []
    for x in range(0, len(letters)):
        if x < (len(letters)-1):
            z = letters[x] + letters[x+1]
            comb_of_two.append(z)
        else:
            continue
    return comb_of_two

words_in_text = []  # Declaring a list to store all 10,000 words
with open(filename, 'r') as text:
    for each_line in text:
        each_line = each_line.lower() # Converting every letter to lower case
        words_in_text.append(each_line)
    text.close()
# Remove End of line characters from every word in the text
for x in range(0,len(words_in_text)):
    words_in_text[x] = words_in_text[x].rstrip()

collection_of_two_letters = []

for each in words_in_text:
    output = split_into_tuple(each)
    for y in output:
        collection_of_two_letters.append(y)

dictionary_of_2letters = {}  # dictionary of all the tuples in the text with its occurrence

for x in collection_of_two_letters:
    if x not in dictionary_of_2letters:
        dictionary_of_2letters[x] = 1
    else:
        dictionary_of_2letters[x] += 1

values = dictionary_of_2letters.values()
total = 0
for x in values:
    total += int(x)

comb_in_text = dictionary_of_2letters.keys()
codewords = {}
for each in comb_in_text:
    codewords[each] = ""
tuples_probability = {}
child_tuples_probability = {}
Entropy = 0  # Compute entropy
for z in comb_in_text:
    frequency = (float(dictionary_of_2letters[z])/total)
    tuples_probability[z] = frequency
    child_tuples_probability[z] = frequency
    y = float(1)/frequency
    log_value = math.log(y, 2)
    Entropy += (frequency*log_value)

sum_probability = 0
#print("The Steps performed based on Huffman Coding are \n")
while sum_probability < 1:
    sorted_letters = sorted(child_tuples_probability.items(), key=operator.itemgetter(1), reverse=True)
    #print(sorted_letters)
    length = len(sorted_letters)
    #print(sorted_letters[(length-2):])
    k = sorted_letters[(length-2):]
    child_prob,sum_probability, codewords = add_probability(k,child_tuples_probability,codewords)  # iasrntwkbpoeyfumglcvzqjxhd =1.0


print("\nCodewords Assigment Based on Huffman Coding")
for each in codewords.keys():
    print each +" = "+codewords[each]
expected_length = 0
number_of_bits = 0
for each in codewords.keys():
    code_string = codewords[each]
    huffman_length = len(list(code_string))
    expected_length = expected_length + float(tuples_probability[each])*huffman_length
    number_of_bits = number_of_bits + dictionary_of_2letters[each]*huffman_length


print("Expected codeword length is "+str(expected_length)+" bits")
print("Entropy is "+str(Entropy)+" bits")

print("The number of bits required "+str(number_of_bits)+" bits")





