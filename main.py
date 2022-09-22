import sys
import json
import random

#Pull the json file data and convert to a Python dictionary
vocab = {}
with open('some.json', 'r') as f:
  vocab = json.load(f)

#Initialize a list that will be used to feed answers for the game to multiple functions 
listOfAnswers = []

#Converts the vocab dict to a list to randomly shuffle the list, and create an answer list for use in the game
def shuffleVocab():
  count = -1
  shuffledVocab = list(vocab.items())
  random.shuffle(shuffledVocab)
  shuffledDict = dict(shuffledVocab)
  for word in shuffledDict:
    count += 1
    #Currently id has no usage, but could be utuilized if there was a database to store the vocabulary
    shuffledDict[word].update(id=count)
    listOfAnswers.append(shuffledDict[word]['answer'])
  count = 0
  return shuffledDict

#Runs all functions pertaining to the vocab practice game
def play_game():
  #Clear any prior list of answers to prevent duplicates from prior games
  listOfAnswers.clear()
  #Variable stores all of the shuffled key value pairs for words and answers
  shuffledDict = shuffleVocab()
  #Score counters
  correctCounter = 0
  incorrectCounter = 0
  #Track question number, which also is a param used to get the question and matching answer
  gameCounter = 0
  #Game loop, starts with first question and prints 4 answers
  for word in shuffledDict:
    print("Score:", correctCounter,"-", incorrectCounter, "\n")
    #Game counter increases after each loop
    gameCounter += 1
    print("Question", gameCounter, " What is the definition for", word, "...")
    answers = answer_shuffler(gameCounter)
    print("(A) - ", answers[0])
    print("(B) - ", answers[1])
    print("(C) - ", answers[2])
    print("(D) - ", answers[3])
    while True:
      response = input("Choose your answer by entering a, b, c, or d ... ")
      if response.lower() in ("a", "b", "c", "d"):
        if response.lower() == "a":
          if answers[0] == shuffledDict[word]["answer"]:
            print("\nYES, THAT IS CORRECT!!! :)\n")
            correctCounter += 1
            break
          else:
            print("\nNO,  SORRY, THAT IS NOT CORRECT! :(\n")
            incorrectCounter += 1
            break
        elif response.lower() == "b":
          if answers[1] == shuffledDict[word]["answer"]:
            print("\nYES, THAT IS CORRECT!!! :)\n")
            correctCounter += 1
            break
          else:
            print("\nNO,  SORRY, THAT IS NOT CORRECT! :(\n")
            incorrectCounter += 1
            break
        elif response.lower() == "c":
          if answers[2] == shuffledDict[word]["answer"]:
            print("\nYES, THAT IS CORRECT!!! :)\n")
            correctCounter += 1
            break
          else:
            print("\nNO,  SORRY, THAT IS NOT CORRECT! :(\n")
            incorrectCounter += 1
            break
        elif response.lower() == "d":
          if answers[3] == shuffledDict[word]["answer"]:
            print("\nYES, THAT IS CORRECT!!! :)\n")
            correctCounter += 1
            break
          else:
            print("\nNO,  SORRY, THAT IS NOT CORRECT! :(\n")
            incorrectCounter += 1
            break
      else:
        print("\nNot a valid command, please try again\n")
        continue
  print("\nFinal Score:", correctCounter, "-", incorrectCounter)
  print()
  gameCounter = 0
  start_menu()

def answer_shuffler(gameCounter):
  ansCount = gameCounter - 1
  correctAnswer = ""
  correctAnswer = listOfAnswers[ansCount]
  randomAnswers = random.sample([i for i in listOfAnswers if i != correctAnswer], 3)
  returnAnswers = randomAnswers
  returnAnswers.append(correctAnswer)
  random.shuffle(returnAnswers)
  return returnAnswers

def change_word(word, answer, update=False):
  if word in vocab and update == False:
    response = input("Word is already on the list, do you want to update it?  Type yes to update ... ")
    if response.lower() == "yes":
      vocab[word] = {"answer": answer}
      save_vocab()
      print("\nWord successfully updated!")
    else:
      edit_menu()
  else:
    vocab[word] = {"answer": answer}
    save_vocab()
    print("\nWord successfully added!")


def delete_word(word):
  if word in vocab:
    response = input(f"Are you sure you want to delete {word}?  Type yes to confirm or press enter to cancel ... ")
    if response.lower() == "yes":
      del vocab[word]
      save_vocab()
      print("\nWord successfully deleted!")
      edit_menu()
    else:
      edit_menu()

  else:
    print("I didn't find this word")
  
def list_words():
  print(json.dumps(vocab, indent=4, sort_keys=True))

def save_vocab():
    with open('some.json', 'w') as f:
      json.dump(vocab, f)

def exit():
  save_vocab()
  print("Goodbye")
  sys.exit()

def edit_menu():
  while True:
    print()
    print("EDIT MENU --- Choose what you would like to do next")
    print("V - View a list of vocabulary words")
    print("A - Add a word")
    print("U - Update an existing word")
    print("D - Delete a word")
    print("R - Return to Main Menu")
    command = input("Choose a command from above ... ")
    if command.lower() == "v":
      list_words()
      edit_menu()
    elif command.lower() == "a":
      word = input("Enter in the word you would like to add ...")
      answer = input("Enter the answer ...")
      change_word(word.lower(), answer.lower())
    elif command.lower() == "u":
      word = input("Enter in the word you would like to update  ...")
      if word in vocab:
        answer = input("Enter the answer ...")
        change_word(word.lower(), answer.lower(), update=True)
      else:
        response = input("Word not found, type 'add' to continue adding the word or press enter to go back to the edit menu ... ")
        if response == "add":
          answer = input("Enter the answer ... ")
          change_word(word.lower(), answer.lower())
        else:
          edit_menu()
    elif command.lower() == "d":
      word = input("Enter the word to delete ... ")
      delete_word(word.lower())     
    elif command.lower() == "r":
      break
    else:
      print("\nNot a valid command, please try again\n")
  start_menu()


def start_menu():
  print()
  print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
  print("  WELCOME TO THE VOCAB GAME!")
  print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
  print("P - Practice")
  print("U - Update Vocab List")
  print("E - Exit")
  while True:
    command = input("Choose a command from above ... ")
    if command.lower() == "p":
      play_game()
    elif command.lower() == "u":
      edit_menu()
    elif command.lower() == "e":
      break
    else:
      print("\nNot a valid command, please try again\n")
      start_menu()
  print("Saving and Exiting ...")
  exit()

start_menu()