import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
from time import sleep
import sqlite3
import random
# supporting functions

def newWindow(title): # supporting function to open a new window with an title
   global window # Is needed for the addPrompt() function
   window = tk.Toplevel()
   window.title(title)

def closingUp(): # closing up button
  message = tk.messagebox.askquestion("Closing window...",  "Do you wish to close the app?") # gives a pop up with a Yes/No question
  
  if message == True: # if Yes is pressed
    print("Closing in...")
    closing_time = 5

    messages = [
      "Saving prompts...",
      "Saving changes...",
      "Closing connection...",
    ]

    while closing_time >=0:
      print(closing_time, random.choice(messages)) ; sleep(0.5)
      closing_time -= 1
    if closing_time <= 1:
      root.destroy()

# main functions

def setupDatabase(): # connect to and setup an initial database with existing prompts
  conn = sqlite3.connect("journal.db")
  cursor = conn.cursor()

  cursor.execute('''
                CREATE TABLE IF NOT EXISTS prompts
                (text TEXT UNIQUE)
                ''')

  cursor.execute('SELECT COUNT(*) FROM prompts')
  if cursor.fetchone()[0] == 0:
      prompts_li = [                              # list of innitial prompts
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


def addPrompt():
  global window
  newWindow("Entry Window")

  tk.Label(window, text="Enter a new prompt: ")
  text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
  text_area.pack(pady=10)

  def Publish():
    add_prompt = text_area.get("1.0", tk.END).strip()  # "stripping" the text from an area
    if add_prompt:
      # Make a connection to the DB
      conn = sqlite3.connect("journal.db")
      cursor = conn.cursor()
      cursor.execute('INSERT INTO prompts (text) VALUES (?)', (add_prompt,))
      conn.commit()
      cursor.close()
      conn.close()

      # Print and add label that the prompt was published to the DB
      print("Prompt was added!")
      completed = tk.Label(window, text="Prompt was added!\n Add new text to publish a new prompt to the DataBase!")
      completed.pack(pady=10)
  
  publish_button = tk.Button(window, text="Publish", command=Publish, width=20).pack(pady=10)

def getRandomPrompt():
  newWindow("Random prompt")
  def getNewPompt():
    conn = sqlite3.connect('journal.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, text FROM prompts ORDER BY RANDOM() LIMIT 1') # get a random prompt from the DB
    result = cursor.fetchone()
    conn.close()
    if result:  # Ensure there's a valid result
      prompt_label.config(text=result[1]) # result[1] contains the new prompt, but without the added number in the front (from the database)

  gen_prompts = tk.Button(window, text="New prompt", command=getNewPompt, width = 20).pack(pady=10)
  prompt_label = tk.Label(window, text="", anchor="w")

  prompt_label.pack(pady=10)


# setup Tkinter starting window
root = tk.Tk()
root.title("Journal App")
root.geometry("600x250")

# Current date
today = datetime.now().strftime('%d-%m-%Y')
tk.Label(root, text=f"Today's Date: {today}", font=("Arial", 14)).pack(pady=10)

# Buttons
gen_prompts = tk.Button(root, text="Generate Prompt", command=getRandomPrompt, width=20).pack(pady=10)
add_prompts = tk.Button(root, text="Add Prompt", command=addPrompt, width=20).pack(pady=10)
close_window = tk.Button(root, text="Close window", command=closingUp, width=20).pack(pady=20)

root.mainloop()