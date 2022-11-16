import random
class Rps:
    def __init__(self,computer,user,num_try=3):
        self.computer = computer
        self.user = user
        self.num_try = num_try
     #Computer choice
    def get_computer_choice():
        List_1 = ['rock', 'paper', 'scissor']
        computer = random.choice(List_1)
        print(computer)
    get_computer_choice()
      # Player choice
    def get_user_choice():
        user = input('User ''write your choice: ')
        list_2 = ['rock', 'paper', 'scissor']
        print(user)
    get_user_choice()
    
    def get_winner(computer,user):
        
        while computer == user:
            print('It is a Tie.')
            break
        else:
            if computer == 'scissor' and user =='paper':
                print('Computer Wins')
            elif computer == 'scissor' and user =='rock':
                print('Userer Wins')
            elif computer == 'rock' and user == 'paper':
                print('User Wins')
            elif computer == 'rock' and user == 'scissor':
                print('Computer Wins')
            elif computer == 'paper' and user == 'rock':
                print('Computer Wins')
            else:
                computer == 'paper' and user == 'scissor'
                print('User Wins')
    get_winner('computer','user')

    def _play_game():
        game = Rps 
       
    get_computer_choice()
    get_user_choice()
    get_winner('computer','user')
  
        
