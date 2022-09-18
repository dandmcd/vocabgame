import sys
import json
import pprint
from types import SimpleNamespace
import random
from random import randint, shuffle
from dataclasses import dataclass
from typing import List


# vocab = {
#     "grandiose": {
#       "id": 1,
#       "answer": "characterized by affectation of splendor or by exaggeration"
#     },
#     "facsimile": {
#       "id": 2,
#       "answer": "an exact copy"
#     },
#     "mawkish": {
#       "id": 3,
#       "answer": "exaggeratedly or childishly emotional"
#     },
#     "sophia": {
#       "id": 4,
#       "answer": "divine wisdom"
#     },
#     "conciliate": {
#       "id": 5,
#       "answer": "to make more friendly or less angry"
#     },
#     "panache": {
#       "id": 6,
#       "answer": "dash or flamboyance in style and action"
#     },
#     "assiduous": {
#       "id": 7,
#       "answer": "showing great care, attention, and effort"
#     },
#     "adjure": {
#       "id": 8,
#       "answer": "to urge or advise earnestly"
#     },
#     "umbrage": {
#       "id": 9,
#       "answer": "a feeling of being offended at what someone has said or done"
#     },
#     "succint": {
#       "id": 10,
#       "answer": "giving the gist of something without excessive words"
#     },
#     "germinal": {
#       "id": 11,
#       "answer": "containing seeds of later development"
#     },
#     "fauna": {
#       "id": 12,
#       "answer": "the animals of a given region or period considered as a whole."
#     }
#   }

# class Word(object):
#   def __init__(self, id, answer):
#     self.id = id
#     self.answer = answer

vocab = {}

# with open('some.json', 'w') as f:
#   json.dump(vocab, f)
with open('some.json', 'r') as f:
  vocab = json.load(f)


print(vocab['sophia'])


# data = json.dumps(vocab)
# dataObj = json.loads(data)
# dataObjList = list(data.vocab())
# print(type(vocab))

shuffledVocab = list(vocab.items())
# print(shuffledVocab)
random.shuffle(shuffledVocab)
print(shuffledVocab[0])
# shuffledDict = dict(dataObjList)
# print(shuffledDict)
for word in shuffledVocab:
  print(word)

# vocab["taco"] = {"answer": "yummy"}
print(vocab)

def change_word(word, answer, update=False):
  if word in vocab and update == False:
    response = input("Word is already on the list, do you want to update it?  Type yes to update.")
    if response.lower() == "yes":
      vocab[word] = {"answer": answer}
      print(vocab)
      print("Word successfully updated!")
    else:
      edit_menu()
  else:
    vocab[word] = {"answer": answer}
    print(vocab)
    print("Word successfully added!")
    

def update_word(word, answer):
  pass


def delete_word(word):
  if word in vocab:
    response = input("Are you sure you want to delete {word}?  Type yes to confirm or press enter to cancel")
    if response.lower() == "yes":
      del vocab[word]
      print(vocab)
      print()
      print("Word successfully deleted!")
      edit_menu()
    else:
      edit_menu()

  else:
    print("I didn't find this word")
  


def list_words():
  # pprint.pprint(vocab)
  print(json.dumps(vocab, indent=4, sort_keys=True))

def exit():
  print("Goodbye")
  sys.exit()

print("taco")
print("bell pizza hell john")

def edit_menu():
  print()
  print("EDIT MENU --- Choose what you would like to do next")
  print("V - View a list of vocabulary words")
  print("A - Add a word")
  print("U - Update an existing word")
  print("D - Delete a word")
  print("R - Return to Main Menu")
  while True:
    command = input("Choose a command from above")
    if command.lower() == "v":
      list_words()
      edit_menu()
    elif command.lower() == "a":
      word = input("Enter in the word you would like to add ...")
      answer = input("Enter the answer ...")
      change_word(word.lower(), answer.lower())
    elif command.lower() == "u":
      word = input("Enter in the word you would like to update  ...")
      answer = input("Enter the answer ...")
      change_word(word.lower(), answer.lower(), update=True)
    elif command.lower() == "d":
      word = input("Enter the word to delete")
      delete_word(word.lower())     
    elif command.lower() == "r":
      break
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
    command = input("Choose a command from above")
    if command.lower() == "p":
      pass
      #play game
    elif command.lower() == "u":
      edit_menu()
    elif command.lower() == "e":
      break
    else:
      print("Not a valid command, please try again")
      start_menu()
  print("Exiting ...")
  exit()

start_menu()

# while True:
#   command = input("Choose a command from above")
#   if command.lower() == "p":
#     pass
#     #play game
#   elif command.lower() == "u":
#     command = input("Choose next command")
#     if command.lower() == "v":
#       list_words()
#       edit_menu()
#     elif command.lower() == "a":
#       pass
#       #add_word()
#     elif command.lower() == "u":
#       pass
#       #add_word() - Use same function
#     elif command.lower() == "d":
#       pass
#       delete_word()     
#     elif command.lower() == "r":
#       break
#   elif command.lower() == "e":
#     break
#   else:
#     print("Not a valid command, please try again")
#     start_menu()
# print("Exiting ...")