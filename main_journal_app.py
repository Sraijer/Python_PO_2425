import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime
import sqlite3
import random


# connect to a database
def setupDatabase(): # setup initial database with existing prompts
  conn = sqlite3.connect("journal.db")
  cursor = conn.cursor()

  cursor.execute('''
                CREATE TABLE IF NOT EXISTS prompts
                (text TEXT UNIQUE)
                ''')

  cursor.execute('SELECT COUNT(*) FROM prompts')
  if cursor.fetchone()[0] == 0:
      prompts_li = [                              # list of prompts
      "What is a quote that means a lot to you?",
      "What quote do you live by and why?",
      "What is a place you love to frequent?",
      "What is the best book you have read?",
      "What is your favorite flower, why and draw it out:",
      "What is your most cherished memory?",
      "The world would be a lot better if...",
      "What are some things that frustrate you? Why does it bother you so much?",
      "What is holding you back right now from achieving your dreams?",
      "What rules do you (want to) live your life by?",
      "Write about times you were really proud of yourself, what happened? Why did it make you proud?",
      "What is a petpeeve you have?",
      "What triggered negative feelings today?",
      "How do I think others perceive me and how do I want them to see me?",
      "How do I respond to compliments?",
      "What is the best compliment I have ever recieved and why did it brighten up my day?",
      "What was the best vacation I have been on?",
      "What are my bucket-list travel places?",
      "What are some healthy coping meganisms I want to build?",
      "What do I want to save money for?",
      "What is your favorite childhood show?",
      "What is your favorite song?",
      ]

      # add initial prompts to database
      cursor.executemany('INSERT INTO prompts (text) VALUES (?)', [(p,) for p in prompts_li] )
      conn.commit()

  # close db objects
  cursor.close()
  conn.close()
  return prompts_li

  
def addPrompt(): # user function to add new prompts into database
  def save(): # saves the entry, incomplete
    text = text_area.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Entry", "Please write something before saving.")
        return
  
  entry_window = tk.Toplevel() # creates a seperate window to enter new prompts

  tk.Button(entry_window, text="Save Entry", command=save, width=15).pack(pady=10) # save button
  text_area = scrolledtext.ScrolledText(entry_window, wrap=tk.WORD, width=40, height=15)
  text_area.pack(pady=10)

  conn = sqlite3.connect("journal.db")
  cursor = conn.cursor()
  
  add_prompt = input("Add in a prompt: ")
  
  cursor.execute('INSERT INTO prompts (text) VALUES (?)', (add_prompt,))
  conn.commit()
  
  cursor.close()
  conn.close()

def getRandomPrompt():
  conn = sqlite3.connect('journal.db')
  cursor = conn.cursor()

  cursor.execute('SELECT id, text FROM prompts ORDER BY RANDOM() LIMIT 1')
  result = cursor.fetchone()
  print(result)
  conn.close()
  return result

def getRandomQuote():
   print("hi") # place holder

root = tk.Tk()
root.title("Journal App")
root.geometry("400x300")

# Current date
today = datetime.now().strftime('%d-%m-%Y')
tk.Label(root, text=f"Today's Date: {today}", font=("Arial", 14)).pack(pady=10)

# Buttons
gen_prompts = tk.Button(root, text="Generate Prompt", command=getRandomPrompt, width=20).pack(pady=10)
add_prompts = tk.Button(root, text="Add Prompt", command=addPrompt, width=20).pack(pady=10)
root.mainloop()