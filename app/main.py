from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Service is Ready! (v3)"

@app.route('/predict', methods=['POST'])
def predict():
    # Получаем данные от клиента
    data = request.json
    number = data.get('number', 0)
    
    # Имитируем работу тяжелой AI модели (ждем 1 секунду)
    # На реальном GPU тут был бы вызов model.generate()
    time.sleep(1)
    
    # "Предсказание"
    result = number * number
    
    return jsonify({
        "input": number,
        "prediction": result,
        "status": "success",
        "model": "fake-gpu-model-v1"
    })

if __name__ == '__main__':
    # Запускаем сервер на порту 5000 и слушаем всех (0.0.0.0)
    app.run(host='0.0.0.0', port=5000)
