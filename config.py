import openai

class DevelopmentConfig():
        DEBUG = True
        openai.api_key = 'YOUR-APIKEY-HERE'
    
config = {
    'development': DevelopmentConfig
}