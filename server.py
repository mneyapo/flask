# Import Flask, the Python micro web framework
from flask import Flask, render_template
from flask import request, redirect
import cgi
form = cgi.FieldStorage()

# Create the application instance
app = Flask(__name__, template_folder="templates")

#BADGE="A04748A04748A047"
# Create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "home.html"
    """
    return render_template("home.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['projectFilepath']
    processed_text = text.upper()
    return processed_text
    #return render_template("result.html",result = result)

@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():
    projectpath = request.form['projectFilepath']
    result="BAD "
    return result

@app.route('/result',methods = ['POST', 'GET'])
def result():
    result = request.form['projectFilepath']
    if request.method == "POST":
        result = request.form['projectFilepath']
        #return redirect(request.url)
    result = request.args.get('projectFilepath')
    print(result)
    return render_template("result.html",result = result)

if __name__ == "__main__":
    try:
        app.run(debug=True)
        searchterm =  form.getvalue('projectFilepath')
        print(searchterm)
    except (SystemExit, MemoryError, KeyboardInterrupt):
         pass 
    # We can do something here if needed
    # But if we don't catch these safely, the script will crash
print ('This is printed when the window is closed!')
