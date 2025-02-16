from flask import Flask, render_template, request
import openai

# Configuration de l'API OpenAI
openai.api_key = 'your-api-key'

app = Flask(__name__)

def generate_code(mode, details):
    prompt = f"Create a {mode} website based on the following details: {details}"
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
        generated_code = generate_code(mode, details)
        return render_template('result.html', generated_code=generated_code)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
