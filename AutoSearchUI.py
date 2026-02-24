import tkinter as tk
import threading
import pyautogui
import time
import random
import webbrowser

# Sample clean words (extend as needed)
clean_words = ["India",
    "nature", "ocean", "sunrise", "library", "harmony", "peaceful",
    "science", "flowers", "mountain", "books", "history", "sunshine",
    "smile", "kindness", "technology", "art", "music", "garden", "calm",
    "forest", "river", "sky", "wind", "time", "friendship", "future", "energy",
    "temple", "yoga", "ayurveda", "meditation", "lotus", "sandalwood", "Himalayas",
    "peacock", "festival", "diya", "rangoli", "unity", "culture", "classical", "saree",
    "spice", "mango", "turmeric", "riverbank", "ghats", "chant", "rhythm", "wisdom",
    "purity", "sacred", "incense", "prayer", "holy", "teacher", "guru", "ashram",
    "banyan", "coconut", "silk", "village", "monsoon", "devotion", "flute", "sari",
    "mehndi", "laughter", "moonlight", "tranquility", "compassion", "respect",
    "heritage", "tradition", "sweets", "jasmine", "kathak", "tabla", "veena", "bhajan",
    "raga", "dawn", "dusk", "cows", "fields", "blessing", "neem", "bricks", "trust",
    "saffron", "belief", "dreams", "innocence", "equality", "care", "love", "pilgrimage",
    "tolerance", "serenity",
    "lotuspond", "pavilion", "scripture", "garland", "charity", "rice", "lantern",
    "namaste", "marigold", "heritage", "ghungroo", "cowbell", "paddy", "wheel", "path",
    "steps", "healer", "echo", "pebble", "breeze", "amber", "karma", "handicraft",
    "candle", "joy", "hope", "nectar", "sage", "mantra", "clarity", "fountain",
    "lantern", "shade", "ink", "festivallight", "celebration", "ritual", "grain",
    "pottery", "truth", "balance", "innate", "humility", "reflection", "bindi", "ricefield"
]


running = False

def open_browser():
    webbrowser.open("https://www.bing.com")

def type_random_words(limit):
    global running
    words_to_use = random.sample(clean_words, min(limit, len(clean_words)))
    
    for i, word in enumerate(words_to_use):
        if not running:
            print("Stopped early at", i, "searches.")
            break
        time.sleep(7)
        pyautogui.hotkey('ctrl', 'l')  # Focus search bar
        time.sleep(0.5)
        pyautogui.typewrite(word)
        pyautogui.press('enter')

def start_bot():
    global running
    try:
        search_count = int(entry.get())
    except ValueError:
        status_label.config(text="Enter a valid number")
        return
    
    if search_count < 1:
        status_label.config(text="Enter a number > 0")
        return
    
    running = True
    status_label.config(text="Running...")
    threading.Thread(target=run_bot, args=(search_count,)).start()

def run_bot(search_count):
    open_browser()
    time.sleep(5)  # Wait for browser to open
    type_random_words(search_count)
    status_label.config(text="Done or Stopped")

def stop_bot():
    global running
    running = False
    status_label.config(text="Stopped")

# GUI Setup
root = tk.Tk()
root.title("Auto Search Bot")
root.geometry("320x220")

tk.Label(root, text="How many searches to run:").pack(pady=5)
entry = tk.Entry(root)
entry.insert(0, "20")
entry.pack(pady=5)

start_btn = tk.Button(root, text="Start Searching", command=start_bot, bg="green", fg="white")
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="Stop", command=stop_bot, bg="red", fg="white")
stop_btn.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
