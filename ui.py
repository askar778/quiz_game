from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
word_font_name = "Ariel"
word_font_size = 20
word_font_style = "italic"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=300, background="white", highlightthickness=0)
        self.false_img = PhotoImage(file="images/false.png")
        self.true_img = PhotoImage(file="images/true.png")

        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.false_button = Button(image=self.false_img, highlightthickness=0)

        self.score_text = Label(text="Score: ", fg="white", bg=THEME_COLOR)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="sample text", fill="black",
                                                     font=(word_font_name, word_font_size, word_font_style))

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        self.score_text.grid(column=1, row=0)

        self.get_next_question()

    def get_next_question(self):
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())

        self.window.mainloop()
