from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
word_font_name = "Ariel"
word_font_size = 20
word_font_style = "italic"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.user_input = None
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=300, background="white", highlightthickness=0)
        self.false_img = PhotoImage(file="images/false.png")
        self.true_img = PhotoImage(file="images/true.png")
        self.time = time

        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_button)
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_button)

        self.score_text = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="sample text", fill="black",
                                                     font=(word_font_name, word_font_size, word_font_style))

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        self.score_text.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_have_questions():
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text= f"QUIZ COMPLETED\nYour Score is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button(self):
        self.user_input = "True"
        self.check_answer(user_input=self.user_input)

    def false_button(self):
        self.user_input = "False"
        self.check_answer(user_input=self.user_input)

    def check_answer(self, user_input):
        if user_input.lower() == self.quiz.current_answer.lower():
            self.quiz.score += 1
            self.score_text.config(text=f"score: {self.quiz.score}")
            self.canvas.config(bg="green")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            self.score_text.config(text=f"score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text="Wrong Answer")
            self.canvas.config(bg="red")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

        self.window.after(1000, self.get_next_question)
