from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

Question_bank = []
for Questions in question_data:
    question_text = Questions["text"]
    question_answer = Questions["answer"]
    new_question = Question(question_text, question_answer)
    Question_bank.append(new_question)

quiz = QuizBrain(Question_bank)

quizscreen = QuizInterface(quiz)

# while quiz.still_have_questions():
#     quiz.next_question()
