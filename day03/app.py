from flask import Flask, request, render_template

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    # request.args.get('파라미터명')
    # request.args -> flask가 client로부터 받은 파라미터를 담는 Dictionary(Immutable)
    student = request.args.get('student')
    return {'hello': student}

# 주소 자체에 parameter 심어놓기
@app.route('/<day>')
def toons(day):
    return{ 'today is': day}