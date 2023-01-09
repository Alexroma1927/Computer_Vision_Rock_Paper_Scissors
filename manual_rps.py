import random
class Rps:
    num_trys = 3
    
    def get_computer_choice(self):
        List_1 = ['rock', 'paper', 'scissor']
        computer = random.choice(List_1)
        return computer
    def get_user_choice(self):
        user = input('User ''write your choice: ')
        list_2 = ['rock', 'paper', 'scissor']
        return user
    
    def get_winner(self,computer,user):
       
        if computer == user:
            print('It is a Tie.') 
             
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
    def _play_game():
        game = Rps 
            
        

Rps_1 = Rps()
new_computer_choice = Rps_1.get_computer_choice()
new_user_choice = Rps_1.get_user_choice()
Rps_1.get_winner(new_computer_choice , new_user_choice)
