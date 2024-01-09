import requests
import json
import pyfiglet
import tkinter as tk
from tkinter import scrolledtext

burp0_url = "https://papersowl.com:443/plagiarism-checker-send-data"
# Define other global variables like burp0_headers, burp0_cookies, etc.

def check_plagiarism():
    burp0_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
        "Accept": "*/*",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://papersowl.com/free-plagiarism-checker",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://papersowl.com",
        "Dnt": "1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-origin",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Te": "trailers",
        "Connection": "close"
    }

    burp0_cookies = {
        # Define your cookies here
        "PHPSESSID": "qjc72e3vvacbtn4jd1af1k5qn1",
        # Add other cookies as needed
    }

    text_to_check = text_entry.get("1.0", "end-1c")
    
    burp0_data = {
        "is_free": "false",
        "plagchecker_locale": "en",
        "product_paper_type": "1",
        "title": '',
        "text": str(text_to_check)
    }

    r = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    result = json.loads(r.text)

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"\n[!] Word count : {result['words_count']}")
    output_text.insert(tk.END, f"\n[!] Turnitin index : {100 - float(result['percent'])}")
    output_text.insert(tk.END, f"\n[!] Matches : {result['matches']}")



# Rest of the GUI code remains the same...


# GUI Setup
window = tk.Tk()
window.title("Plagiarism Checker")
window.geometry("600x400")

# Create a banner label
banner = pyfiglet.figlet_format("ThePJcodes")
banner_label = tk.Label(window, text=banner, font=("Courier", 14))
banner_label.pack(pady=10)

# Create a text entry for user input
text_label = tk.Label(window, text="Input text to check with Turnitin:")
text_label.pack(pady=5)

text_entry = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=10)
text_entry.pack(pady=10)

# Create a button to trigger the plagiarism check
check_button = tk.Button(window, text="Check Plagiarism", command=check_plagiarism)
check_button.pack(pady=10)

# Create a scrolled text widget for displaying the results
output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=10)
output_text.pack(pady=10)

# Run the GUI
window.mainloop()
