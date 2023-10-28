from flask import Flask, request


app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    # Aquí manejarás la lógica de tu webhook
    # Puedes acceder a los datos recibidos en request.data
    data = request.data
    # Realiza las acciones necesarias con los datos del webhook
    # ...
    return 'Webhook recibido con éxito', 200


if __name__ == '__main__':
    app.run(debug=True)
