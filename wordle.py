import random

WORD_LENGTH = 5
GUESS_LIMIT = 6
SOURCE_FILE = 'wordlist.txt'
OBSCURITY_THRESHOLD = 30000  # Difficulty setting
                   

with open(SOURCE_FILE, 'r') as sourceFile:
    reader = list(sourceFile)

# Build a list for all acceptable words and a separate one for words that
# can be used as answers
allWords, answerList = ([], [])
for counter, line in enumerate(reader):
    currentWord = line.strip().upper()
    if len(currentWord) == WORD_LENGTH:
        allWords.append(currentWord)
        if counter < OBSCURITY_THRESHOLD:
            answerList.append(currentWord)

def main():
    """Runs games infinitely until the player decides to stop."""
    print('Welcome to my Wordle clone!')
    while True:
        result = runGame()
        if result:
            print('Nope, better luck next time.')
            print(f'The word was {result}')
        else:
            print('WINNER!')
        
        response = input('Play again? Y/N\n')
        if response:
            if response.upper()[0] != 'Y':
                break
    print('Thanks for playing')

def runGame():
    """Runs a single game."""
    # Assign a word as the correct answer
    answer = random.choice(answerList).upper()
    board = []

    print(f'Take a guess. The answer is {WORD_LENGTH} letters long:')

    while True:
        # Accept a guess from the user
        try:
            guess = takeAnswer()
        except KeyboardInterrupt:
            return answer

        # Add the newest line to the board and print
        newRow = [guess, ' '] + generateReturn(guess, answer)
        newRow = ''.join(newRow)
        board.append(newRow)
        boardToPrint = '\n'.join(board)
        print('\n' + boardToPrint + '\n')

        if guess == answer:
            # Victory. Return empty string
            return ''
        elif len(board) == GUESS_LIMIT:
            # Defeat. Return the correct answer
            return answer
        else:
            # Print number of remaining guesses and invite to guess again
            guessesLeft = GUESS_LIMIT - len(board)
            print(f'{guessesLeft} guesses left.')
            print('Guess again:')


def takeAnswer():
    """Takes and vets user input and returns the result."""
    while True:
        response = input().strip().upper()
        if len(response) != WORD_LENGTH:
            print(f'Guesses need to be {WORD_LENGTH} letters long.')
        elif not response in allWords:
            print(f"{response} isn't in the dictionary.")
        else:
            return response
        print('Try again:')


def generateReturn(guessedWord, correctAnswer):
    """Generates a new board row in the form of a list"""
    output = []

    # Compare the guess to the answer
    tildaLog = {}
    for i in range(WORD_LENGTH):
        if correctAnswer[i] == guessedWord[i]:
            output.append(correctAnswer[i])
            tildaLog.setdefault(guessedWord[i], 0)
            tildaLog[guessedWord[i]] += 1
        elif guessedWord[i] in correctAnswer:
            output.append('~')
            tildaLog.setdefault(guessedWord[i], 0)
            tildaLog[guessedWord[i]] += 1
        else:
            output.append('.')

    # Check for and remove ~s in excess of the letters they represent
    for i in range(WORD_LENGTH - 1, -1, -1):
        if output[i] == '~':
            if tildaLog[guessedWord[i]] > \
               correctAnswer.count(guessedWord[i]):
                output[i] = '.'
                tildaLog[guessedWord[i]] -= 1

    return output


if __name__ == '__main__':
    main()
