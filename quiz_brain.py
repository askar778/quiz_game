import html


class QuizBrain:
    def __init__(self, question_list):
        self.current_answer = None
        self.current_question = None
        self.question_list = question_list
        self.question_number = 1
        self.score = 0

    def still_have_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = (self.question_list[self.question_number]).text
        self.current_answer = (self.question_list[self.question_number]).answer.lower()
        q_text = html.unescape(self.current_question)
        self.question_number += 1
        return f"Q.{self.question_number}: {q_text}?"

    def check_answer(self):
        user_input = QuizBrain.next_question().lower()
        if user_input == self.current_answer:
            print("Correct answer")
            self.score += 1
        else:
            print("Wrong answer")
        print(f"score: {self.score}")
