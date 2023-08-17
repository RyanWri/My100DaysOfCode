from tkinter import *
import os

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzlire")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label_score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.label_score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="assadsa", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_button = PhotoImage(file=self.find_image("true.png"))
        self.true_button = Button(image=true_button, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        false_button = PhotoImage(file=self.find_image("false.png"))
        self.false_button=Button(image=false_button, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        self.window.mainloop()

    def find_image(self, filename):
        base_folder=os.path.dirname(__file__)
        image_path=os.path.join(base_folder, f'images/{filename}')
        return image_path
