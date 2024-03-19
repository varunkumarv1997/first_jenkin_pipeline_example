from flask import Flask, render_template, Response
import time

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    def generate():
        count = 0
        while True:
            yield f"data: {count}\n\n"
            count += 1
            time.sleep(1)

    return Response(generate(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
