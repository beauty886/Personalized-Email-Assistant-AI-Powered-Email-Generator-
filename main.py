from flask import Flask, render_template, request
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

def generate_email(prompt, tone):
    tone_instruction = f"Write this email in a {tone} tone:"
    full_prompt = tone_instruction + prompt

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=full_prompt,
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].text.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    email_output = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        tone = request.form["tone"]
        email_output = generate_email(prompt, tone)
    return render_template("index.html", email=email_output)

if __name__ == "__main__":
    app.run(debug=True)