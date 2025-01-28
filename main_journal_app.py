import tkinter as tk
from tkinter import *
from datetime import datetime
import sqlite3
import random

#functions:
def db_connect(): # db setup
  # connect to a database
  conn = sqlite3.connect("journal.db")
  cursor = conn.cursor()

  cursor.execute('''
                CREATE TABLE IF NOT EXISTS prompts
                (id INTEGER PRIMARY KEY, text TEXT)
                ''')
  conn.commit()

  prompts_li = [ # list of prompts
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

  # close db objects
  cursor.close()
  conn.close()