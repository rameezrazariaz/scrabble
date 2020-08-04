letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#adding the values of letters and points to dictionary
letter_to_points = {key: value for key,value in zip(letters, points)}
letter_to_points[" "] = 0
#print(letter_to_points)

#function to calculate the score
def score_word(word):
  print_total = 0
  for letter in word:
    print_total += letter_to_points.get(letter, 0)
  return print_total

#brownie_points = score_word("BROWNIE")
#print(brownie_points)

#empty dictionary to store words played by each player
player_to_words = {}
player_to_points = {}

#calculating the points obtained by players and storing them in player_to_points
def playerpoints(player_to_words):
  #player_to_points = {}
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

#print(player_to_points)

def play_word():
  player_count = int(input("Enter the number of players "))
  for i in range(player_count):
    name = input("Enter the name of player {} ".format(i+1))
    words_input = input("Enter the words played by player {} ".format(i+1))
    words_played = words_input.split(" ")
    player_to_words[name] = words_played

  playerpoints(player_to_words)

play_word()

#print(player_to_words)
print(player_to_points)