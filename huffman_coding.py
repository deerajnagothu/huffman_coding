# Deeraj Nagothu
# Homeowork 06
# Huffman Coding for 26 English letters

import math
import operator


def assign_Codeword(x,y, codewords):  # This function assignes the codewords based on which is 1st and 2nd
    listx = list(x)
    listy = list(y)
    for every in listx:
        codewords[every] = "0"+codewords[every]  # If its first, it adds 0
    for every1 in listy:
        codewords[every1] = "1"+codewords[every1]
    return codewords

def add_probability(tuple, child_prob, codewords):  # Adds the probability of least two
    letter_list = []
    freq_list = []
    for each in tuple:
        letter_list.append(each[0])
        freq_list.append(each[1])

    combination_of_letters = letter_list[0]+letter_list[1]
    combination_of_frequency  = float(freq_list[0])+float(freq_list[1])
    print "* "+letter_list[0]+" with "+letter_list[1]+" =" +str(combination_of_frequency)
    codewords = assign_Codeword(letter_list[0],letter_list[1], codewords)
    del child_prob[letter_list[0]]  # Delete the last two probabilities and replace it with new combined probability
    del child_prob[letter_list[1]]
    child_prob[combination_of_letters] = combination_of_frequency
    sum_freq = combination_of_frequency
    return child_prob, sum_freq, codewords


filename = "google-10000-english.txt"

words_in_text = [] # Declaring a list to store all 10,000 words
with open(filename, 'r') as text:
    for each_line in text:
        each_line = each_line.lower() # Converting every letter to lower case
        words_in_text.append(each_line)
    text.close()
# Remove End of line characters from every word in the text
for x in range(0,len(words_in_text)):
    words_in_text[x] = words_in_text[x].rstrip()

splitting_words = []  # All the words will be split into individual letters

# Every word in the text is split and stored in a separate list
for word in words_in_text:
    letters_in_word = list(word)
    for letter in letters_in_word:
        splitting_words.append(letter)
# The list of letters is now counted and stored in a dictionary
number_of_letters_in_text = {}
for each_letter in splitting_words:
    if each_letter not in number_of_letters_in_text:
        number_of_letters_in_text[each_letter] = 1
    else:
        number_of_letters_in_text[each_letter] += 1

total_letters = len(splitting_words)

Letters_in_text = sorted(number_of_letters_in_text.keys())
Entropy = 0  # Calculate entropy
english_letters = sorted(number_of_letters_in_text.keys())
codewords = {}
for each in english_letters:
    codewords[each] = ""
probability = {}  # Dictionary which constitutes of all the letters and their respective probabilies
child_prob = {}  # Duplicate of the above dictionary
for z in Letters_in_text:
    frequency = (float(number_of_letters_in_text[z])/total_letters)
    probability[z]=frequency
    child_prob[z] = frequency
    z = float(1)/frequency
    log_value = math.log(z,2)
    Entropy +=(frequency*log_value)  # calculate entropy

# print(probability) # This dictionary should include all the letters with their probabilities
sum_probability = 0
print("The Steps performed based on Huffman Coding are \n")
while sum_probability < 1:
    sorted_letters = sorted(child_prob.items(), key=operator.itemgetter(1), reverse=True)  # sort dict based on prob
    length = len(sorted_letters)
    k = sorted_letters[(length-2):]  # select last 2 probabilities and call the function to add them
    child_prob,sum_probability, codewords = add_probability(k,child_prob,codewords)  # calling function


print("\nCodewords Assigment Based on Huffman Coding")
for each in codewords.keys():
    print each +" = "+codewords[each]
expected_length = 0
number_of_bits = 0
for each in codewords.keys():
    code_string = codewords[each]
    huffman_length = len(list(code_string))  # measure the codeword length for each letter
    expected_length = expected_length + float(probability[each])*huffman_length  # calculate the expected codeword lenth
    number_of_bits = number_of_bits + number_of_letters_in_text[each]*huffman_length


print("Expected codeword length is "+str(expected_length)+" bits")
print("Entropy is "+str(Entropy)+" bits")

print("The number of bits required "+str(number_of_bits)+" bits")

