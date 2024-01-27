from flask import Flask, render_template
from openai import OpenAI
import os
# client = OpenAI(
#     # Defaults to os.environ.get("OPENAI_API_KEY")
# )
# Our_key = os.getenv('OPENAI_API_KEY')
# chat_completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Hello world"}]
# )

app = Flask(__name__,template_folder='template')
@app.route("/")
def hello():
    return render_template('index.html')

app.run(debug=True)