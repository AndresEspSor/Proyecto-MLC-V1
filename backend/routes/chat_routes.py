from flask import Blueprint, jsonify, request

from controllers.model_controller import get_model_response

chat_routes = Blueprint('chat_routes', __name__)

from utils import QRCode

@chat_routes.route('/whatsapp/qr', methods=['POST'])
def whatsapp_qr():
    """ This route is used to handle whatsapp messages. 
    It receives a message from the user and sends it to the chatbot. 
    Then, it receives the chatbot's response and sends it back to the user.

    Args:
        phone_number (str): The user's phone number.

    Returns:
        MessagingResponse: The chatbot's response.
    """

    try:
        # Get the message from the user
        QRCode.create(request.json['qr'])
        return {
            "message": "QR code recieved"
        }, 200
    except Exception as e:
        print(e)
        return {'message': e}, 500

@chat_routes.route('/whatsapp/ready', methods=['POST'])
def whatsapp_ready():
    """ This route is used to handle whatsapp messages. 
    It receives a message from the user and sends it to the chatbot. 
    Then, it receives the chatbot's response and sends it back to the user.

    Args:
        phone_number (str): The user's phone number.

    Returns:
        MessagingResponse: The chatbot's response.
    """

    try:
        # Get the message from the user
        QRCode.remove()
        return {
            "message": "Client ready from Python"
        }, 200
    except Exception as e:
        print(e)
        return {'message': e}, 500
    
@chat_routes.route('/', methods=['POST'])
def chat():
    """ This route is used to handle whatsapp messages. 
    It receives a message from the user and sends it to the chatbot. 
    Then, it receives the chatbot's response and sends it back to the user.

    Body Args:
        message (str): The message from the user.
        
    Returns:
        MessagingResponse: The chatbot's response.
    """

    try:
        # Get the message from the user
        message = request.json.get('message')
        
        # Get the chatbot's response
        response = get_model_response(message)
        
        # Send the chatbot's response to the user
        return jsonify({
            'message': response,
        }), 200
    except Exception as e:
        print(e)
        return {'message': e}, 500