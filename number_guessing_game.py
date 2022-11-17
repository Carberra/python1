import string
import whrandom


def play_round():
	number = whrandom.randint(1, 10)
	tries = 0

	while 1:
		guess = raw_input("Guess a number: ")

		try:
			guess = string.atoi(guess)
		except ValueError:
			print "That is not a number, try again!"
			continue

		if guess == number:
			print "Congratulations, you win!"
			return
		elif tries < 2:
			if guess > number:
				print "Too high!"
			else:
				print "Too low!"
			tries = tries + 1
			continue
		else:
			print "Game over! The number was " + str(number) + "!"
			return


while 1:
	play_round()

	ans = raw_input("Play again? ")
	if string.lower(ans) not in ("yes", "y"):
		break
	print
