from random import randint
import hang_man_draws
import os
#return the word randomly
def get_a_word():
    print("x")
    x = ''
    with open("words.txt",'r') as f:
        #O(n) depend on the len of the file
        for word in f :
            x+=word
    list = x.split("\n")
    index = randint(0,len(list)-1)

    return list[index]



def play_game():
    vidas = 8
    state_of_the_draw=0
    status="Start the game"
    #get the word randomly
    word = get_a_word()
    #Start the list
    word_in_list_format = ["__ " for x in word]
    while vidas >0:
        os.system("clear")
        print(status)
        print("Lives: {}".format(vidas))
        print(hang_man_draws.hangman[state_of_the_draw])
        print("".join(word_in_list_format))
        answer = input("wich word: ")
        if "".join(word_in_list_format) == "".join(word):
            print("Congratulations you win the game")
            return
        elif answer in word and answer not in word_in_list_format:
            word_in_list_format[word.index(answer)] = answer
            status ="Good one"
        else:
            status="incorrect answer"
            vidas-=1
    print("You lose the game , the correct answer was: {}".format("".join(word)))



def display_words():
    with open("words.txt",'r') as f:
        print("""
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        █░▄▄▄█░▄▄▀█░▄▀▄░█░▄▄███░███░█▀▄▄▀█░▄▄▀█░▄▀█░▄▄
        █░█▄▀█░▀▀░█░█▄█░█░▄▄███▄▀░▀▄█░██░█░▀▀▄█░█░█▄▄▀
        █▄▄▄▄█▄██▄█▄███▄█▄▄▄████▄█▄███▄▄██▄█▄▄█▄▄██▄▄▄
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        """)
        for word in f :
            print(5*" "+word)
    f.close()
    return

def add_new_word():
    with open("words.txt","a")as f:
        while True:
            word= input("Write the word you like to add: ")
            f.write(word.lower()+'\n')
            #add another word
            cont=input("you want to add another word ? yes/no: ")
            if cont =='yes':
                pass
            elif cont == 'no':
                return False
            else:
                print("no valid option ")
    f.close()
    return



def display_menu():
    menu="""
            1.- Play a new game
            2.- Add new words
            3.- Display all the words
            4.- Exit
    """
    print(menu)

def main():
    # Initial message
    print("""
        ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄    ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄
        █  █ █  █       █  █  █ █       █  █  █▄█  █       █  █  █ █
        █  █▄█  █   ▄   █   █▄█ █   ▄▄▄▄█  █       █   ▄   █   █▄█ █
        █       █  █▄█  █       █  █  ▄▄   █       █  █▄█  █       █
        █   ▄   █       █  ▄    █  █ █  █  █       █       █  ▄    █
        █  █ █  █   ▄   █ █ █   █  █▄▄█ █  █ ██▄██ █   ▄   █ █ █   █
        █▄▄█ █▄▄█▄▄█ █▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█  █▄█   █▄█▄▄█ █▄▄█▄█  █▄▄█
    """)
    while True:
        #display the menu
        display_menu()
        option = int(input("Select an option: "))
        #start a new game
        if option == 1:
            play_game()
        #Add new words to the game
        elif  option == 2:
            # pritn("Hola")
            add_new_word()
        #Display all the words
        elif option ==3:
            display_words()
        #End Game
        elif   option == 4:
            print("""
              ______________
             |  __________  |
             | | see youu | |
             | |__________| |
             |______________|
            """)
            return False
        else:
            print("this option is not valid ")

if __name__ == '__main__':
    main()
