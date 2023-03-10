import openai

class DevelopmentConfig():
        DEBUG = True
        openai.api_key = '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'
    
config = {
    'development': DevelopmentConfig
}