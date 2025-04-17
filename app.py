from flask import Flask, request, render_template
from inference import generate_caption

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    caption = ""
    if request.method == 'POST':
        image = request.files['image']
        image_path = f"static/{image.filename}"
        image.save(image_path)
        caption = generate_caption(image_path, target_lang='fr')
    return render_template('index.html', caption=caption)

if __name__ == '__main__':
    app.run(debug=True)