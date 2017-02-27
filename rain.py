# Rahul Ramesh
#rvramesh@bu.edu
import random

def create_dictionary(filename):
    """creates a dictionary based on the amount of words in a text file"""
    file = open(filename, 'r', encoding='utf8', errors='ignore')
    text = file.read()
    file.close()

    words = text.split()

    d = {}

    current_word = '$'
    
    for next_word in words:
        if current_word not in d:
            d[current_word] = [next_word]
        else:
            d[current_word] += [next_word]
            
        if next_word[-1] == '.' or next_word[-1] == '?' or next_word[-1] == '!':
            current_word = '$'
        else:
            current_word = next_word
            
    return d 
    
def generate_text(word_dict,num_words):
    """generates new text based on the create_dictionary function"""
    y = ''
    current_word = '$'
    next_word = ''
    for x in range(num_words):
        wordlist = word_dict[current_word]
        next_word = random.choice(wordlist)
        y += ' ' + next_word
        if next_word[-1] == '.' or next_word[-1] == '?' or next_word[-1] == '!':
           current_word = '$'
        else:
            current_word = next_word
    while len(y) > 140:
        f = y.rfind(' ')
        y = y[:f]
    return str(y)
    
def count_syll(word):
    count = 0
    vowels = 'aeiouy'
    word = word.lower().strip(".:;?!-")
    for i in range(1,len(word)):
        if word[i] in vowels and word[i - 1] not in vowels:
            count +=1
    if word.endswith('re'):
        count += -1
    if word.endswith('ce'):
        count += -1
    if word.endswith('le'):
        count += 0
    if word.endswith('ile'):
        count += -1
    if word.endswith('ed'):
        count += -1
    if word.endswith('eare'):
        count += -1
    if count == 0:
        count = 1
    return count
def haiku_maker(generated_txt):
    pre = generated_txt.split()
    line = ''
    count = 0
    for i in range(len(pre)):
        count += count_syll(pre[i])
        if count >= 5:
            g = generated_txt.find(pre[i + 1])
            line += generated_txt[:g] + '/'
            break
    if count == 4:
        line += 'thee'
    if count == 6:
        line = line[:-1] + '/'
    return line
def haiku_maker2(generated_txt):
    pre = generated_txt.split()
    line = ''
    count = 0
    for i in range(len(pre)):
        count += count_syll(pre[i])
        if count >= 7:
            g = generated_txt.find(pre[i + 1])
            line += generated_txt[:g] + '/'
            break
    if count == 6:
        line += 'be'
    if count == 8:
        line = line[:-1] + '/'
    return line
def haiku_maker3(generated_txt):
    pre = generated_txt.split()
    line = ''
    count = 0
    for i in range(len(pre)):
        count += count_syll(pre[i])
        if count >= 5:
            g = generated_txt.find(pre[i + 1])
            line += generated_txt[:g]
            break
    if count == 4:
        line += 'thee'
    if count == 6:
        line = line[:-1]
    return line
v = create_dictionary('rain.txt')
g = generate_text(v,20)
h = generate_text(v,20)
f = generate_text(v,20)

print(haiku_maker(g), haiku_maker2(h), haiku_maker3(f))

