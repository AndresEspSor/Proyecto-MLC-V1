# Flask Workshop: Flask First CRUD

This project is designed for a Flask workshop. The workshop is aimed at teaching the basics of Flask, a micro web framework written in Python. It's a great tool for small web applications and quick prototyping.

## Installation

Before you start, make sure you have Python and pip (Python package installer) installed on your system. If not, you can download Python [here](https://www.python.org/downloads/) and pip will be installed with it.

To install the necessary libraries and dependencies for this project, navigate to the project directory and run the following command:

```bash
pip install -r requirements.txt
```

This command tells pip to install the packages listed in the `requirements.txt` file.

## Running the Application

To run the application, you can use the flask command or python command. Before running the application, make sure you are in the project directory.

If you want to use the flask command, run the following:

```bash
export FLASK_APP=app
flask run --host=0.0.0.0 --port=8000
```

If you want to use the python command, run the following:

```bash
python app.py
```

## Debugging

To enable debugging mode, which provides you with more detailed error messages and enables the debugger, run the following command:

```bash
export FLASK_DEBUG=1
```

Then start your application. The application will now run in debug mode.

Enjoy the workshop!

## Next Steps

- Try running the application
- Explore the codebase
- Start building your Flask application!
