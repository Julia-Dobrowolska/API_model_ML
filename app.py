
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/api/v1.0/predict", methods=['GET'])
def wyznaczenie_predykcji():
    num1 = float(request.args.get("num1", 0))
    num2 = float(request.args.get("num2", 0))

    if sum([num1, num2]) > 5.8:
        wartość_predykcji = 1
    else:
        wartość_predykcji = 0

    return {"prediction": wartość_predykcji, "features": {"num1": num1, "num2": num2}}

if __name__ == '__main__':
    app.run(port=5001)
