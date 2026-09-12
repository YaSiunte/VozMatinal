import requests
import os
from dotenv import load_dotenv
from gtts import gTTS

# carrega as variáveis do .env
load_dotenv()

# pega a chave guardada no .env
chave = os.getenv("NEWS_API_KEY")

# monta a URL da requisição
url = f"https://newsapi.org/v2/everything?q=brasil&language=pt&pageSize=5&apiKey={chave}"

# faz a requisição
resposta = requests.get(url)

dados = resposta.json()
texto_final = "Aqui estão as 5 notícias principais dessa manhã.\n\n"
lista_noticias = []

for artigo in dados ["articles"]:
    titulo = artigo["title"]
    descricao = artigo["description"]

    texto_final += f"{titulo}.\n"

    # guarda a notícia completa numa lista de dicionários, pro front-end usar depois
    lista_noticias.append({"titulo": titulo, "descricao": descricao})

print(texto_final)

audio = gTTS(text=texto_final, lang="pt", tld="com.br")
audio.save("vozfinal.mp3")