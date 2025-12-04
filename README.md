# Hangman – Campus IL self.py Project

A classic **Hangman** game implemented as part of the *self.py* course on Campus IL.  
The game loads a secret word from a user-provided text file and lets the player guess letters until the word is fully revealed or the maximum number of mistakes is reached.

---

## 📌 Overview

This project implements an interactive Hangman game with:

- ASCII-art drawings for every mistake level  
- Input validation for file path, index, and guessed letters  
- Word selection based on an index provided by the player  
- Automatic restart after each completed round

The gameplay includes guessing letters, revealing the word progressively, and visual feedback through Hangman drawings.

---

## 🧠 How the Game Works

### 1. Opening Screen
When the game starts, it displays:

- Welcome message  
- Hangman ASCII banner  
- Maximum mistakes allowed (**6**)  

---

### 2. Loading the Secret Word
The player is asked to:

1. **Enter a path to a text file containing English words**  
   - The file must exist  
   - Words can be separated by newlines or spaces  

2. **Enter the index of the desired word**  
   - Must be a positive integer  
   - If the index exceeds the number of words, the code wraps using modulo  

Example file format:
bird
cat
dog
elephant
tiger


---

### 3. Gameplay Loop
The main game loop runs while mistakes < 6:

1. Player guesses a letter  
2. Input is validated:  
   - One character  
   - Alphabetic  
   - Not guessed before  

3. The game updates:  
   - List of guessed letters  
   - Mistake count (letters not in the secret word)  
   - ASCII hangman drawing  
   - Current word state (e.g., `_ _ a _ _`)  

4. **Win check:**  
   If all letters are revealed → the player wins immediately.

---

### 4. Ending the Game
- **Win:** The full secret word is shown and the player receives a WINNER message.  
- **Lose:** The complete hangman is drawn, mistakes reach 6, and the player sees *GAME OVER* alongside the secret word.

---

### 5. Auto-Restart
After a round ends, the game starts over automatically thanks to an outer `while True` loop.

---

## 🎮 Example Gameplay Flow

1. Game starts  
2. ASCII welcome screen  
3. Player enters file path  
4. Player enters word index  
5. Word appears as underscores  
6. Player guesses letters  
7. Hangman updates each mistake  
8. Win / Game Over  
9. Game restarts  

---

## ▶️ Running the Game

### Requirements
- Python 3 installed

### Run command:
python hangman.py


### Inputs required:
1. **Path to words file**  
2. **Word index (positive integer)**  

---

## 📁 Words File Format

The file must contain **English words only**, separated by whitespace or newlines, for example:

bird
cat
chicken
cow
dog
elephant


---

## 📄 Project Files

- `hangman.py` — main game implementation  
- `README.md` — this documentation  
- Optional: `.gitignore` (to ignore `__pycache__/` and `.pyc` files)  

---

## ✔️ Notes

- The game supports any number of words in the file  
- Invalid inputs are handled gracefully with clear error messages  
- The Hangman ASCII drawing changes according to the mistake count  

---

Enjoy the game!
