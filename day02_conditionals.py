# Inputs
number_grade = int(input('Enter your numeric grade: '))
# Conditional
if not (0 <= number_grade <= 100):
    print('Invalid grade. Please enter a value between 0 and 100.')
elif number_grade >= 90:
    letter_grade = 'A'
    print(f' You earned a {letter_grade}. Good job!')
elif 80 <= number_grade <= 89:
    letter_grade = 'B'
    print(f' You earned a {letter_grade}. Good job!')
elif 70 <= number_grade <= 79:
    letter_grade = 'C'
    print(f' You earned a {letter_grade}. Good job!')
elif 60 <= number_grade <= 69:
    letter_grade = 'D'
    print(f' You earned a {letter_grade}. Good job!')
else:
    letter_grade = 'F'
    print(f' You earned a {letter_grade}. Try again.')