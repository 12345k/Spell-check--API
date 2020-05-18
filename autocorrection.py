from textblob import TextBlob

def get_corrected_sentence(text):
    b = TextBlob(text)
    return str(b.correct())

if __name__ == "__main__":
    text="I havv goood speling!"
    result=get_corrected_sentence(text)    
    print(result)