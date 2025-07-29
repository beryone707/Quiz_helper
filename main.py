from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank=[]
for list in question_data:
    q_text=list["text"]
    q_answer=list["answer"]
    question=Question(text_q=q_text,answer_q=q_answer)
    #question = Question(list["text"],list["answer"]) aynı şey
    question_bank.append(question)

quiz=QuizBrain(q_list=question_bank)

while quiz.still_have_questions():
    quiz.next_question()
