import random

def Welcome():
    print("*Welcome to random number guess.*\n")

def finish(num, count):
    print("Good Game!")
    print(f"The number was {num} and you found it in {count} guess{"es" if count > 1 else ""}")
    answer = input("\n\nDo you want to resume?(Y/N): ")
    if answer.lower() == "y":
        return True
    else:
        return False

def win(cnum, unum):
    return cnum == unum

def answer(cnum, unum):
    if cnum > unum:
        return("'Your guess is smaller.'\n")
    if cnum < unum:
        return("'Your guess is greater.'\n")
    return "You Win!!!"

def get_guess():
    while True:
        try:
            unum = int(input("\nWhat is your guess?"))
            if unum == int(unum):
                break
        except ValueError:
            print("Bro, I need a number.\n")
            continue
    return unum

Welcome()
continue_playing = True
least = 1
end = 10
change = input("The default mode has a range from 1 to 10.\n\
If you want to change it, enter 'H'.\
Otherwise, just press Enter.\n\
(Note: If you change this setting, you won’t be able to change it again unless you restart the game.)\n\
H or Enter:")
if change == "H":
    least = input("Enter the lower number: ")
    end = input("Enter the bigger number: ")
else:
    pass
while continue_playing:
    cnum = random.randint(int(least), int(end)+1)
    unum = 0
    count = 0
    while not win(cnum, unum):
        unum = get_guess()
        count += 1
        print(answer(cnum, unum))
        
    continue_playing = finish(cnum, count)

    

