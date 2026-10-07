import pgzrun
TITLE="quiz master"
WIDTH=870
HEIGHT=700
Marquee_box=Rect(0,10,880,80)
question_box=Rect(20,100,650,150)
timer_box=Rect(700,100,150,150)
a1_box=Rect(20,270,300,150)
a2_box=Rect(370,270,300,150)
a3_box=Rect(20,450,300,150)
a4_box=Rect(370,450,300,150)
skip_box=Rect(700,270,150,330)

answer_boxes=[a1_box,a2_box,a3_box,a4_box]

score=0
timeleft=10
question_file_name="question.txt"
marquee_message=""
is_game_over=False
questions=[]
question_count=0
question_index=0

def draw():
    global marquee_message
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(Marquee_box,"pink")
    screen.draw.filled_rect(question_box,"yellow")
    screen.draw.filled_rect(timer_box,"pink")
    screen.draw.filled_rect(skip_box,"yellow")
    for i in answer_boxes:
        screen.draw.filled_rect(i,"blue")

    marquee_message="Welcome to Quiz Master"+f"Q:{question_index} of {question_count}"

    screen.draw.textbox(marquee_message,Marquee_box,color="yellow")

    screen.draw.textbox(
        str(timeleft),
        timer_box,
        color="pink"
    )
    screen.draw.textbox(
        "Skip",
        skip_box,
        color="yellow",
        angle=-90
    )
    screen.draw.textbox(
        question[0].strip(),
        question_box,
        color="pink",
        shadow=(0.5,0.5),
        scolor="yellow"
    )
    index=1
    for i in answer_boxes:
        screen.draw.textbox(question[index].strip(),i,color="pink")
        index=index+1

def update():
    move_marquee()

def read_question_file():
    global question_count,questions
    q_file=open(question_file_name,"r")
    for question in q_file:
        questions.append(question)
        question_count=question_count+1
    q_file.close()

def on_mouse_down(pos):
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index == int(question[5]):
                correct_answer()
            else:
                gameover()
    if skip_box.collidepoint(pos):
        skipquestion()


def move_marquee():
    Marquee_box.x=Marquee_box.x+2
    if Marquee_box.left >870:
        Marquee_box.right=0
    

def read_next_question():
    global question_index
    question_index=question_index+1
    return questions.pop(0).split("|")
question=read_next_question()

def correct_answer():
    global score, question, timeleft, questions
    score=score+1

    if questions:
        question=read_next_question()
        timeleft=10

    else:
        gameover()

def gameover():
    global question, timeleft, is_game_over
    message=f"Game over!\nYou got {score} questions correct!"
    question=[message,"-","-","-","-","-"]
    timeleft=0
    is_game_over=True

def skipquestion():
    global question, timeleft

    if questions and not  is_game_over:
        question=read_next_question()
        timeleft=10

    else:
        gameover()

def update_time_left():
    global timeleft
    if timeleft:
        timeleft=timeleft-1

    else:
        gameover

clock.schedule_interval(update_time_left,1)
read_question_file()
question=read_next_question()

    
pgzrun.go()
