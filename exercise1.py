questions=[
    {
        "no":1,
        "question":"Qustion 1 ",
        "A":"option 1",
        "B":"option 2",
        "C":"option 3",
        "D":"option 4",
        "ans":"A"
    }, 
     {
        "no":2,
        "question":"Qustion 2 ",
        "A":"option 1",
        "B":"option 2",
        "C":"option 3",
        "D":"option 4",
        "ans":"A"
    }, 
     {
        "no":3,
        "question":"Qustion 4 ",
        "A":"option 1",
        "B":"option 2",
        "C":"option 3",
        "D":"option 4",
        "ans":"A"
    }, 
     {
        "no":4,
        "question":"Qustion 5 ",
        "A":"option 1",
        "B":"option 2",
        "C":"option 3",
        "D":"option 4",
        "ans":"A"
    }, 
        {
        "no":5,
        "question":"Qustion 2 ",
        "A":"option 1",
        "B":"option 2",
        "C":"option 3",
        "D":"option 4",
        "ans":"A"
    }]

# print(questions[0]['no'],". ",end='')
# print(questions[0]['question'])
# print(f"\nA) {questions[0]['A']}")
# print(f"\nB) {questions[0]['B']}")
# print(f"\nC) {questions[0]['C']}")
# print(f"\nD) {questions[0]['D']}")
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

    if(Answer==questions[0]['ans']):
        score+=1
        print("\n Your Ans is correct \n")
        
    else:
        print("\n Your Ans is Wrong \n")
        print(f"Write Answer : {questions[i]['ans']}")

    

print(f" \n |||||||||||||||||||||||||||||| SCORE : {no}out of {score} |||||||||||||||||||||||||||||||||")