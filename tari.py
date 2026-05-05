from flask import Flask, render_template
from lib import biblioteca_coreea as sk 
from lib import biblioteca_header as header 


print('Coreea de Sud')
app = Flask(__name__)

@app.route("/", methods=['GET'])
def pagina_principala():
    descriere = sk.descriere_tara()
    return render_template('index.html', descriere=descriere)


@app.route("/capitala", methods=['GET'])
def pagina_capitala():
    header_capitala = header.header_capitala()
    capitala = sk.descriere_capitala()
    
    return render_template('pagina.html', 
                         titlu='Capitala',
                         header=header_capitala,
                         continut=capitala)


@app.route("/populatie", methods=['GET'])
def pagina_populatie():
    header_populatie = header.header_populatie()
    populatie = sk.descriere_populatie()
    
    return render_template('pagina.html',
                         titlu='Populație', 
                         header=header_populatie,
                         continut=populatie)


@app.route("/steag", methods=['GET'])
def pagina_steag():
    header_steag = header.header_steag()
    steag = sk.descriere_steag()
    
    return render_template('steag.html',
                         header=header_steag,
                         continut=steag)

if __name__ == '__main__':
    app.run(debug=True)
