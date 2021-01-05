# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    if False:

        alien_0 = {'color': 'green'}
        print(f"The alien is {alien_0['color']}.")

        alien_0['color'] = 'yellow'
        print(f"The alien is now {alien_0['color']}.")

        alien_0['points'] = 5

        alien_0['x_position'] = 0
        alien_0['y_position'] = 25
        alien_0['speed'] = 'medium'
        print(f"Original position: {alien_0['x_position']}")

        # Move the alien to the right
        # Determine how far to move the alien based on its current speed
        if alien_0['speed'] == 'slow':
            x_increment = 1
        elif alien_0['speed'] == 'medium':
            x_increment = 2
        else:
            # This must be a fast alien
            x_increment = 3

        alien_0['x_position'] += x_increment

        print(f"New position: {alien_0['x_position']}")

        print(alien_0)

        del alien_0['points']

        print(alien_0)

        point_value = alien_0.get('points', 'No point value assigned.')
        print(point_value)

        for key, value in alien_0.items():
            print(f"\nKey: {key}")
            print(f"Value: {value}")

        aliens = []

        for alien_number in range(30):
            color = ''
            points = None
            speed = ''
            if alien_number % 3 == 0:
                color = 'green'
                points = 5
                speed = 'slow'
            elif alien_number % 3 == 1:
                color = 'yellow'
                points = 10
                speed = 'medium'
            else:
                color = 'red'
                points = 5
                speed = 'fast'
            new_alien = {
                'color': color,
                'points': points,
                'speed': speed
            }
            aliens.append(new_alien)

        print(aliens)
        print(f"Total number of aliens: {len(aliens)}")

# car = input("What kind of rental car would you like? ")
# print(f"Let me see if I cab find you a {car}")

guest_number = input("How many people are there in your group? ")
if int(guest_number) > 8:
    print("You have to wait for a table")
else:
    print("Your table is ready5")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
