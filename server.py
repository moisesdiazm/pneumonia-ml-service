import os
from flask import Flask, request, jsonify
from predictive_model.query_model import KerasModel

app = Flask(__name__)
app.config['UPLOAD_PATH'] = os.getcwd() + "/temporal"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
pneumonia_predictor = KerasModel(os.getcwd() + "/predictive_model/model.json", os.getcwd() + "/predictive_model/model.h5")

@app.route('/analyze', methods=['POST'])
def analyze():
    images = []
    for filename,f in request.files.items():
        image_path = os.path.join(app.config['UPLOAD_PATH'], filename)
        f.save(image_path)
        images.append(image_path)
    
    result = pneumonia_predictor.predict_multiple(images)
    
    for filename,f in request.files.items():
        image_path = os.path.join(app.config['UPLOAD_PATH'], filename)
        os.remove(image_path)

    return jsonify({'results': list(result)})

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")