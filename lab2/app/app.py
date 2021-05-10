from flask import Flask, render_template, request, make_response
from numberValidation import checkLength, checkChars, formatNumber, formatNumberOut
import operator as op

app = Flask(__name__)
application = app

operations = ['+','-','*','/']

operations_functions = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/args')
def args():
    return render_template('args.html')

@app.route('/headers')
def headers():
    return render_template('headers.html')

@app.route('/cookies')
def cookies():
    resp = make_response(render_template('cookies.html'))
    if 'username' in request.cookies:
        resp.set_cookie('username', 'Some name', expires=0)
    else:
        resp.set_cookie('username', 'Some name')
    return resp

@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/calc')
def calc():
    try:
        result = None
        error_msg = None
        op1 = float(request.args.get('operand1'))
        op2 = float(request.args.get('operand2'))
        f = operations_functions[request.args.get('operation')]
        result = f(op1, op2)
    except ValueError:
        error_msg = 'Пожалуйста, вводите только числа'
    except ZeroDivisionError:
        error_msg = 'Нельзя делить на ноль!'
    except KeyError:
        error_msg = 'Недопустимая операция'
    except TypeError:
        pass
    return render_template('calc.html', operations=operations, result=result, error_msg=error_msg)

@app.route('/numbercheck', methods=['POST'])
def numbercheck():
    number = request.form.get('number')
    number = formatNumber(number)
    isLenghtRight = checkLength(number)
    isCharsRight = checkChars(number)
    if (isLenghtRight and isCharsRight):
        number=formatNumberOut(number)
        return render_template('numbercheck.html', number_res=number)
    elif (not isCharsRight and not isLenghtRight):
        return render_template('numbercheck.html', err_msg="Недопустимый ввод. В номере телефона встречаются недопустимые символы и введено неверное количество цифр.")
    elif (not isCharsRight):
        return render_template('numbercheck.html', err_msg="Недопустимый ввод. В номере телефона встречаются недопустимые символы.")
    elif (not isLenghtRight):
        return render_template('numbercheck.html', err_msg="Недопустимый ввод. Неверное количество цифр.")

@app.route('/numbercheck', methods=['GET'])
def numbercheckGet():
    # number = request.form.get('number')
    return render_template('numbercheck.html')
    


