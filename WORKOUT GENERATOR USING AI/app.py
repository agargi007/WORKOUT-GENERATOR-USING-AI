import os
from flask import Flask, render_template, request
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")  # Or another supported model

app = Flask(__name__)

def format_workout_response(text):
    # Converts numbered tips to HTML list for display
    import re
    split = re.split(r'1\.', text, maxsplit=1)
    intro = split[0].strip()
    tips_block = "1." + split[1] if len(split) > 1 else ""
    tips = re.findall(r'\d+\.\s*(.*?)((?=\d+\.)|$)', tips_block, re.DOTALL)
    if tips:
        html_list = "<ol>"
        for tip, _ in tips:
            html_list += f"<li>{tip.strip()}</li>"
        html_list += "</ol>"
        return f"<p>{intro}</p>{html_list}"
    else:
        return f"<p>{text.strip()}</p>"

def get_workout_plan(goal, level):
    prompt = (
        f"Create a weekly workout plan for someone with the goal: {goal} "
        f"and fitness level: {level}. List daily exercises, sets/reps, and give 3 practical tips. "
        "Make it beginner-friendly and easy to follow."
    )
    response = model.generate_content(prompt)
    return format_workout_response(response.text)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        goal = request.form['goal']
        level = request.form['level']
        plan = get_workout_plan(goal, level)
        return render_template('result.html', plan=plan, goal=goal, level=level)
    return render_template('index.html')

if __name__ == '__main__':
    import threading, webbrowser
    threading.Timer(1.5, lambda: webbrowser.open('http://127.0.0.1:5000')).start()
    app.run(debug=True)
