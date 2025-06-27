# Flask Calculator

A simple web-based calculator built with Flask. Supports evaluating safe mathematical expressions, stores a calculation history, and provides a clean, modern interface styled with CSS.

## Features

- Web-based calculator using Flask  
- Supports addition, subtraction, multiplication, division, parentheses  
- Calculation history shown on the page  
- "Clear History" button  
- Secure math evaluation with `asteval` (safer than raw eval)  
- Clean, responsive CSS styling  
- Ready to deploy on Heroku or other cloud services

## Installation

1. Clone the repository

git clone https://github.com/yourusername/flask-adder.git
cd flask-adder
Create a virtual environment

python -m venv venv
Activate the virtual environment

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install requirements
pip install -r requirements.txt

Run the app
python app.py

Visit http://127.0.0.1:5000 in your browser.

Usage
Type a valid math expression, e.g. 5 + 3 * 2

Press Calculate to see the result

View previous calculations in the history

Press Clear History to reset

Roadmap
Add SQLite history storage

Add user accounts (future)

Deploy to Heroku

Add unit tests with GitHub Actions

License
This project is licensed under the MIT License.

Contributing
Contributions welcome! Please open issues or submit pull requests on GitHub.


---

**Steps to add this file:**

1. Create a new file in your project root folder named `README.md`  
2. Paste the content above inside it  
3. Save the file  
4. In your terminal, commit and push:

git add README.md
git commit -m "Add README file"
git push
