import openai  

chave_api = 

openai.api_key = chave_api

def envia_mensagem_chatbot(mensagem, lista_mensagens = []):
    
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )
    
    
    resposta = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = lista_mensagens,
    )
    
    return resposta["choices"][0]["message"]

lista_mensagens = []

while True:
    texto = input("escreva sua mensagem (digite sair para parar a conversa)")
    
    if texto.lower() == "sair" or texto.upper() == "sair":
        break
    else:
        resposta = envia_mensagem_chatbot(texto, lista_mensagens)
        lista_mensagens.append(resposta)
        print(resposta["content"])

