import sys
from nlp_processor import detect_language, preprocess_text
from model import ChatModel
from search_engine import search_internet
from learner import Learner

def main():
    chat_model = ChatModel()
    learner = Learner()

    print("Chatbot iniciado. Escribe 'salir' para terminar.")

    while True:
        user_input = input("Pregunta: ").strip()
        if user_input.lower() == 'salir':
            print("Chatbot terminado.")
            break
        
        # Detectar idioma
        lang = detect_language(user_input)
        
        if lang not in ['es', 'ca', 'en']:
            print("Chatbot: Estoy aprendiendo, pronto podré hablar en tu idioma. Escríbeme en Español, catalán o inglés.")
            continue
        
        # Preprocesar texto
        processed_input = preprocess_text(user_input, lang)
        
        # Obtener respuesta del modelo
        response = chat_model.get_response(processed_input, lang)
        
        # Aprender de la interacción
        learner.learn_from_interaction(user_input, response)
        
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()

