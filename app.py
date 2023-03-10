from flask import Flask, jsonify
import openai

app=Flask(__name__)

class DevelopmentConfig():
        DEBUG = True
        openai.api_key = 'API-KEY'
    
config = {
    'development': DevelopmentConfig
}

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
    
    result = {"role": "assistant", "content": response}
    
    messages.append(result)
    
    return jsonify(result)

@app.route('/messages', methods=['GET'])
def getMessages():
    
    return jsonify(messages)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()

