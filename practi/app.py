from flask import Flask,render_template,request,jsonify

app  = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        eamil = request.form.get('email')
        phn = request.form.get('phn')
        psw = request.form.get('psd')
        cspws = request.form.get('cpsd')
        gender = request.form.get('gender')
        
        if psw != cspws:
            return jsonify({'error': 'password does not match'})
        print(f"user register : {name} , {eamil}")
        
        return jsonify({'message': 'Registration successful!'})

    return render_template('index.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5005, debug=True)