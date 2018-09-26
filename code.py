from random import choice



def rps():



    print ('Welcome to a game of rock, paper, scissors. Good luck!')

    score = 0

    count = 0

    #only print above line once

    while True:

        while count < 3:

            #player inputs their choice

            player=input('ROUND {} - Choose rock(r), paper(p) or scissors(s)?:'.format(count+1))



            while True:

                #if player doesn't enter rock, paper or scissors'

                if player=='r' or player =='rock' or player =='p' or player =='paper' or player =='scissors' or player =='s':

                    break

                    

                elif len(player) ==0:

                    print ('Are you too scared to play?')

                    player=input('rock(r), paper(p) or scissors?:')

                else:

                    player=input('rock(r), paper(p) or scissors?:')

                



   



            #computer randomly guesses either rock paper or scissors

            computer='rps'

            x=choice(computer)



            

            



            #game outcomes

            if x=='r' and player=='s' or x=='r' and player=='scissors':

                print ('You lost - I chose rock')

                score -=1

                



            if x=='r' and player=='r' or x=='r' and player=='rock':

                print ('We drew - I chose rock')



            if x=='r' and player=='p' or x=='r' and player=='paper':

                print('You won - I chose rock')

                score +=1





            if x=='p' and player=='r' or x=='p' and player=='rock':

                print ('You lost - I chose paper')

                score -=1



            if x=='p' and player=='p' or x=='p' and player=='paper':

                print ('We drew - I chose paper')



            if x=='p' and player=='s' or x=='p' and player =='scissors':

                print('You won - I chose paper')

                score +=1







            if x=='s' and player=='p' or x=='s'and player=='paper':

                print ('You lost- I chose scissors')

                score -=1



            if x=='s' and player=='s' or x=='s' and player=='scissors':

                print ('We drew - I chose scissors')



            if x=='s' and player=='r' or x=='s' and player=='rock' :

                print('You won - I chose scissors')

                score +=1



    

            count += 1





        # print results 

        print('GAME OVER: ')

        if score >0:

            print('You won!')

        elif score == 0:

            print('We drew')

        else:

            print('You lost!')

            

        #game repeats
        again=input('Would you like to play again, y/n?')
        if again == 'y':
            rps()
        else:
            pass
        print ('I hope you enjoyed the game!')
       

