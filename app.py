from flask import Flask,request,jsonify
from googletrans import Translator
translator = Translator()
app = Flask(__name__)


@app.route('/translate',methods=['POST'])
def translate():
    data=request.get_json()
    text = data['text']
    lang = data['lan']
    out = translator.translate(text, dest=lang)
    return jsonify({"output":out.text})

if __name__== "__main__":
    print("The App is running .")
    app.run()