from os import system, name
from time import sleep

guess_no = 13
guess = []

# Entering the word for guessing
word = list(input("Enter the Letter : ").lower())
success_count = len(word)
failed = len(word)
guess_word = []
print("-------------------------------------------------------")

#clearing the screen
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


sleep(2)
clear()




#Showing the blank spaces for guessing
for ch in word:
    guess_word.append("_")
print(f"The word has {len(word)} letters.")
print(guess_word)
print("-------------------------------------------------------")

#game starts
while guess_no != 0:
    print(f'you have {guess_no} guess left')
    sleep(2)
    # clear()
    ch = input("Try Your Guess (1 Letter at a time): ")
    if ch not in guess:
        guess.append(ch)
    if ch in word:
        print(f"Yes !!! Your guess is correct. '{ch}' is in the given word")
        for n in range(word.count(ch)):
            guess_word[word.index(ch)] = ch
            word[word.index(ch)] = '*'
            success_count -= 1
    else:

        # failed -= 1
        if ch in guess_word and ch in guess:
            sleep(1)
            print("-------------------------------------------------------")
            print(f"Pressed Word '{ch}' is already entered. TRY ANOTHER !!!!!!!")
            print("-------------------------------------------------------")
            continue
        sleep(1)
        print(f"Pressed Word '{ch}' is not  present in the given word.")
        guess_no -= 1
    # if failed == 0:
    #     break
    sleep(1)
    print("\n",guess_word)
    print("-------------------------------------------------------")
    print(f"your guesses: ", guess)
    if success_count == 0:
        sleep(0.5)
        clear()
        print("You Won")
        print("The End")
        break
else:
    sleep(0.5)
    clear()
    print("""
You failed...........
Try Again !!!!
""")