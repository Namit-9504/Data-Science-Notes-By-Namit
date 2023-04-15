from flask import Flask ,request ,render_template , jsonify

app1 = Flask(__name__)

@app1.route('/')
def home_page():
    return render_template('index.html')


@app1.route('/postman_action',methods=['POST'])
def math_ops1():
    if(request.method=='POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The addition of  " + str(num1)+ " and " + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtraction of  " + str(num1)+ " and " + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiplication of  " + str(num1)+ " and " + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The division  of  " + str(num1)+ " and " + str(num2) + " is " + str(r)
        if ops == 'log':
            r = num1+num2
            result = "The addition of  " + str(num1)+ " and " + str(num2) + " is " + str(r)



        return jsonify(result)



if __name__=="__main__":
    app1.run(host="0.0.0.0")
