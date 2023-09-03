import time

THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizeInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.root=Tk()
        self.root.title('MY QUIZE APP')
        self.root.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label=Label(text='Score:0',fg='white',bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas=Canvas(width=380,height=250,bg='white')
        self.question_text=self.canvas.create_text(200,125,width=200,text='some  question text',
                                                   fill=THEME_COLOR,
                                                   font=('Arial',15,'italic'))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        #Add butttons

        true_image=PhotoImage(file='images/true.png')
        self.true_button=Button(image=true_image,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)

        false_image = PhotoImage(file='images/false.png')
        self.true_button = Button(image=false_image, highlightthickness=0,command=self.false_pressed)
        self.true_button.grid(row=2, column=1)

        self.get_next_question()
        self.root.mainloop()



    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f'score:{self.quiz.score}')
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text)


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.root.after(1000,self.get_next_question)
