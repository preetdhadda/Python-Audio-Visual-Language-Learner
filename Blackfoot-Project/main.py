# Blackfoot Project
# Author: Preet Dhadda
# Date: November 30, 2020

# import modules
import cmpt120image
import helper

# show the town image and set current location to town
town = cmpt120image.getImage("images/town.png")
cmpt120image.showImage(town,"location.png")
current_location = "town"

# initialize dictionaries to store the scores of both test types
basic_scores_dict = {
  "town" : [],
  "restaurant" : [],
  "people" : [],
  "greetings" : [],
  "home" : []
}

custom_scores_dict = {
  "town" : [],
  "restaurant" : [],
  "people" : [],
  "greetings" : [],
  "home" : []
}
  
# introduce the program
print("Oki (Hello)! Welcome to Brocket, Alberta! I can, \n teach you some Blackfoot while you are here!")

# set while loop to ask the user what they want to do
while True:
  print("Do you want to learn some words around you (learn), \nHave me test you (test), \nGo somewhere else (move), \nView your top test scores in " + current_location + " (scores), \nBuild sentences (sentences), \nOr leave (exit)?")
  action_input = input().lower().strip("!,?. ")

  # call the appropriate function for each of the actions
  if action_input == "learn":
    helper.learn(current_location)

  elif action_input == "move":
    current_location = helper.move(current_location)

  elif action_input == "test":
    # set while loop to ask which test the user wants
    invalid_test = True
    while invalid_test:
      test_type = input("Would you like to do the basic test (basic) or the custom test (custom)? ").lower().strip("!,?. ")

      if test_type == "basic":
        invalid_test = False
        basic_results = helper.basic_test(current_location)
        # add the score to the dictionary 
        basic_score = [basic_results[0]]
        location = basic_results[1]
        basic_scores_dict[location] += basic_score

      elif test_type == "custom":
        invalid_test = False
        custom_results = helper.custom_test(current_location)
        # add the score to the dictionary 
        custom_score = [custom_results[0]]
        location = custom_results[1]
        custom_scores_dict[location] += custom_score
        
      else: 
        print("Sorry, I didn't get that. Please type 'basic' for the basic test and 'custom' for the custom test.")

  elif action_input == "scores":
    helper.top_scores(current_location,basic_scores_dict,custom_scores_dict)

  elif action_input == "sentences":
    helper.speech_synthesis()

  # break the loop if the user says exit 
  elif action_input == "exit":
    print("Goodbye, thanks for visiting!")
    break

  # say you don't understand if an unknown input is given
  else: 
    print("Sorry, I didn't get that.")
