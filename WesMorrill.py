from flask import Flask, send_from_directory, render_template
import requests
import xml.etree.ElementTree as ET
import json
app = Flask(__name__)

@app.route("/")
def hello():
    url = "http://gateway-a.watsonplatform.net/calls/url/URLGetEmotion"

    querystring = {"api_key":"4d1bc45dacc0540817699070700a9c626cdec654","url":"www.linkedin.com/in/evancole1"}

    payload = ""
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "ee296e1e-1aa2-d7e4-fd95-7e55198a8626"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    root = ET.fromstring(response.content)
    docEmotions = {}
    docEmotions['anger'] = root[5][0].text
    docEmotions['disgust'] = root[5][1].text
    docEmotions['fear'] = root[5][2].text
    docEmotions['joy'] = root[5][3].text
    docEmotions['sadness'] = root[5][4].text
    docEmotionsText = json.dumps(docEmotions);

    return render_template('WesMorrill.html', docEmotions=docEmotionsText)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == "__main__":
    app.run()
