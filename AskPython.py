print('Welcome to python Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What symbol do you use to start a comment in Python?')
    if answer.lower()=='#':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: How do you print 'Hello, World!' in Python? ')
    if answer.lower()=='print("hello world")':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What is the keyword used to define a function in Python?')
    if answer.lower()=='def':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, ',score,"questions right!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('Thankyou!')
