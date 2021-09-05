from  flask import request,render_template,Flask
import requests
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather',methods=['POST','GET'])
def weather():
    url='http://api.openweathermap.org/data/2.5/weather?q={},india&APPID=aac677282727107540ca7a173c69cfca'
    city=request.form['city']
    
    r=requests.get(url.format(city)).json()
    print(r)
    return render_template('result.html',data=r)

if(__name__=="__main__"):
    app.run(debug=True)