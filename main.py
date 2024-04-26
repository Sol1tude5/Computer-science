import random


#Username is a global variable so 
#I dont have to pass it as an argument to the functions
username = ''

#function to authenticate the user
def auth():
    #We return bl to use it as a condition to run the game
    bl = False
    with open('songgame/unp.txt', 'r') as f:
        un_pw = [line.strip().split(',') for line in f.readlines()]
    ch = input('Enter your username: ')

    for username, password in un_pw:
        if username == ch:
            username = ch
            psi = input('Enter your password: ')
            if password == psi:
                print('Access granted.')
                bl = True
                
            else:
                print('Access denied.')
            break
    else:
        print('Access denied.')

    return bl

#main function to run the game
def main():
    print("\nYou may guess twice to get the right song.")
    with open('songgame/SongnArtist.txt', 'r') as f:
        lines = f.readlines()
        #shuffle the lines to get a random song
        random.shuffle(lines)
        #iterate through the lines
        for line in lines:
            artist, song = line.strip().split(',')
            print("Artist:", artist)
            print("Song's first letters:", ' '.join(word[0] for word in song.split()))
            ut = str(input("Enter the song: "))
            if ut.lower() == song.lower():
                print("\nCongratulations! You guessed the right song.")
                update_score(3)
            else:
                print("Sorry, wrong guess. Try again.")
                wg = 1
                while wg < 2:
                    ut = str(input("Enter the song: "))
                    if ut.lower() == song.lower():
                        print("\nCongratulations! You guessed the right song.")
                        update_score(1)
                        break
                    else:
                        wg += 1
                else:
                    print("\nSorry, wrong guess. The correct song was:", song)
                    game_end()
                    return

#function to update the score
def update_score(score):
    with open('scores.txt', 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if username in line:
                lines[i] = f"{username},{score}\n"
                break
        else:
            lines.append(f"{username},{score}\n")
        f.seek(0)
        f.writelines(lines)
    
#function to end the game
def game_end():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if username in line:
                score = line.strip().split(',')[1]
                break
        else:
            score = 0
    print("Game Over!")
    print("Your score is:", score,"Thank you for playing.")

#run the game only if authentication is passed
if auth():
    main()
