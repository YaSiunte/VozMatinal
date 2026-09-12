from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv
from gtts import gTTS


app = Flask(__name__)


@app.route("/")
def home():
    load_dotenv()

    chave = os.getenv("NEWS_API_KEY")

    url = f"https://newsapi.org/v2/everything?q=brasil&language=pt&pageSize=5&apiKey={chave}"

    resposta = requests.get(url)

    dados = resposta.json()
    texto_final = "Aqui estão as 5 notícias principais dessa manhã.\n\n"
    lista_noticias = []

    for artigo in dados["articles"]:
        titulo = artigo["title"]
        descricao = artigo["description"]

        texto_final += f"{titulo}.\n"

        lista_noticias.append({"titulo": titulo, "descricao": descricao})

    print(texto_final)

    audio = gTTS(text=texto_final, lang="pt", tld="com.br")
    audio.save("static/audio/vozfinal.mp3")

    return render_template("index.html", noticias=lista_noticias)


if __name__ == "__main__":
    app.run(debug=True)
