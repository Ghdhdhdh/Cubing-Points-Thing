from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/submit')
def submitting():
    score = int(request.args.get('time')) * 0.9
    team = request.args.get('team')

    

    with open(team+'.txt', 'r') as f:
        current_score = f.read()

    with open(team+'.txt', 'w') as f:
        f.write(str(int(current_score) + score))

    return render_template('submited.html', points=str(score))






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)