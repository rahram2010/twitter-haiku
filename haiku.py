# Rahul Ramesh
#rvramesh@bu.edu
import random, tweepy, time, sys

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
            line += generated_txt[:g]+'/'
            break
    if count == 4:
        line += 'be'
    if count == 6:
        line = line[:-1]
    return line
def haiku_maker2(generated_txt):
    pre = generated_txt.split()
    line = ''
    count = 0
    for i in range(len(pre)):
        count += count_syll(pre[i])
        if count >= 7:
            g = generated_txt.find(pre[i + 1])
            line += generated_txt[:g]+'/'
            break
    if count == 6:
        line += 'be'
    if count == 8:
        line = line[:-1]
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
        line += 'by'
    if count == 6:
        line = line[:-1]
    return line

CONSUMER_KEY = '9cTRuxAtJF5PGO2Z5XSnWvjBj'
CONSUMER_SECRET = 'CScnQbGKcqrldLv2QEpsleXepSyYzZA6jFYy2pa8W9au1TUIZ7'
ACCESS_KEY = '809216244289335296-HNibCDQwyLTSrUUTc4lqxfHEwAIKjMj'
ACCESS_SECRET = 'ozb5A9MN6qYH6zm3qFnB0AChFAHKJgCmPLU5KMLyCeK8z'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth)

while True:
    #generating text
    rain = create_dictionary('rain.txt')
    sun = create_dictionary('sunny.txt')
    cloud = create_dictionary('cloudy.txt')
    snow = create_dictionary('snowy.txt')

    #generating lines
    
    sunny_line = generate_text(sun,20)
    sunny_line2 = generate_text(sun,20)
    sunny_line3 = generate_text(sun,20)
    
    rain_line = generate_text(rain,20)
    rain_line2 = generate_text(rain,20)
    rain_line3 = generate_text(rain,20)

    cloudy_line = generate_text(cloud,20)
    cloudy_line2 = generate_text(cloud,20)
    cloudy_line3 = generate_text(cloud,20)

    snow_line = generate_text(snow,20)
    snow_line2 = generate_text(snow,20)
    snow_line3 = generate_text(snow,20)
    

    #stanza generation

    stanza1 = str(haiku_maker(rain_line))
    stanza2 = str(haiku_maker2(rain_line2))
    stanza3 = str(haiku_maker3(rain_line3))

    sun_stanza = str(haiku_maker(sunny_line))
    sun_stanza2 = str(haiku_maker2(sunny_line2))
    sun_stanza3 = str(haiku_maker3(sunny_line3))

    cloud_stanza = str(haiku_maker(cloudy_line))
    cloud_stanza2 = str(haiku_maker2(cloudy_line2))
    cloud_stanza3 = str(haiku_maker3(cloudy_line3))

    snow_stanza = str(haiku_maker(snow_line))
    snow_stanza2 = str(haiku_maker2(snow_line2))
    snow_stanza3 = str(haiku_maker3(snow_line3))

    

    stanzarainy = '☂:'+stanza1+stanza2+stanza3

    stanzasunny = '☀️:'+sun_stanza+sun_stanza2+sun_stanza3

    stanzasnowy = '⛄:️'+snow_stanza+snow_stanza2+snow_stanza3

    stanzacloudy = '☁️︎︎:'+cloud_stanza+cloud_stanza2+cloud_stanza3
    
    weather = api.user_timeline(id = '21071455', count = 1)[0]
    weather_text = weather.text
    weather_str = str(weather_text) 
    print(weather_str)

    # implementing update status

    if 'Rain' in weather_str:
        print(stanzarainy)
        api.update_status(stanzarainy)
    elif 'Fair' in weather_str:
        print(stanzasunny)
        api.update_status(stanzasunny)
    elif 'Cloudy' in weather_str:
        print(stanzacloudy)
        api.update_status(stanzacloudy)
    elif 'Clouds' in weather_str:
        api.update_status(stanzacloudy)
    elif 'Overcast' in weather_str:
        api.update_status(stanzacloudy)
    elif 'Snow' in weather_str:
        print(stanzasnowy)
        api.update_status(stanzasnowy)
    else:
        print('SOMETHING IS WRONG')

    time.sleep((60)*60*4)
