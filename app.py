from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Configuration de l'API OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

def generate_code(mode, details, colors=None):
    prompt = f"Create a {mode} website based on the following details: {details}. Customize with colors {colors}" if colors else f"Create a {mode} website based on the following details: {details}"
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mode = request.form['mode']
        details = request.form['details']
        colors = request.form['colors']  # Nouvelle option de couleurs
        generated_code = generate_code(mode, details, colors)
        return render_template('result.html', generated_code=generated_code)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
