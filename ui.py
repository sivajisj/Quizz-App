from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.widow = Tk()
        self.widow.title("Quizzler")
        self.widow.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(

            150,
            125,
            text="Some Question",
            fill=THEME_COLOR,
            width=280,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_image,command=self.its_right, highlightthickness=0)
        self.false_button = Button(image=false_image, command=self.its_wrong,  highlightthickness=0)
        self.true_button.grid(row=2, column=1)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()


        self.widow.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quizz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def its_right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def its_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.widow.after(1000, self.get_next_question)






