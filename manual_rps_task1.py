import random
class Rps:
     #Computer choice
    #def _get_computer_choice():
        List_1 = ['rock', 'paper', 'scissor']
        computer_choice = random.choice(List_1)
        print(computer_choice)
      # Player choice
    #def _get_user_choice():
        player = input('player ''write your choice: ')
        list_2 = ['rock', 'paper', 'scissor']
        print(player)

        while player == computer_choice:
            print('It is a Tie.')
            break
        else:
            if player == 'Scissor' and computer_choice =='Paper':
                print('Player Wins')
            elif player == 'Scissor' and computer_choice =='Rock':
                print('Player_2 Wins')
            else: 
                player == 'Scissor' and computer_choice =='Scissor'
                print('It is a Tie')
            
