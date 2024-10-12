from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)

# Funzione per generare password
def genera_password(lunghezza=12, numeri=False, speciali=False, maiuscole=False):
    caratteri = ''
    
    # Aggiungi tipi di caratteri selezionati dall'utente
    if numeri:
        caratteri += string.digits
    if speciali:
        caratteri += string.punctuation
    if maiuscole:
        caratteri += string.ascii_uppercase
    
    # Se nessuna opzione è selezionata, usa solo lettere minuscole
    if not caratteri:
        caratteri = string.ascii_lowercase

    # Usa 'secrets' per la generazione sicura
    password = ''.join(secrets.choice(caratteri) for i in range(lunghezza))
    return password

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        lunghezza = int(request.form["lunghezza"])
        numeri = request.form.get("numeri") is not None
        speciali = request.form.get("speciali") is not None
        maiuscole = request.form.get("maiuscole") is not None
        
        # Genera la password
        password = genera_password(lunghezza=lunghezza, numeri=numeri, speciali=speciali, maiuscole=maiuscole)
    
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
