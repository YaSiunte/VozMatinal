import requests
import os
from dotenv import load_dotenv

# carrega as variáveis do .env
load_dotenv()

# pega a chave guardada no .env
chave = os.getenv("NEWS_API_KEY")

# monta a URL da requisição
url = f"https://newsapi.org/v2/everything?q=brasil&language=pt&pageSize=5&apiKey={chave}"

# faz a requisição
resposta = requests.get(url)

dados = resposta.json()

for artigo in dados ["articles"]:
    titulo = artigo["title"]
    print(titulo)
