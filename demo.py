import tkinter as tk
from tkinter import ttk
from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self, master):
        self.master = master
        master.title("Cool Spell Checker App")
        master.geometry("600x400")  # Set the initial size of the window
        master.configure(bg="lightblue")  # Set the background color of the main window

        self.style = ttk.Style()
        self.style.theme_use("clam")  # You can experiment with other available themes

        # Button style for Check and Correct button
        self.style.configure("TButton",
                             padding=(10, 5),
                             font=('Arial', 14),
                             background="#4CAF50",  # Green color
                             foreground="white",  # Text color
                             )

        self.label = ttk.Label(master, text="Enter a sentence:")
        self.label.pack(pady=10)

        self.user_input = ttk.Entry(master, font=('Arial', 14))
        self.user_input.pack(pady=10)

        self.check_button = ttk.Button(master, text="Check and Correct", command=self.check_and_correct)
        self.check_button.pack(pady=10)

        self.result_label = ttk.Label(master, text="", font=('Arial', 14))
        self.result_label.pack(pady=10)

        self.previous_entries_label = ttk.Label(master, text="Previous Entries:")
        self.previous_entries_label.pack(pady=10)

        # Customize the appearance of the Text widget
        self.previous_entries_text = tk.Text(master, height=5, width=40, font=('Arial', 12), borderwidth=2, relief="solid", wrap="word", bg="lightyellow")
        self.previous_entries_text.pack(pady=10)

        self.clear_button = ttk.Button(master, text="Clear", command=self.clear_entries)
        self.clear_button.pack(pady=10)

        self.previous_entries = []

    def check_and_correct(self):
        user_input = self.user_input.get()

        # Check for an empty input
        if not user_input:
            self.result_label.config(text="Please enter a sentence.")
            return

        corrected_sentence = self.correct_spelling_in_sentence(user_input)

        # Check if the input sentence is correct
        if user_input.lower() == corrected_sentence.lower():
            self.result_label.config(text="The sentence is correct.")
        else:
            # Display corrected sentence
            self.result_label.config(text=f"Corrected Sentence: {corrected_sentence}")

            # Store both the original and corrected sentences
            self.previous_entries.append((user_input, corrected_sentence))
            self.update_previous_entries()

    def correct_spelling_in_sentence(self, sentence):
        spell = SpellChecker()
        words = sentence.split()
        corrected_words = [spell.correction(word) for word in words]
        corrected_sentence = ' '.join(corrected_words)
        return corrected_sentence

    def update_previous_entries(self):
        # Limit the number of previous entries to 5, for example
        self.previous_entries = self.previous_entries[-5:]

        # Display both original and corrected sentences in the text widget
        previous_entries_text = "\n".join([f"Original: {entry[0]}\nCorrected: {entry[1]}\n" for entry in self.previous_entries])
        self.previous_entries_text.delete("1.0", tk.END)
        self.previous_entries_text.insert(tk.END, previous_entries_text)

    def clear_entries(self):
        # Clear the list of previous entries and update the display
        self.previous_entries = []
        self.update_previous_entries()


if __name__ == "__main__":
    root = tk.Tk()
    app = SpellCheckerApp(root)
    root.mainloop()
