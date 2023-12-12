import Question
# print(questions[0]['no'],". ",end='')
# print(questions[0]['question'])
# print(f"\nA) {questions[0]['A']}")
# print(f"\nB) {questions[0]['B']}")
# print(f"\nC) {questions[0]['C']}")
# print(f"\nD) {questions[0]['D']}")
questions=Question.questions
no=len(questions)

score=0
for i in range(no):
    Answer=''
    # print(questions[i])
    print("\n",questions[i]['no'],". ",end='')
    print(questions[i]['question'])
    print(f"\nA) {questions[i]['A']}")
    print(f"\nB) {questions[i]['B']}")
    print(f"\nC) {questions[i]['C']}")
    print(f"\nD) {questions[i]['D']}")
    Answer=input("Enter Ans ")
    print(Answer)
    ans=questions[i]['ans']
    if  Answer.upper() == questions[i]['ans']:
        score+=1
        print(" Your Ans is correct \n")
        
    else:
        print("\n Your Ans is Wrong  ! ")
        print(f"Write Answer : {questions[i]['ans']} ) {questions[i][ans]}")

    

print(f" \n |||||||||||||||||||||||||||||| SCORE : {score}/{no}  |||||||||||||||||||||||||||||||||")