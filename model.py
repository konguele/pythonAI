from transformers import AutoModelForCausalLM, AutoTokenizer

class ChatModel:
    def __init__(self):
        self.models = {
            'es': self.load_model('dccuchile/bert-base-spanish-wwm-cased'),
            'ca': self.load_model('projecte-aina/bert-base-ca-cased'),
            'en': self.load_model('gpt2')
        }
    
    def load_model(self, model_name):
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        return model, tokenizer
    
    def get_response(self, processed_input, lang):
        model, tokenizer = self.models[lang]
        inputs = tokenizer.encode(processed_input, return_tensors='pt')
        outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

