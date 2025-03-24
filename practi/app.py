# from flask import Flask,render_template,request,jsonify

# app  = Flask(__name__)

# @app.route('/', methods = ['GET','POST'])
# def register():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         eamil = request.form.get('email')
#         phn = request.form.get('phn')
#         psw = request.form.get('psd')
#         cspws = request.form.get('cpsd')
#         gender = request.form.get('gender')
        
#         if psw != cspws:
#             return jsonify({'error': 'password does not match'})
#         print(f"user register : {name} , {eamil}")
        
#         return jsonify({'message': 'Registration successful!'})

#     return render_template('index.html')
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5050, debug=True)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        print(f"Received: Name={name}, Email={email}, Password={password}")

        return render_template('success.html')

    return render_template('index.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)