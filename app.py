from flask import Flask, jsonify
from src.config import config
import openai

app=Flask(__name__)

messages = [
    {"role": "user", "content": "Hola"}
]

@app.route('/question/<userquestion>', methods=['GET'])
def getQuestion(userquestion):
    
    messages.append({"role": "user", "content": userquestion})
    customError = "No estoy disponible para responder en este momento"
    
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=messages
        )
            
        response = completion["choices"][0]["message"]["content"]
        
    except openai.error.APIError as e:
        response = customError
        pass

    except openai.error.APIConnectionError as e:
        response = customError
        pass
    
    except openai.error.AuthenticationError as e:
        response = customError
        pass

    except openai.error.RateLimitError as e:
        response = customError
        pass
    
    except openai.error.OpenAIError as e:
        response = customError
        pass
    
    messages.append({"role": "assistant", "content": response})
    
    return jsonify(response)

@app.route('/messages', methods=['GET'])
def getMessages():
    
    return jsonify(messages)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()

