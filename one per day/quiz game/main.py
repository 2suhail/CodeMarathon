from data import question_data
from question_model import Question
from quiz_brain import QuizBrain



def main():

    question_bank = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    # print(question_bank)
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
    print("you've completed the quiz!")
    print(f"your score is {quiz.score}/{quiz.question_number}")

if __name__ == "__main__":
    main()
