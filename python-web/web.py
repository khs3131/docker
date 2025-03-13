# chatGPT 작품 입니다.
# 기본적인 웹서버 이며 80포트를 이용하여 외부에서 웹 접속이 가능합니다. 
# 3000번 포트 /metrics 경로를 이용하여 메트릭을 수집합니다(근데 3000번은 잘 안되고 80으로는 잘되네)

from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Metrics 엔드포인트에 대한 경로 설정
metrics.info('app_info', 'Application Information', version='1.0.0')

# 80포트에 웹 서버 라우트
@app.route('/')
def home():
    return 'Hello, this is the home page!'
    return 'Python and Docker'

# /metrics 엔드포인트에 대한 라우트
@app.route('/metrics')
def metrics_route():
    return jsonify({
        'status': 'success',
        'message': 'Metrics are available on this endpoint.'
    })

if __name__ == '__main__':
    # 80포트에 웹 서버 실행
    app.run(host='0.0.0.0', port=80)