import tkinter as tk
import random
from tkinter import font as tkFont

class RockPaperScissorsGUI:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game 🎮")
        self.root.geometry("500x650") # Made window slightly taller
        self.root.resizable(False, False) # Prevents resizing

        # --- Colors & Fonts ---
        self.BG_COLOR = "#2C3E50"       # Dark blue-gray
        self.TEXT_COLOR = "#ECF0F1"   # Light gray/white
        self.BTN_FRAME_BG = "#34495E" # Slightly lighter gray-blue
        self.ROCK_COLOR = "#E74C3C"   # Red
        self.PAPER_COLOR = "#3498DB"  # Blue
        self.SCISSORS_COLOR = "#F1C40F" # Yellow
        self.RESET_COLOR = "#95A5A6"  # Gray
        self.EXIT_COLOR = "#E74C3C"   # Red
        
        self.TITLE_FONT = tkFont.Font(family="Segoe UI", size=24, weight="bold")
        self.BATTLE_FONT = tkFont.Font(family="Segoe UI", size=48, weight="bold")
        self.RESULT_FONT = tkFont.Font(family="Segoe UI", size=18, weight="bold")
        self.SCORE_FONT = tkFont.Font(family="Segoe UI", size=14)
        self.BUTTON_FONT = tkFont.Font(family="Segoe UI", size=24, weight="bold")

        self.root.config(bg=self.BG_COLOR)

        # --- Game Variables ---
        self.user_score = 0
        self.computer_score = 0
        self.choices = ["Rock", "Paper", "Scissors"]
        self.emoji_map = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}
        
        # --- Create UI Elements ---
        self.create_widgets()

    def show_popup(self, message, color):
        """Creates a temporary, centered popup to show the result."""
        
        # Create a new Toplevel window (a popup)
        popup = tk.Toplevel(self.root)
        popup.overrideredirect(True) # Removes title bar and borders
        popup.config(bg=color, relief="solid", borderwidth=3, background=color)

        # Style the message label
        popup_font = tkFont.Font(family="Segoe UI", size=18, weight="bold")
        label = tk.Label(popup, text=message, font=popup_font, 
                         bg=color, fg=self.TEXT_COLOR, padx=30, pady=20)
        label.pack()

        # --- Logic to center the popup on the main window ---
        popup.update_idletasks() # Let tkinter calculate the popup's size

        main_x = self.root.winfo_x()
        main_y = self.root.winfo_y()
        main_w = self.root.winfo_width()
        main_h = self.root.winfo_height()
        
        pop_w = popup.winfo_width()
        pop_h = popup.winfo_height()
        
        # Calculate position
        pos_x = main_x + (main_w // 2) - (pop_w // 2)
        pos_y = main_y + (main_h // 2) - (pop_h // 2)
        
        popup.geometry(f"+{pos_x}+{pos_y}")
        # --- End Centering Logic ---

        # Set the timer to destroy the popup after 1.2 seconds (1200 ms)
        # 1 second is often too fast to read
        popup.after(500, popup.destroy)


    def create_widgets(self):
        # --- Title ---
        title_label = tk.Label(self.root, text="Rock Paper Scissors", font=self.TITLE_FONT, bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        title_label.pack(pady=20)

        # --- Battle Display ---
        # Shows the choices (e.g., 🪨 vs 📄)
        self.battle_display_label = tk.Label(self.root, text="VS", font=self.BATTLE_FONT, bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        self.battle_display_label.pack(pady=20)

        # --- Result Label ---
        self.result_label = tk.Label(self.root, text="Make your move!", font=self.RESULT_FONT, bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        self.result_label.pack(pady=10)

        # --- Score Label ---
        self.score_label = tk.Label(self.root, text=self.get_score_text(), font=self.SCORE_FONT, bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        self.score_label.pack(pady=15)

        # --- Buttons Frame ---
        button_frame = tk.Frame(self.root, bg=self.BTN_FRAME_BG, relief="solid", borderwidth=1)
        button_frame.pack(pady=20, padx=20, fill="x")
        button_frame.grid_columnconfigure((0, 1, 2), weight=1) # Make columns resize equally

        # --- Buttons ---
        self.rock_btn = self.create_choice_button(button_frame, self.emoji_map["Rock"], self.ROCK_COLOR, lambda: self.play("Rock"))
        self.rock_btn.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.paper_btn = self.create_choice_button(button_frame, self.emoji_map["Paper"], self.PAPER_COLOR, lambda: self.play("Paper"))
        self.paper_btn.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.scissors_btn = self.create_choice_button(button_frame, self.emoji_map["Scissors"], self.SCISSORS_COLOR, lambda: self.play("Scissors"))
        self.scissors_btn.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        # --- Controls Frame (Reset / Exit) ---
        controls_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        controls_frame.pack(fill="x", side="bottom", pady=20)
        controls_frame.grid_columnconfigure((0, 1), weight=1)

        reset_btn = tk.Button(controls_frame, text="Reset Game", font=self.SCORE_FONT, bg=self.RESET_COLOR, fg="#000", command=self.reset_game, relief="flat")
        reset_btn.grid(row=0, column=0, padx=20, sticky="ew")
        
        exit_btn = tk.Button(controls_frame, text="Exit Game", font=self.SCORE_FONT, bg=self.EXIT_COLOR, fg=self.TEXT_COLOR, command=self.root.destroy, relief="flat")
        exit_btn.grid(row=0, column=1, padx=20, sticky="ew")

    def create_choice_button(self, parent, text, bg_color, cmd):
        """Helper function to create styled buttons with hover effects."""
        btn = tk.Button(parent, text=text, font=self.BUTTON_FONT, bg=bg_color, fg=self.TEXT_COLOR, command=cmd, width=4, relief="flat", activeforeground=self.TEXT_COLOR, activebackground="#555")
        
        # Store original color for hover effect
        btn.original_bg = bg_color
        btn.hover_bg = "#555" # A dark gray for hover
        
        btn.bind("<Enter>", self.on_enter)
        btn.bind("<Leave>", self.on_leave)
        return btn

    def on_enter(self, e):
        e.widget['background'] = e.widget.hover_bg

    def on_leave(self, e):
        e.widget['background'] = e.widget.original_bg
        
    def get_score_text(self):
        """Formats the score string."""
        return f"🏆 Score → 🧍 You: {self.user_score} | 💻 Computer: {self.computer_score}"

    def play(self, choice):
        computer_choice = random.choice(self.choices)
        
        user_emoji = self.emoji_map[choice]
        comp_emoji = self.emoji_map[computer_choice]
        
        # Determine result
        if choice == computer_choice:
            result_text = "It's a Tie! 😐"
            result_color = "#F1C40F" # Yellow
        elif (choice == "Rock" and computer_choice == "Scissors") or \
             (choice == "Paper" and computer_choice == "Rock") or \
             (choice == "Scissors" and computer_choice == "Paper"):
            result_text = "You Win! 🎉"
            result_color = "#2ECC71" # Green
            self.user_score += 1
        else:
            result_text = "Computer Wins! 💻"
            result_color = "#E74C3C" # Red
            self.computer_score += 1

        self.show_popup(result_text, result_color)

        # Update labels
        self.battle_display_label.config(text=f"{user_emoji} vs {comp_emoji}")
        self.result_label.config(text=result_text, fg=result_color)
        self.score_label.config(text=self.get_score_text())

    def reset_game(self):
        """Resets the score and all labels to their default state."""
        self.user_score = 0
        self.computer_score = 0
        self.battle_display_label.config(text="VS")
        self.result_label.config(text="Make your move!", fg=self.TEXT_COLOR)
        self.score_label.config(text=self.get_score_text())

# --- Run the App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()
