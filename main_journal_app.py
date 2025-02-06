import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime
import sqlite3
import random

# supporting functions
def newWindow(title): # supporting function to open a new window with an title
   global window
   window = tk.Toplevel()
   window.title(title)

# main functions

def setupDatabase(): # connect to a(n) and setup initial database with existing prompts
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
  newWindow("Entry Window")
  tk.Label(window, text="Enter a new prompt in the terminal").pack(pady=30)
  # text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=15).pack(pady=10)

  conn = sqlite3.connect("journal.db")
  cursor = conn.cursor()

  global text
  add_prompt = input("\n \n Add in a new prompt: ")
  print("new prompt added!")
  
  cursor.execute('INSERT INTO prompts (text) VALUES (?)', (add_prompt,))
  conn.commit()
  
  cursor.close()
  conn.close()

def getRandomPrompt():
  newWindow("Random prompt")
  def getNewPompt():
    conn = sqlite3.connect('journal.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, text FROM prompts ORDER BY RANDOM() LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    if result:  # Ensure there's a valid result
      prompt_label.config(text=result[1]) # result[1] contains the new prompt, but without the added number in the front (from the database)

  gen_prompts = tk.Button(window, text="New prompt", command=getNewPompt, width = 20).pack(pady=10)
  prompt_label = tk.Label(window, text="", anchor="w")

  prompt_label.pack(pady=10)


def getRandomQuote():
   print("hi") # place holder




# setup Tkinter starting window
root = tk.Tk()
root.title("Journal App")
root.geometry("400x300")

# Current date
today = datetime.now().strftime('%d-%m-%Y')
tk.Label(root, text=f"Today's Date: {today}", font=("Arial", 14)).pack(pady=10)

# Buttons
gen_prompts = tk.Button(root, text="Generate Prompt", command=getRandomPrompt, width=20).pack(pady=10)
add_prompts = tk.Button(root, text="Add Prompt", command=addPrompt, width=20).pack(pady=10)
get_quote = tk.Button(root, text="Quote of the Day", command=getRandomQuote, width=20).pack(pady=10)

root.mainloop()