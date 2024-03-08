print('Welcome to the Python Basics Quiz')
answer = input('Are you ready to play the Quiz? (yes/no): ').strip().lower()
score = 0
total_questions = 3

if answer == 'yes':
    print("\nQuestion 1: What symbol do you use to start a comment in Python?")
    user_answer = input("Your answer: ").strip()
    if user_answer == '#':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    print("\nQuestion 2: How do you print 'Hello, World!' in Python?")
    user_answer = input("Your answer: ").strip()
    if user_answer == 'print("Hello, World!")' or 'print("hello, world")' :
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    print("\nQuestion 3: What is the keyword used to define a function in Python?")
    user_answer = input("Your answer: ").strip()
    if user_answer == 'def':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

print('\nThank you for playing this small quiz game!')
print('You answered', score, "out of", total_questions, "questions correctly.")
percentage_correct = (score / total_questions) * 100
print('Percentage Correct:', percentage_correct, '%')
print('BYE!')
