from translate import Translator

def get_translate(to_lang,text):
    translator= Translator(to_lang=to_lang)
    translation = translator.translate(text)
    return translation

if __name__ == "__main__":
    to_lang="German"
    text="Good Morning!"
    result=get_translate(to_lang,text)    
    print(result)