# model_integration.py

class ModelIntegration:
    def __init__(self):
        self.models = {
            'gpt-3': OpenAIModel(api_key='OPENAI_API_KEY', model_name='gpt-3'),
            'gpt-4': OpenAIModel(api_key='OPENAI_API_KEY', model_name='gpt-4'),
            # Add other models as needed
        }

    def run_prompt(self, prompt_content, model_name, parameters=None):
        model = self.models.get(model_name)
        if not model:
            raise Exception("Model not supported")
        return model.generate(prompt_content, parameters)

