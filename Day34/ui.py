from tkinter import *
import os
from typing import Self
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    
    @staticmethod
    def find_image(filename):
        base_folder=os.path.dirname(__file__)
        image_path=os.path.join(base_folder, f'images/{filename}')
        return image_path
    
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzlire")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label_score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.label_score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,width=280, text="assadsa", fill=THEME_COLOR, font=("Arial", 16, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_button = PhotoImage(file=self.find_image("true.png"))
        self.true_button = Button(image=true_button, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        false_button = PhotoImage(file=self.find_image("false.png"))
        self.false_button=Button(image=false_button, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self) -> Self:
        self.canvas.config(bg="white")
        if self.brain.still_has_questions():
            self.label_score.config(text=f'Score: {self.brain.score}')
            q_text = self.brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self) -> None:
        self.give_feedback(self.brain.check_answer("True"))
    
    def false_pressed(self) -> None:
        self.give_feedback(self.brain.check_answer("False"))

    def give_feedback(self, is_right: bool) -> None:
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)