#app do flask

from flask import Flask, render_template

app = Flask(__name__)

lista = [
    ['Refrigerante', 4.50, 'https://pontodopastel.economise.com.br/wp-content/uploads/2019/03/refrigerantes.jpg','Tomos os refrigerantes de 2lt: Coca-Cola, Sukita, Sprite, Fanta, Schweppes,Guaraná, Soda Antartica, Fors Cola'],
    ['Pizza', 2.50, 'https://s3.amazonaws.com/pu-mgr/default/a0R0f000010ZDNXEA4/5c001711e4b00010cfa42363.jpg','Temos pizza de: Frango, Calabresa, Brocolis, 4 queijos, Presunto e mussarela, Chocolate, Abacaxi, Camarão'],
    ['Suco', 24.90, 'https://cptstatic.s3.amazonaws.com/imagens/enviadas/materias/materia19920/beneficios-dos-sucos-naturais-1-alfa-hotel.jpg','Temos Sucos de: Abacaxi, Morango, Laranja, Limonada, Mamão, Aceróla, Frutas vermelhas, Frutas cítricas'],
    ['Salgados', 5.50, 'https://media-cdn.tripadvisor.com/media/photo-l/10/d0/52/2c/salgadinho-de-festa-betim.jpg','Temos estes  tipos de Salgados: Coxinha, Risole, Quibe, empáda, Esfira, Pasteis, Salsicha empanada'],
    ['Lanche', 18.50, 'http://malucaciadolanche.com.br/home/wp-content/uploads/2016/09/home_maluca_cardapio-01.jpg','Temos lanches de: X-tudo, X-file,Super-lombo, Americano, Bauru, X-egg, Bacon-tudo, X-salada']
]

@app.route('/')
def site():

    return render_template(
        'index.html', 
        titulo ='index',
        lista = lista
    )

@app.route('/itens/<int:id>')
def itens(id):
    index = lista[id]
    return render_template('itens.html', item = index )

if __name__ == '__main__':
    app.run()