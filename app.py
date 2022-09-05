from flask import Flask, jsonify, request
import time

app = Flask(__name__)
@app.route("/bot", methods=["POST"])

def response():
    query = dict(request.form)['query']
    if 'medico' in query or 'Medico' in query or 'Médico' in query or 'médico' in query:
        result = "La lista de médicos actual varía dependiendo de la especialidad."
    elif 'solicitud' in query or 'Solicitud' in query:
        result = "Puedes hacerlo a través de la opción que se encuentra en la parte inferior derecha."
    elif 'especialidad' in query or 'Especialidad' in query:
        result = "Contamos con Dermatología, Traumatología, Oftalmología, Cardiología, entre otros."
    elif 'medicamento' in query or 'Medicamento' in query:
        result = "En la sección de medicamentos puedes buscarlos por nombre y verificar si hay Stock."
    elif 'reprogramar' in query or 'Reprogramar' in query:
        result = "Sí, lo puedes realizar ingresando al calendario y dando click a la cita."
    elif 'contact' in query or 'Contact' in query:
        result = "Puedes escribirle al médico con el que tienes la cita a través del chat que está disponible en la cita."
    elif 'pago' in query or 'Pago' in query:
        result = "Los pagos pueden ser realizados con efectivo o tarjeta de crédito/débito."
    elif 'diagnóstico' in query or 'Diagnóstico' in query:
        result = "Ingresando a la cita en tu historial de citas puedes ver el diagnóstico."
    elif 'mi perfil' in query or 'Mi perfil' in query:
        result = "Sí, ingresando a tu perfil puedes modificar tus datos."
    elif 'calificación' in query or 'Calificación' in query or 'Calificaciones' in query or 'calificaciones' in query:
        result = "La respuesta dependerá por la especialidad, por favor ingresa una:"
    else:
        result = "Aun me estoy entrenando para ayudarte con eso."
        
    return jsonify({"response" : result})

if __name__ == "__main__":
    app.run(host="0.0.0.0",)