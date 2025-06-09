from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/saludo', methods=['GET'])
def saludo():
    """
    Saluda con una cadena personalizada
    ---
    parameters:
      - name: cadena
        in: query
        type: string
        required: false
        description: Cadena de entrada para el saludo
    responses:
      200:
        description: Mensaje de saludo
        schema:
          type: object
          properties:
            mensaje:
              type: string
              example: hola Platzi desde la API de Python
    """
    entrada = request.args.get('cadena', '')
    resultado = f"hola {entrada} desde la API de Python"
    return jsonify({'mensaje': resultado})

if __name__ == '__main__':
    app.run(debug=True)