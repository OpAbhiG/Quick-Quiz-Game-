print('# AskPython Quiz')
print('Welcome to the AskPython Quiz! Test your knowledge in this small quiz game.\n')

answer = input('Are you ready to play the Quiz? (yes/no): ').strip().lower()
score = 0
total_questions = 3

if answer == 'yes':
    print('\n## How to Play\n')
    print('1. Answer each question prompted in the terminal.')
    print('2. Check your score at the end of the quiz.\n')

    print('## Quiz Details\n')
    print('The quiz consists of 3 questions related to Python and AskPython.')
    print('- **Question 1:** What is your favorite programming language?')
    print('- **Question 2:** Do you follow any author on AskPython?')
    print('- **Question 3:** What is the name of your favorite website for learning Python?\n')

    print('## Scoring\n')
    print('- Each correct answer adds to your score.')
    print('- Your final score is displayed at the end of the quiz.\n')

    print('## Run the Quiz\n')
    print('```bash')
    print('python quiz.py')
    print('```\n')

    print('## Example\n')
    print('```plaintext')
    print('Welcome to AskPython Quiz')
    print('Are you ready to play the Quiz? (yes/no) :yes')
    answer = input('Question 1: What is your Favourite programming language?').strip().lower()
    if answer == 'python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer = input('Question 2: Do you follow any author on AskPython? ').strip().lower()
    if answer == 'yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer = input('Question 3: What is the name of your favourite website for learning Python?').strip().lower()
    if answer == 'askpython':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    print('Thank you for Playing this small quiz game, you attempted', score, "questions correctly!")
    mark = (score / total_questions) * 100
    print('Marks obtained:', mark, '%')
    print('BYE!')
