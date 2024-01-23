#Desenvolva uma aplicação Flask que exiba
#uma lista de jogos ao acessar a página.
#Utilize uma rota única para mostrar os
#nomes dos jogos e, se desejar, adicione
#informações adicionais, como o gênero.

from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)

@app.route('/jogos')

class J1:
    def __init__(self, nome, plataforma, seguidores, interesse):
        self.nome = nome
        self.plataforma = plataforma
        self.seguidores = seguidores
        self.interesse = interesse

lista = []


if __name__ == '__main__':
    app.run()