##Building url dynamically
###variable rules and url building

 
from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/')
def index():
    return "Hello World"
@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is "+str(score)

@app.route('/result/<int:marks>')
def result(marks):
    if marks<50:
        result="fail"
    else:
        result="success"    
    return redirect(url_for(result,score=marks))    

if __name__=="__main__":
    app.run(debug=True)