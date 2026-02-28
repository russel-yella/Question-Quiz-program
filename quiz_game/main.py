from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for item in question_data:
    question = item["question"]
    answer = item["correct_answer"]
    question_model = Question(question,answer)
    question_bank.append(question_model)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your score is {quiz.score}/{len(quiz.quest_list)}")


