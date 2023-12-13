const { Client, LocalAuth } = require('whatsapp-web.js');
const dotenv = require('dotenv');
const axios = require('axios');
const cors = require('cors');

const express = require('express');
const bodyParser = require('body-parser');

const whatsapp = new Client({
    puppeteer: {
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox'
        ],
        authStrategy: new LocalAuth()
    }
});

dotenv.config();

const app = express();

app.use(bodyParser.json()); // support json encoded bodies

const API_URL = process.env.API_URL;

app.use(cors({
    origin: process.env.API_HOST
}));

const extract_numbers = (phone_number) => {
    return phone_number.replace(/[^0-9]/g, '');
}

const send_message = (phone_number, message) => {
    if (message && phone_number.length < 21) // 21 is the max length of a phone number in whatsapp else will be a WhatsApp Group
        whatsapp.sendMessage(phone_number, message).then(() => {
            console.log(`Mensaje enviado a ${extract_numbers(phone_number)}`);
        }).catch((error) => {
            console.error(`Error al enviar el mensaje a ${extract_numbers(phone_number)}: ${error}`);
        });
}

// whatsapp
whatsapp.on('qr', qr => {
    console.log('QR code sent');
    axios.post(`${API_URL}/chat/whatsapp/qr`, {
        qr: qr
    }).then((response) => {
        console.log(response.data.message);
    }).catch((error) => {
        console.log(error.response);
    });
});

whatsapp.on('ready', () => {
    console.log('Client is ready from Javascript');
    axios.post(`${API_URL}/chat/whatsapp/ready`).then((response) => {
        console.log(response.data.message);
    }).catch((error) => {
        console.log(error.response ? error.response.data : undefined)
    });
});

whatsapp.on('message', async message => {
    // Get message phone_number
    const user_phone_number = message.from;

    // Check if message starts with a slash
    if (message.body[0] === '/')
        await axios.post(`${API_URL}/chat/`, {
            message: message.body
        }).then((response) => {
            send_message(user_phone_number, response.data.message);
        }).catch((error) => {
            console.log(error);
            console.log(error.response ? error.response.data : undefined)
            send_message(user_phone_number, 'Hay un error en el servidor, por favor intente en unos minutos...');
        });
});


whatsapp.initialize();

app.get('/health-check', (req, res) => {
    res.status(200).json({ message: 'Server is running' });
});
