from flask import Flask,render_template,url_for,request
app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def addition():
	return render_template('form.html')
	
@app.route('/answer',methods=['POST','GET'])
def answer():
	if request.method=='POST':
		num1=request.form['n1']
		num2=request.form['n2']
		num3=int(num1)+int(num2)
		return render_template('result.html',num1=num1,num2=num2,num3=num3)

if __name__=='__main__':
	app.run(debug=True)