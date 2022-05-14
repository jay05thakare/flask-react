from flask import Flask
# from dotenv import load_dotenv
# load_dotenv()
# import os

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return {
        'name': 'Hence frontend is integrated to backend properly!',
    }


if __name__ == '__main__':
    app.run(debug=True)