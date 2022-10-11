# Helper functions for Blackfoot project
# CMPT 120 
# Nov. 30, 2020

# import moddules
import wave
import cmpt120image
import random
from replit import audio 

### function for concatenating audio files
def concat(infiles,outfile):
  """
  Input: 
  - infiles: a list containing the filenames of .wav files to concatenate,
    e.g. ["hello.wav","there.wav"]
  - outfile: name of the file to write the concatenated .wav file to,
    e.g. "hellothere.wav"
  Output: None
  """
  data= []
  for infile in infiles:
      w = wave.open(infile, 'rb')
      data.append( [w.getparams(), w.readframes(w.getnframes())] )
      w.close()    
  output = wave.open(outfile, 'wb')
  output.setparams(data[0][0])
  for i in range(len(data)):
      output.writeframes(data[i][1])
  output.close()

### function to perform "learn"
def learn(location):
  """
  input: the user's present location 
  output: none
  purpose: 
  - user types in a word they wish to learn
  - console outputs the Blackfoot translation and audio 
  """
  # set a while loop to ask the user for a word they wish to translate
  while True:
    if location in ["town","restaurant","people","home","greetings"]:
      word_input = input("What Blackfoot word do you want to learn? Type it in English, or type done to finish. ").lower().strip(",!.? ").replace("'","").replace(".","")

    # open the appropriate text file based on the location
    if location in ["town","restaurant","people","greetings","home"]:
      words = open("text_files/" + location + "_words.csv")
      # remove the first line
      words.readline()

      # initialize a dictionary
      dictionary = {}
      # loop through the lines to get each word and its translation
      for line in words:
        linelist = line.strip().split(",")
        english = linelist[0]
        blackfoot = linelist[1]
        dictionary[english] = blackfoot
      # update the dictionary with the words and their translations
      blackfoot_translation = dictionary.get(word_input)

      # set conditionals to break, receive an unknown word, and provide translations
      if word_input == "done":
        break
      elif blackfoot_translation == None:
        print("Sorry, I don't know that word.")
      else:
        print("In Blackfoot that is: " + blackfoot_translation)
        # play the audio for the Blackfoot word
        # and replace spaces in the input with underscores
        no_spaces = word_input.replace(" ","_")
        learn_audio = "sounds/" + no_spaces + ".wav"
        audio.play_file(learn_audio)
       
### function to perform the "basic test"
def basic_test(location):
  """
  input: user's current location
  output: user's score for the test & the location the test occurred in 
  purpose: 
  - console asks user 10 questions with random Blackfoot words
  - user inputs answer in English 
  - program keeps track of score 
  """
  # open the appropriate text file based on the location
  if location in ["town","restaurant","people","greetings","home"]:
    test_words = open("text_files/" + location + "_words.csv")
    # remove the first line
    test_words.readline()

    # initialize a list of Blackfoot words and a dictionary
    blackfoot_words = []
    dictionary = {}
    # loop through the lines and index to get the specific values 
    for line in test_words:
      linelist = line.strip().split(",")
      english = linelist[0]
      blackfoot = linelist[1]
      # create the dictionary
      dictionary[blackfoot] = english
      # add the blackfoot words to the previous list
      blackfoot_words += [blackfoot]

  # initialize a score
  basic_score = 0
  # create a for loop with 10 iterations
  for i in range(10):
    # get a random Blackfoot word
    random_blackfoot_word = random.choice(blackfoot_words)
    # get the correct translation for the Blackfoot word
    correct_answer = dictionary.get(random_blackfoot_word)
    
    # ask the user a question with a random blackfoot word
    # and play the audio for the Blackfoot word
    no_spaces = correct_answer.replace(" ","_")
    basic_audio = "sounds/" + no_spaces + ".wav"
    audio.play_file(basic_audio)
    basic_input = input("What is " + random_blackfoot_word + "? ").lower().strip(",!.? ").replace("'","").replace(".","")
  
    # reply based on user input and update the score
    if basic_input == correct_answer:
      basic_score += 1
      print("Good job!")
    else:
      print("Nope it's '" + correct_answer + "'")
  # give the user their score
  print("You got " + str(basic_score) + "/10 right!")

  return basic_score, location

### function to perform the "custom test"
def custom_test(location):
  """
    input: user's current location
    output: user's score for the test & the location the test occurred in 
    purpose: 
    - console asks user 10 questions with random English words
    - console gives user 2 Blackfoot answer options
    - user inputs Blackfoot translation
    - program keeps track of score 
    """
  # open the appropriate text file based on the location
  if location in ["town","restaurant","people","greetings","home"]:
    test_words = open("text_files/" + location + "_words.csv")
    # remove the first line
    test_words.readline()
  
  # initialize lists of English and Blackfoot words and a dictionary
  english_words = []
  blackfoot_words = []
  eng_to_black_dict = {}
  black_to_eng_dict = {}
  # loop through the lines and index to get the specific values 
  for line in test_words:
    linelist = line.strip().split(",")
    english = linelist[0]
    blackfoot = linelist[1]
    # add to the dictionaries
    eng_to_black_dict[english] = blackfoot
    black_to_eng_dict[blackfoot] = english
    # add the appropriate words to the previous lists
    english_words += [english]
    blackfoot_words += [blackfoot]

  # initialize a score 
  custom_score = 0
  # create a for loop with 10 iterations
  for i in range(10):
    # get a random English word & its translation
    random_english_word = random.choice(english_words)
    correct_answer = eng_to_black_dict.get(random_english_word)
    # get a random Blackfoot word & its translation
    random_blackfoot_word = random.choice(blackfoot_words)
    random_translation = black_to_eng_dict.get(random_blackfoot_word)

    # check to make sure the random Blackfoot word isn't the correct answer
    if correct_answer == random_blackfoot_word:
      while True:
        random_blackfoot_word = random.choice(blackfoot_words)
        if correct_answer != random_blackfoot_word:
          break

    # create a list with the random Blackfoot word and the correct answer
    options = [random_blackfoot_word,correct_answer]
    # randomize the options and make sure they don't duplicate
    random_option = random.choice(options)
    if random_option == options[0]:
      remaining_option = options[1]
    elif random_option == options[1]:
      remaining_option = options[0]
    
    # play the audio for the Blackfoot words
    no_spaces1 = random_english_word.replace(" ","_")
    no_spaces2 = random_translation.replace(" ","_")
    custom_audio1 = "sounds/" + no_spaces1 + ".wav"
    custom_audio2 = "sounds/" + no_spaces2 + ".wav"
    concat([custom_audio1,custom_audio2],"sounds/custom_concat.wav")
    audio.play_file("sounds/custom_concat.wav")

    # ask the user a question with the random English word
    custom_input = input("Does '" + random_english_word + "' translate to '" + random_option + "' or '" + remaining_option + "'? ").lower().strip(",!.? ").replace("'","").replace(".","")
    # update the score and reply to the user accordingly
    if custom_input == correct_answer:
      custom_score += 1
      print("Good job!")
    else:
      print("Nope it's " + correct_answer)

  # give the user their score
  print("You got " + str(custom_score) + "/10!")

  return custom_score, location

### function to perform "move"
def move(location_input):
  """
  input: location the user has asked to go to 
  output: user's current location 
  purpose: 
  - allow user to switch between locations 
  - display the new location's image in the console 
  """
  # set a while loop asking the user where they want to go
  invalid_location = True
  while invalid_location:
    location_input = input("Where do you want to go (Town/Restaurant/People/Greetings/Home)? ").lower().strip("!,?. ")
    # update the current location
    current_location = location_input

    # if the location is valid, display that location's image & end the loop
    if location_input in ["town","restaurant","people","greetings","home"]:
      invalid_location = False
      move_to = cmpt120image.getImage("images/" + location_input + ".png")
      cmpt120image.showImage(move_to,"location.png")
    else: 
      print("Sorry I didn't get that.")

  return current_location

### function to display the top test scores for each location
def top_scores(location,basic_scores_dict,custom_scores_dict):
  """
  input: user's current location & dictionaries for both test types
  output: none
  purpose: 
  - display the top test score for each test type for current location 
  """
  # give the max basic test score for the location
  basic_scores = basic_scores_dict.get(location)
  top_basic_score = 0
  for score in basic_scores:
    if score > top_basic_score:
      top_basic_score = score
  print("Your top score for the basic test in " + location + " is " + str(top_basic_score) + "/10!")

  # give the max custom test score for the location
  custom_scores = custom_scores_dict.get(location)
  top_custom_score = 0
  for score in custom_scores:
    if score > top_custom_score:
      top_custom_score = score
  print("Your top score for the custom test in " + location + " is " + str(top_custom_score) + "/10!")

### function to perform "speech synthesis"
def speech_synthesis():
  """
  input: none 
  output: none 
  purpose: 
  - allow the user to choose from a series of options 
  - add together appropriate audio files and play the sentence
  """
  while True:
    print("Let's build some sentences in Blackfoot!")

    # ask for a time input 
    print("Starting with when, please type one of: \n'This evening' \n'This morning' \n'Today' \n'Tomorrow'")
    time_input = input().lower().strip(",!?.").replace(" ","_")
    # format the time into audio
    time_audio = "sounds/" + time_input + ".wav"

    # ask for a verb phrase
    print("Next, please choose one of the following verb phrases: \n'I went' \n'I will go' \n'I will eat")
    verb_input = input().lower().strip(",!?.").replace(" ","_")
    # format the verb into audio
    verb_audio = "sounds/" + verb_input + ".wav"

    # if the user said "i will eat", ask for a food
    if verb_input == "i_will_eat":
      print("Finally, please choose a food: \n'Dessert' \n'Burger' \n'Fries' \n'Bread' \n'Apples' \n'Oranges' \n'Fish'")
      food_input = input().lower().strip(",!?.")
      # format the food into audio
      food_audio = "sounds/" + food_input + ".wav"
      # play the audio 
      print("In Blackfoot, this sentence sounds like: ")
      concat([time_audio,verb_audio,food_audio],"sounds/speech_synthesis.wav")
      audio.play_file("sounds/speech_synthesis.wav")

    # otherwise, ask for a destination
    else:
      print("Finally, please choose a destination: \n'Cafe' \n'Cinema' \n'Night club' \n'House' \n'Store' \n'Tipi'")
      destination_input = input().lower().strip(",!?.").replace(" ","_")
      # format the destination into audio 
      destination_audio = "sounds/" + destination_input + ".wav"
      # play the audio 
      print("In Blackfoot, this sentence sounds like: ")
      concat([time_audio,verb_audio,destination_audio],"sounds/speech_synthesis.wav")
      audio.play_file("sounds/speech_synthesis.wav")

    while True:
      repeat = input("Would you like to hear that again? (yes/no) ").lower().strip(",.!? ")
      if repeat == "no":
        break
      elif repeat == "yes":
        audio.play_file("sounds/speech_synthesis.wav")
      else:
        print("Sorry, I didn't get that.")
    
    break