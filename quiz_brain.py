class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0

    def still_have_questions(self):
        if self.question_number < len(self.question_list) :
            return True
        else:
            False

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"Q.{self.question_number}. {current_question.text} Answer:(True/False)")
        question_answer=current_question.answer
        self.check_answer(user_answer,question_answer)

    def check_answer(self, user_answer, checked_answer):
            if user_answer.lower() == checked_answer.lower():
                self.score+=1
                print("You got it right")
            else:
                print("You got it wrong")
            print(f"The correct answer is {checked_answer}")
            print(f"Your score is: {self.score}/{self.question_number} ")
            print("\n"*5)
            if 