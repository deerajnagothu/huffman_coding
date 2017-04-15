# Deeraj Nagothu
# Homeowork 06
# Huffman Coding for 26 English letters

import math
import operator


def assign_Codeword(x,y):
    return x,y


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
print("Total Number of Letters in the Given text: "+str(total_letters))
Letters_in_text = sorted(number_of_letters_in_text.keys())
Entropy = 0  # Calculate entropy
probability = {}
for z in Letters_in_text:
    frequency = (float(number_of_letters_in_text[z])/total_letters)
    probability[z]=frequency
    z = float(1)/frequency
    log_value = math.log(z,2)
    Entropy +=(frequency*log_value)

# print(probability) # This dictionary should include all the letters with their probabilities

sorted_letters = sorted(probability.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_letters)