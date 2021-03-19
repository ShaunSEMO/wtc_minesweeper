import random

print("Welcome to Minesweeper! \nTo play, please enter your name, board dimensions and number of bombs \nRemeber the number of bombs cannot exceed the board dimensions.")
print("\n")

name = input("Name: ")
input_board_dim = int(input("Board dimension(Enter number only): "))
input_bomb_num = int(input("Number of bombs: "))
print('\n')

y_axis = []
x_axis = []

top_line = ""
bottom_line = ""

blocks = ''
# You may create additional functions here:

for num in range(input_board_dim+1):
    # blocks += f' {random.randint(num, input_board_dim)} |'
    blocks += f'   |'
    top_line += f'___{num}'
    bottom_line += '----'
    y_axis.append(num)
    x_axis.append(num)

def print_board(y,x):
    print(top_line)
    for i in y:
        print(f'{i}|{blocks} ')
    print(bottom_line)

print_board(y_axis, x_axis)
# Additional Functions above this comment

# Implement your Minesweeper Solution Below:



# def play(dim_size, num_bombs):
#     #Edit the code Below Here



#     pass
    #Edit the code Above Here
#play Function Ends Here


# if __name__=='__main__':
#     play()
    