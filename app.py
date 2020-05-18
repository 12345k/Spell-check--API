from flask import Flask, render_template, request,jsonify,Response,make_response
import autocorrection
import autotranslate
app = Flask(__name__)

@app.route('/api/v1/autocorrection', methods=['GET', 'POST'])
def autocorrect():

    is_changed=True
    content = request.get_json()
    text=content['text']
    result=autocorrection.get_corrected_sentence(text)
    if result == text:
        is_changed=False
    message = {"result":result,"is_changed":is_changed}
    print(message)
    return jsonify(message)



@app.route('/api/v1/translate', methods=['GET', 'POST'])
def translate():
    content = request.get_json()
    text=content['text']
    to_lang=content['to_lang']
    result=autotranslate.get_translate(to_lang,text)
    message = {"result":result}
    print(message)
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True,port=5000)