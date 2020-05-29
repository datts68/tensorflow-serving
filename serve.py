import json

from flask import Flask, request

from utils import grpc_infer, convert_image

app = Flask(__name__)


@app.route('/api/tlai', methods=['POST'])
def hello():
    encoded_img = request.values['encoded_image']
    img = convert_image(encoded_img)

    result = grpc_infer(img)
    return json.dumps(
        {
            "code": 200,
            "result": result.tolist()
        }
    )


if __name__ == '__main__':
    app.run(debug=True, host="10.10.10.4", port=5000)