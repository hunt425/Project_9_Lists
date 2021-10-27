#####################################################
# Hunter Tysdal
# CompSci101
# Program 9 Lists
import math


def menu():
    print("1 - Add Test")
    print("2 - Remove Test")
    print("3 - Clear Tests")
    print("4 - Add Assignment")
    print("5 - Remove Assignment")
    print("6 - Clear Assignments")
    print("D - Display Scores")
    print("Q - Quit")
    return ''


options = ['1', '2', '3', '4', '5', '6', 'd', 'D', 'q', 'Q']
tests = []
assignments = []
choice = ""

while choice != 'q' and choice != 'Q':
    print(menu())

    choice = input("What do you want to do?\n")

    if choice not in options:
        print('That is not a valid option')
        continue

    # Add test score
    if choice == '1':
        add = float(input("Enter the new Test score 0-100:\n"))
        if add < 0:
            print("That is not a valid option")
            continue
        else:
            tests.append(add)

    # Remove test score
    if choice == '2':
        gone = float(input("Enter Test Score to remove 0-100:\n"))
        if gone < 0:
            print('Cannot be lower than zero')
            continue
        if gone not in tests:
            print("Could not find that score to remove")
            continue
        else:
            tests.remove(gone)
            print("Successfully removed")

    # Clear Test Score
    if choice == '3':
        print("Test Scores Successfully Cleared")
        tests.clear()

    # Add to Assignment list
    if choice == '4':
        more = float(input("Enter the new Assignment score 0-100:\n"))
        if more < 0:
            print("That is not a valid option")
            continue
        else:
            assignments.append(more)

    # Remove Assignment Score
    if choice == '5':
        detach = float(input("Enter Assignment Score to remove 0-100:\n"))
        if detach < 0:
            print("Cannot be lower than zero")
            continue
        if detach not in assignments:
            print("Could not find that score to remove")
        else:
            assignments.remove(detach)
            print("Successfully removed")

    # Clear Assignment List
    if choice == '6':
        print("Assignment Scores Successfully Cleared")
        assignments.clear()

    # Displaying Table with Statistics
    if choice == 'd' or choice == 'D':
        print('Test Scores: {}'.format(tests))
        print('Program Scores: {}'.format(assignments))
        print()
        # number of items in lists:
        length = len(tests)
        length_2 = len(assignments)

        # min and max of lists:
        if length == 0:
            minim = 'n/a'
        else:
            minim = min(tests)
            minim = '{:.1f}'.format(minim)

        if length_2 == 0:
            minim_2 = 'n/a'
        else:
            minim_2 = min(assignments)
            minim_2 = '{:.1f}'.format(minim_2)

        if length == 0:
            maxim = 'n/a'
        else:
            maxim = max(tests)
            maxim = '{:.1f}'.format(maxim)

        if length_2 == 0:
            maxim_2 = 'n/a'
        else:
            maxim_2 = max(assignments)
            maxim_2 = '{:.1f}'.format(maxim_2)

        # Find Average:
        if length == 0:
            avg = 'n/a'
        else:
            avg = sum(tests) / len(tests)
            average = avg
            avg = '{:.2f}'.format(avg)

        if length_2 == 0:
            avg_2 = 'n/a'
        else:
            avg_2 = sum(assignments) / len(assignments)
            average_2 = avg_2
            avg_2 = '{:.2f}'.format(avg_2)

        # Standard Dev:
        blank = []
        blank_2 = []
        if length == 0:
            std = 'n/a'
        else:
            for i in tests:
                trying = (i - average) ** 2
                blank.append(trying)
            almost = sum(blank) / len(tests)
            std = math.sqrt(almost)
            std = '{:.2f}'.format(std)

        if length_2 == 0:
            std_2 = 'n/a'
        else:
            for j in assignments:
                trying_2 = (j - average_2) ** 2
                blank_2.append(trying_2)
            almost_2 = sum(blank_2) / len(assignments)
            std_2 = math.sqrt(almost_2)
            std_2 = '{:.2f}'.format(std_2)

        # weighted grade:
        if length == 0:
            weight = 0.00
        else:
            weight = average * 0.6

        if length_2 == 0:
            weight_2 = 0.00
        else:
            weight_2 = average_2 * 0.4

        total = weight + weight_2

        # making the table:
        print('Type               #       min       max       avg       std')
        print('============================================================')
        print('Tests              {}       {}      {}      {}     {}'.format(length, minim, maxim, avg, std))
        print('Programs           {}       {}      {}      {}     {}'.format(length_2, minim_2, maxim_2, avg_2, std_2))

        print()
        print('The weighted scores is: {:.2f}'.format(total))
        print()

print("Thank you")