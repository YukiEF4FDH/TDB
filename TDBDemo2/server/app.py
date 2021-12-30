import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

SEC1_TEXT0_MD = [
    {
        'CONTENT': 'Sec1-Text0-MD: This <ref>is</ref> the updated *text* content !!!',
    },
]
	
@app.route('/sec1-text0-md', methods=['GET']) # Test for markdown text to html
def sec1_text0_md():
	return jsonify(SEC1_TEXT0_MD);

SEC2_TEXT0_MD = [
    {
        'CONTENT': 'Sec2-Text0-MD: This <ref>is</ref> the updated *text* content !!!',
    },
]
	
@app.route('/sec2-text0-md', methods=['GET']) # Test for markdown text to html
def sec2_text0_md():
	return jsonify(SEC2_TEXT0_MD);

df = pd.read_csv (r'F1A_Data.csv',header=0)
total = df.sum(axis=1)
print(total)
df['total'] = total
f1a = df.to_json (orient='records',force_ascii=False)
	
@app.route('/f1a-json', methods=['GET']) # Test for Json loading
def f1a_json():
	return jsonify(f1a);

df2 = pd.read_csv (r'F2A_Data.csv',header=0)
total2 = df2.sum(axis=1)
df2['total'] = total2
f2a = df2.to_json (orient='records',force_ascii=False)

@app.route('/f2a-json', methods=['GET']) # Test for Json loading
def f2a_json():
    return jsonify(f2a);

df2_1 = pd.read_csv (r'F2A-1_Data.csv',header=0)
f2a_1 = df2_1.to_json (orient='records',force_ascii=False)

@app.route('/f2a_1-json', methods=['GET']) # Test for Json loading
def f2a1_json():
    return jsonify(f2a_1);

df3 = pd.read_csv (r'F3A_Data.csv',header=0)
f3a = df3.to_json (orient='records',force_ascii=False)

@app.route('/f3a-json', methods=['GET']) # Test for Json loading
def f3a_json():
    return jsonify(f3a);
	
if __name__ == '__main__':
    app.run()