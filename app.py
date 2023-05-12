from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home page"

@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run()

# if __name__ == '__main__':
#     host = os.environ.get('HOST', 'localhost')
#     port = int(os.environ.get('PORT', 8080))
#     app.run(host=host, port=port)
