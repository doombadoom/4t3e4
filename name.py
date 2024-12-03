pip install flask requests
from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Web Proxy! Add '?url=<your-url>' to visit a site."

@app.route('/proxy')
def proxy():
    target_url = request.args.get('url')
    if not target_url:
        return "Please provide a URL, e.g., /proxy?url=https://example.com"

    try:
        response = requests.get(target_url)
        return Response(response.content, content_type=response.headers['Content-Type'])
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<doombadoom>/<4t3e4>.git
git branch -M main
git push -u origin main
