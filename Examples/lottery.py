import random

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

def draw_winner():
    winner = []
    for i in range(4):
        winner.append(str(random.choice(lottery)))
    return winner

print("Winner:")
print(''.join(sorted(draw_winner())))

my_ticket = ['2', '2', 'e', 'b']

print(f"My ticket: {''.join(my_ticket)}")

i_won = False
draws = 0

while not i_won:
    draws += 1
    winner = draw_winner()
    print(f"{draws}. winner: {''.join(sorted(winner))}")
    if ''.join(sorted(winner)) == ''.join(sorted(my_ticket)):
        i_won = True
        print("I won!")
    if draws > 10000:
        print("10000 draws passed, exit!")
        break

print(f"My ticket won after {draws} draws!")


