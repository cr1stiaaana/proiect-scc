from flask import Flask, render_template, abort

# se va da import la fiecare biblioteca a tarii
#from app.lib import biblioteca_tara as <tara>


from app.lib import biblioteca_coreea as sk
from app.lib import biblioteca_belgia as belgia

'''NU SE MODIFICA'''
from app.lib import biblioteca_header as header
from app.lib.biblioteca_tari import TARI, TEMPLATE_TARA

# Mapare tara -> biblioteca
BIBLIOTECI = {
    'coreea-de-sud': sk,
    'belgia': belgia,
    #adauga tara> 'tara': tara
}

print('Proiect SCC - Tari')
app = Flask(__name__)



'''NU SE MAI MODIIFICA NIMIC IN REST'''


@app.route("/", methods=['GET'])
def pagina_home():
    return render_template('home.html')


@app.route("/<tara>", methods=['GET'])
def pagina_tara(tara):
    if tara not in TARI:
        abort(404)
    bib = BIBLIOTECI[tara]
    descriere = bib.descriere_tara()
    return render_template(TEMPLATE_TARA[tara], descriere=descriere, tara=tara)


@app.route("/<tara>/capitala", methods=['GET'])
def pagina_capitala(tara):
    if tara not in TARI:
        abort(404)
    bib = BIBLIOTECI[tara]
    return render_template('pagina.html',
                         titlu='Capitala',
                         header=header.header_capitala(),
                         continut=bib.descriere_capitala(),
                         tara_url=f'/{tara}')


@app.route("/<tara>/populatie", methods=['GET'])
def pagina_populatie(tara):
    if tara not in TARI:
        abort(404)
    bib = BIBLIOTECI[tara]
    return render_template('pagina.html',
                         titlu='Populație',
                         header=header.header_populatie(),
                         continut=bib.descriere_populatie(),
                         tara_url=f'/{tara}')


@app.route("/<tara>/steag", methods=['GET'])
def pagina_steag(tara):
    if tara not in TARI:
        abort(404)
    bib = BIBLIOTECI[tara]
    return render_template('steag.html',
                         header=header.header_steag(),
                         continut=bib.descriere_steag(),
                         tara_url=f'/{tara}')


if __name__ == '__main__':
    app.run(debug=True)
