from importlib.metadata import entry_points
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        # Access the entry fields to get the day, month, and year
        day = int(entry_day.get()) 
        month = int(entry_points.get())
        year = int(entry_year.get()) 
        
        today = datetime.today()
        birth_date = datetime(year, month, day)
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        messagebox.showinfo("Age Calculator", f"You are {age} years old.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid date.")
