# your code starts here:
questions_fp = open('PracticePython/FilesProject/questions.txt', 'r')
questions = questions_fp.readlines()
questions_fp.close()
questions = [question.strip() for question in questions]
score = 0

for problem in questions:
    q_a = problem.split('=')
    user_answer = int(input(f'{q_a[0]}='))
    if user_answer == int(q_a[1]):
        score += 1
        
result_fp = open('PracticePython/FilesProject/result.txt', 'w')
result_fp.write(f'Your final score is {score}/{len(questions)}.')
result_fp.close()