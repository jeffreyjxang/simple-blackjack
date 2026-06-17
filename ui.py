import tkinter as tk
from tkinter import messagebox
import random

# Import logic from logic.py
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def pickup(cards):
    output = cards[random.randint(0, 9)]
    return output

def dealer_turn(dSum, uSum):
    result = []
    while dSum < 17:
        dSum = dSum + pickup(cards)
        result.append(f"Dealer draws: {dSum}")
    
    if dSum > 21:
        result.append("Dealer busts! You win!")
        return "player_wins", result
    elif 17 <= dSum <= 21:
        if dSum > uSum:
            result.append("Dealer wins!")
            return "dealer_wins", result
        elif dSum < uSum:
            result.append("Player wins!")
            return "player_wins", result
        else:
            result.append("It's a push!")
            return "push", result
    
    return "unknown", result


class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")
        self.root.geometry("500x600")
        self.root.configure(bg="#1B5E20")
        
        # Game state
        self.uSum = 0
        self.dSum = 0
        self.uCard_1 = 0
        self.uCard_2 = 0
        self.dCard_1 = 0
        self.dCard_2 = 0
        self.game_over = False
        self.game_active = False
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="BLACKJACK", font=("Arial", 24, "bold"), 
                        bg="#1B5E20", fg="white")
        title.pack(pady=10)
        
        # Dealer section
        dealer_frame = tk.Frame(self.root, bg="#1B5E20")
        dealer_frame.pack(pady=10)
        
        tk.Label(dealer_frame, text="Dealer's Hand:", font=("Arial", 12, "bold"), 
                bg="#1B5E20", fg="white").pack()
        
        self.dealer_hand_label = tk.Label(dealer_frame, text="", font=("Arial", 11), 
                                         bg="#1B5E20", fg="#FFD700")
        self.dealer_hand_label.pack()
        
        self.dealer_sum_label = tk.Label(dealer_frame, text="", font=("Arial", 10), 
                                        bg="#1B5E20", fg="#E0E0E0")
        self.dealer_sum_label.pack()
        
        # Divider
        tk.Label(self.root, text="─" * 40, bg="#1B5E20", fg="white").pack()
        
        # Player section
        player_frame = tk.Frame(self.root, bg="#1B5E20")
        player_frame.pack(pady=10)
        
        tk.Label(player_frame, text="Your Hand:", font=("Arial", 12, "bold"), 
                bg="#1B5E20", fg="white").pack()
        
        self.player_hand_label = tk.Label(player_frame, text="", font=("Arial", 11), 
                                         bg="#1B5E20", fg="#FFD700")
        self.player_hand_label.pack()
        
        self.player_sum_label = tk.Label(player_frame, text="", font=("Arial", 10), 
                                        bg="#1B5E20", fg="#E0E0E0")
        self.player_sum_label.pack()
        
        # Message area
        self.message_label = tk.Label(self.root, text="", font=("Arial", 11), 
                                     bg="#1B5E20", fg="#FFD700", wraplength=450)
        self.message_label.pack(pady=15)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg="#1B5E20")
        button_frame.pack(pady=10)
        
        self.hit_button = tk.Button(button_frame, text="Hit", command=self.hit, 
                                   width=8, font=("Arial", 10), bg="#4CAF50", fg="white")
        self.hit_button.grid(row=0, column=0, padx=5)
        
        self.stand_button = tk.Button(button_frame, text="Stand", command=self.stand, 
                                     width=8, font=("Arial", 10), bg="#FF6F00", fg="white")
        self.stand_button.grid(row=0, column=1, padx=5)
        
        self.double_button = tk.Button(button_frame, text="Double", command=self.double, 
                                      width=8, font=("Arial", 10), bg="#1976D2", fg="white")
        self.double_button.grid(row=0, column=2, padx=5)
        
        # New game button
        self.new_game_button = tk.Button(self.root, text="New Game", command=self.new_game, 
                                        width=15, font=("Arial", 10), bg="#7B1FA2", fg="white")
        self.new_game_button.pack(pady=10)
        
        self.start_game()
    
    def start_game(self):
        self.new_game()
    
    def new_game(self):
        self.uCard_1 = pickup(cards)
        self.uCard_2 = pickup(cards)
        self.uSum = self.uCard_1 + self.uCard_2
        
        self.dCard_1 = pickup(cards)
        self.dCard_2 = pickup(cards)
        self.dSum = self.dCard_1 + self.dCard_2
        
        self.game_over = False
        self.game_active = True
        self.message_label.config(text="")
        self.update_display()
        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)
        self.double_button.config(state=tk.NORMAL)
    
    def update_display(self):
        self.dealer_hand_label.config(text=f"{self.dCard_1} + {self.dCard_2}")
        self.dealer_sum_label.config(text=f"Sum: {self.dSum}")
        
        self.player_hand_label.config(text=f"{self.uCard_1} + {self.uCard_2}")
        self.player_sum_label.config(text=f"Sum: {self.uSum}")
    
    def hit(self):
        if not self.game_active:
            return
        
        new_card = pickup(cards)
        self.uSum += new_card
        self.player_hand_label.config(text=f"{self.player_hand_label.cget('text')} + {new_card}")
        self.player_sum_label.config(text=f"Sum: {self.uSum}")
        
        if self.uSum > 21:
            self.message_label.config(text="You busted! Dealer wins!", fg="#F44336")
            self.end_game()
    
    def stand(self):
        if not self.game_active:
            return
        
        result, messages = dealer_turn(self.dSum, self.uSum)
        
        # Update dealer display with final sum
        self.dealer_sum_label.config(text=f"Final Sum: {self.dSum}")
        
        # Show result
        message_text = "\n".join(messages)
        if result == "player_wins":
            self.message_label.config(text=message_text, fg="#4CAF50")
        elif result == "dealer_wins":
            self.message_label.config(text=message_text, fg="#F44336")
        else:
            self.message_label.config(text=message_text, fg="#FFC107")
        
        self.end_game()
    
    def double(self):
        if not self.game_active:
            return
        
        new_card = pickup(cards)
        self.uSum += new_card
        self.player_hand_label.config(text=f"{self.player_hand_label.cget('text')} + {new_card}")
        self.player_sum_label.config(text=f"Sum: {self.uSum}")
        
        if self.uSum > 21:
            self.message_label.config(text="You busted! Dealer wins!", fg="#F44336")
            self.end_game()
        else:
            # Auto stand after double
            result, messages = dealer_turn(self.dSum, self.uSum)
            self.dealer_sum_label.config(text=f"Final Sum: {self.dSum}")
            message_text = "\n".join(messages)
            if result == "player_wins":
                self.message_label.config(text=message_text, fg="#4CAF50")
            elif result == "dealer_wins":
                self.message_label.config(text=message_text, fg="#F44336")
            else:
                self.message_label.config(text=message_text, fg="#FFC107")
            
            self.end_game()
    
    def end_game(self):
        self.game_active = False
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.double_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = BlackjackGame(root)
    root.mainloop()
