import random

print "Welcome to Rock, Paper, Scissors! The rules are as follows: Rock crushes scissors, paper covers rock, and scissors cuts paper. You will play against the console. Thanks for checking out my game!"

RPS = ['R', 'P', 'S']

wins = {'Player': 0, 'Computer': 0}

validInputs = [ 'R', 'r', 'S', 's', 'P', 'p', 'Exit', 'exit','EXIT']

def RPS_run():
	player_turn = raw_input("When ready, type 'R' for rock, 'P' for paper, or 'S' for scissors. Type 'exit' to exit.")
	computer_turn = random.choice(RPS)
	if player_turn.upper() == 'R' and computer_turn == 'R':
		score = "Player: " + str(wins['Player']) + "\nComputer: " + str(wins['Computer'])
		print "Rock vs. Rock: it's a tie!\n" + score 

	if player_turn.upper() == 'R' and computer_turn == 'P':
		wins['Computer'] = wins['Computer'] + 1
		score = "Player: " + str(wins['Player']) + "\nComputer: " + str(wins['Computer'])
		print "Rock vs. Paper: Paper wins!\n" + score 
	
	if player_turn.upper() == 'R' and computer_turn == 'S':
		wins['Player'] = wins['Player'] + 1
		score = "Player: " + str(wins['Player']) + "\nComputer: " + str(wins['Computer'])
		print "Rock vs. Scissors: Rock wins!\n" + score 

	if player_turn.upper() == 'P' and computer_turn == 'R':
		wins['Player'] = wins['Player'] + 1
		score = "Player: " + str(wins['Player']) + "\nComputer: " + str(wins['Computer'])
		print "Paper vs. Rock: Paper wins!\n" + score 
	
	if player_turn.upper() == 'P' and computer_turn == 'P':
		score = "Player: " + str(wins['Player']) + "\nComputer: " + str(wins['Computer'])
		print "Paper vs. Paper: it's a tie!\n" + score 

	if player_turn.upper() == 'P' and computer_turn == 'S':
		wins['Computer'] = wins['Computer'] + 1
		score = "Player: " + str(wins['Player']) + "\nComputer: " + str(wins['Computer'])
		print "Paper vs. Scissors: Scissors wins!\n" + score 

	if player_turn.upper() == 'S' and computer_turn == 'R':
		wins['Computer'] = wins['Computer'] + 1
		score = "Player: " + str(wins['Player']) + "\nComputer: " + str(wins['Computer'])
		print "Scissors vs. Rock: Rock wins!\n" + score 
	
	if player_turn.upper() == 'S' and computer_turn == 'P':
		wins['Computer'] = wins['Computer'] + 1
		score = "Player: " + str(wins['Player']) + "\nComputer: " + str(wins['Computer'])
		print "Scissors vs. Paper: Scissors wins!\n" + score 

	if player_turn.upper() == 'S' and computer_turn == 'S':
		score = "Player: " + str(wins['Player']) + "\nComputer: " + str(wins['Computer'])
		print "Scissors vs. Scissors: it's a tie!\n" + score 

	if player_turn not in validInputs:
		print "Sorry, I don't recognize that answer."

	if player_turn.lower() == 'exit':
		return False
	else:
		return True

game = True
while game == True:
	game = RPS_run()