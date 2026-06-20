# 🔑 My Grade 12 Password Manager Project

Hey there! Welcome to my 12th-grade Computer Science school project. I built a command-line password manager using Python to help people store all their login details in one place without losing track of them. It saves everything securely into binary files so your data doesn't vanish when you close the program.

---

## ✨ Cool Features

* **User Profiles:** You can create a master account with a unique username and a 4-digit PIN.
* **Isolated Storage:** Every user gets their own personal `.dat` file, meaning your password vault stays completely separate from anyone else's.
* **Password Generator:** If you're out of ideas, the built-in generator will whip up a random, strong password between 8 and 128 characters using letters, numbers, and symbols.
* **Full Control (CRUD):** You can easily view all your saved passwords, search for a specific website, add new entries, update outdated details, or delete accounts you don't use anymore.

---

## 📂 The Two Versions

I actually wrote two different versions of this project to try out different ways of working with binary files, specifically for updating data:

### 1. `password manager.py`
* This version handles updates by reading *all* of your saved credentials from the binary file into a Python list.
* It then finds the specific website you want to change, updates it in the list, and completely rewrites the binary file clean with the updated list.

### 2. `password manager alternate.py`
* This is my alternative approach where I tried a different file handling technique.
* Instead of loading everything into a list, it uses file pointer manipulation with `f.seek()` to jump straight to the exact byte position where the specific website's record is stored and tries to overwrite it directly.

---

## 🛠️ How It Works Under the Hood

* **Python 3** is the backbone of the entire project.
* **`pickle` module** handles our binary file operations (`.dat` files), turning Python dictionaries into saved data on your hard drive.
* **`random` module** handles shuffling the character sets to create secure passwords.
* **`EOFError` handling** keeps the app from crashing by sensing exactly when it hits the end of a file while reading data.

---

## 🎮 Navigation Guide

### The Main Menu
When you first run either script, you'll see this screen:
1. Create account to manage passwords
2. Login to account
3. Generate a password
4. Exit

### The Password Vault Menu
Once you log in successfully with your username and PIN, your vault opens up to these options:
1. View passwords
2. Search
3. Add password
4. Update password
5. Delete password
6. Generate a password
7. Logout

---

## 🚀 Quick Start

1. Make sure you have Python installed on your computer.
2. Download either `password manager.py` or `password manager alternate.py`.
3. Open your terminal/command prompt in that folder and run it:
   ```bash
   python "password manager.py"
