from flask import Flask, request, render_template
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_text', methods=['POST'])
def extract_text():
    try:
        if 'image' not in request.files:
            return render_template('index.html', error="No image part in the form")

        image = request.files['image']
        if image.filename == '':
            return render_template('index.html', error="No selected file")

        img = Image.open(image)
        text = pytesseract.image_to_string(img)

        return render_template('result.html', text=text)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
