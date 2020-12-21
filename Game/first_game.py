choices = []
for pos in range(9):
    choices.append(str(pos + 1))

Is_Current_One = True #default player is player X

won = False

print('\n')
print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
print('----------')
print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
print('----------')
print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')

while not won:
    if Is_Current_One:
        print("Player X")
    else:
        print("Player O")
    
    try:
        choice = input("Enter any position you want from (1-9): \n")
        choice = int(choice.strip())

        if Is_Current_One:
            choices[choice - 1] = 'X'
        else:
            choices[choice - 1] = 'O'
        Is_Current_One = not Is_Current_One
        
    except:
        print("Please enter only valid fields from board (1-9)")
        continue

    print('\n')
    print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print('----------')
    print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print('----------')
    print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')

    for pos_x in range(3):
        pos_y = pos_x * 3

        if (choices[pos_y] == choices[pos_y + 1]) and (choices[pos_y] == choices[pos_y + 2]):
            won = True

        if (choices[pos_x] == choices[pos_x + 3]) and (choices[pos_x] == choices[pos_x + 6]):
            won = True

        if (choices[0] == choices[4] and choices[0] == choices[8]) or (choices[2] == choices[4] and choices[2] == choices[6]):
            won = True

print("Player " + str(int(Is_Current_One) + 1) + " won, Congratulations!")


