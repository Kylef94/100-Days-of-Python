from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
Q_FONT = ('Arial', '20', 'italic')

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.user_score = 0
        self.window = Tk()
        self.window.title('Quizzle')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20, height=700, width=350)

        self.canvas = Canvas(self.window, width=300, height=250,background='white')
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.question_text = self.canvas.create_text(150, 125, text='TEST', width=280, font=Q_FONT)
        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        true_button_img = PhotoImage(file=r'.\images\true.png')
        false_button_img = PhotoImage(file=r'.\images\false.png')

        self.true_button = Button(image=true_button_img, command=self.true_ans)
        self.true_button.grid(column=0, row=2, pady=20, padx=20)
        self.false_button = Button(image=false_button_img, command=self.false_ans)
        self.false_button.grid(column=1, row=2, pady=20, padx=20)

        self.get_nextq()
        self.window.mainloop()

    def get_nextq(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score {self.quiz.user_score}')
            q_text = self.quiz.nextq()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_ans(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def false_ans(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_nextq)