from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('form.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
    
      return '<h1>file uploaded successfully</h1>'
   

		
if __name__ == '__main__':
   app.run(debug = True)