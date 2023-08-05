game = {'1':' ','2':' ',
        '3':' ','4':' ',
        '5':' ','6':' ',
        '7':' ','8':' ',
        '9':' '}

print("7|8|9")
print("-----")
print("4|5|6")
print("-----")
print("1|2|3")

def game_board():
    print(game['7'],'|',game['8'],'|',game['9'])
    print(f'---------')
    print(game['4'],'|',game['5'],'|',game['6'])
    print(f'---------')
    print(game['1'],'|',game['2'],'|',game['3'])


def users_chracters():
    global user1_character
    global user2_character
    while True:
        user1_character = input('Enter your character(X or O): ').upper()
        if user1_character in ('X','O'):
            if user1_character == 'X':
                user2_character = 'O'
            if user1_character == 'O':
                user2_character = 'X'
            break
        else:
            print('Invalid input !')
            continue
     

game_keys = ['1','2','3','4','5','6','7','8','9'] 
user1_combination = ''
def user1_input():
    while True:
        user1_input = input('Enter your choice [Player 1]: ')
        if user1_input not in game.keys():
            print("Wrong choice.")
            continue
        else:
            if user1_input in game_keys:
                game_keys.remove(user1_input)
                game[user1_input] = user1_character
                global user1_combination
                user1_combination += user1_input
                break
            else:
                print('Invalid key!')
                continue
        

user2_combination = ''
def user2_input():
    while True:
        user2_input = input('Enter your choice [Player 2]: ')
        if user2_input not in game.keys():
            print("Wrong choice.")
            continue
        else:
            if user2_input in game_keys:
                game_keys.remove(user2_input)
                game[user2_input] = user2_character
                global user2_combination
                user2_combination += user2_input
                break
            else:
                print('Invalid key!')
                continue
        
        
        
users_chracters()
win_combinations = ['741','852','963','789','456','123','753','951']
i=0  
win = 0
while i != 9:
    if i % 2 == 0:user1_input();game_board() 
    if i % 2 == 1:user2_input();game_board()
    for combinations in win_combinations:
        if combinations[0] in user1_combination and\
           combinations[1] in user1_combination and\
           combinations[2] in user1_combination :
               print('Player 1 wins !')
               i = 8
               win = 1
               break
                   
        elif combinations[0] in user2_combination and\
            combinations[1] in user2_combination and\
            combinations[2] in user2_combination :
                print('Player 2 wins !')
                i = 8
                win = 1
                break
        else:
            pass
    i +=1

if win == 0:
    print("It's a Draw !")
