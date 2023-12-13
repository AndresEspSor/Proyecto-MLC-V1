from joblib import load
import yaml

help_message = """
¡Bienvenido!

Para generar una predicción, escribe:
/predict

Rango de ronquidos del usuario: #.# # (por ejemplo, 45.120)
Frecuencia respiratoria: #.# # (por ejemplo, 16.048)
Temperatura corporal: #.# # (por ejemplo, 85.200)
Frecuencia de movimiento de las extremidades: #.# # (por ejemplo, 4.096)
Niveles de oxígeno en sangre: #.# # (por ejemplo, 82.240)
Movimiento ocular: #.# # (por ejemplo, 60.480)
Número de horas de sueño: #.# # (por ejemplo, 0.000)
Frecuencia cardíaca: #.# # (por ejemplo, 50.120)

Reemplaza los #s con los valores correspondientes. ¡Buena suerte!
"""


def get_model_response(message):
    """ This function sends a message to the chatbot and returns its response.
    
    Args:
        message (str): The message to send to the chatbot.
    
    Returns:
        str: The chatbot's response.
    """
    
    # Get the chatbot's response
    response = f"This is a response from the model to: {message[1:]}"
    
    option, data = message.split('\n')[0], message.split('\n')[1:]
    
    data = '\n'.join(data).strip()

    match option:
        case '/predict':
            data = yaml.load(data, Loader=yaml.Loader)
            
            clf = load('models/model.joblib')

            prediction = clf.predict([list(data.values())])

            responses = ['Nivel de estrés bajo/normal',' Nivel de estrés medio bajo',' Nivel de estrés medio',' Nivel de estrés medio alto',' Nivel de estrés alto']

            response = responses[int(prediction)]
        case '/help':
            response = help_message
    
    
    return str(response)


