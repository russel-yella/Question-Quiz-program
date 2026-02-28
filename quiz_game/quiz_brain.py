class QuizBrain:
    def __init__(self,q_list):
        self.quest_num = 0
        self.quest_list = q_list
        self.score = 0

    #check questions are not finished
    def still_has_question(self):
        return self.quest_num < len(self.quest_list)

    #Bring up available questions and take user answers
    def next_question(self):
        curr_question = self.quest_list[self.quest_num]
        self.quest_num += 1
        user_answer= input(f"Q.{self.quest_num } {curr_question.text}, (True/False) : ")
        self.check_answer(user_answer,curr_question.answer)

    #check user answers and score
    def check_answer(self, user_answer,correct_answer ):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct")
        else:
            print("Wrong")
        print(f"Your score is {self.score}/{self.quest_num}")
