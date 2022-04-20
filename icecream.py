from time import sleep

hints = ["Some people think this flavor is bitter", "It is a classic flavor", "Dogs are allergic"]
answer = 'chocolate' 
def ask_flavor():
    k = 0 
    global answer #because variable is set outside function
    for loop in hints:
        sleep(2)
        x = input('Guess my favorite ice cream flavor:')
        if x == answer: #if guess equals flavor
            print('You guessed it right!')
            break
        else:
            print('Your guess was wrong!')
            sleep(2)
            print(hints[k])
            k = k+1 #runs through list of hints

ask_flavor()