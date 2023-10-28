from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola mundo desde NGINX y AWS pero con mas texto"

@app.route('/home')
def mostrar_imagen():
    return render_template('index.html')



# Ruta para recibir los datos de Shopify a través de un webhook
@app.route('/shopify-webhook', methods=['POST'])
def shopify_webhook():
    # Verifica que el contenido sea JSON
    if request.is_json:
        data = request.get_json()
        # Procesa los datos JSON recibidos

        # Aquí puedes agregar tu lógica para manejar los datos de Shopify

        # Devuelve una respuesta (opcional)
        response_data = {"message": "Datos de Shopify recibidos correctamente"}
        return jsonify(response_data), 200
    else:
        return "El contenido no es JSON", 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)