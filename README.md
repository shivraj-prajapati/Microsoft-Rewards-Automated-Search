# Microsoft Rewards Automated Search

This repository contains a Python script that automates searches in Microsoft Edge to help you earn Microsoft Rewards points. It performs multiple Google searches with random programming-related queries, ensuring that the daily search quota is met. The script is designed to handle multiple accounts, automating the process of opening Edge, searching queries, and closing the browser.

## Features
- Automates opening and closing of Microsoft Edge using `pyautogui`.
- Searches random questions from a predefined list to simulate user searches.
- Supports multiple Microsoft accounts.
- Meets the daily 30 search limit for Microsoft Rewards.
- Randomized time intervals between actions for more human-like behavior.

## How to Use

### Clone this repository:
```bash
git clone https://github.com/shivraj-prajapati/Microsoft-Rewards-Automated-Search.git
```

### Install the required dependencies:
```bash
pip install pyautogui
```

### `questions.py` file is already given you can add more questions if you want. Example:
```python
questions = [
    "What is polymorphism in Java?",
    "Explain inheritance in C++.",
    "How to implement bubble sort algorithm in Python?",
    # Add more questions here...
]
```

### Run the script:
```bash
python search_automation.py
```

The script will automatically open Microsoft Edge, search for the questions, and close the browser once the search limit is met.

## Notes
- Ensure Microsoft Edge is installed on your machine.
- The script uses `pyautogui` to simulate keyboard and mouse actions. Make sure your screen resolution and settings match the coordinates used in the script for clicks and typing.

## Multiple Account Usage

- If you want to automate the search process for **multiple accounts**, uncomment the code in the `search_automation.py` script where multiple account handling is implemented. 
- Make sure you adjust the click coordinates in the script according to your screen resolution and the positioning of accounts in your browser.

## Disclaimer

This script is for educational purposes only. Automating searches for rewards might be against Microsoft's Terms of Service. Use at your own risk.
