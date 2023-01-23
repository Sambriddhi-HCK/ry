import random
words = [ "introductory", "programming", "problem", "solving"]
word=random.choice(words)
display = ["_"] * len(word)

guesses=[]
remaining_guesses = 5

while "_" in display and remaining_guesses > 0:
    print( " ".join(display))
    print ('Guessed letters: ', guesses)
    print('Remaining guesses = ', remaining_guesses)
    guess =input ('Enter your guess letter: ').lower()

    if guess in guesses:
        print('You have already guessed that letter. Please enter another letter: ')
    elif guess in word:
        for i in range(len(word)):
            if word[i]== guess:
                display[i]=guess
                print('Correct guess.🎉🎉 Please enter another letter: ')
    else:
        remaining_guesses-=1
        print('Incorect guess.😢 Please enter another letter: ')
        guesses.append(guess)

if "_" not in display:
    print( " ".join(display))
    print("Congratulaitons🎉🎉 . You have guessed the word correctly.")

else:
    print("Sorry you have ran out of guesses.The word was", word+".")