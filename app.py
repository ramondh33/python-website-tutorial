from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1, 
        'title': 'Data Analyst', 
        'location': 'Miami, Fl', 
        'salary': '120,000'
    }, 
    { 
        'id': 2, 
        'title': 'Data Engineer', 
        'location': 'Tampa, Fl', 
        'salary': '180,000'
    }, 
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Miami, Fl',
        'salary': '200,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Miami, Fl',
        'salary': '200,000'
    },
]
COMPANY_NAME = 'Apple'

@app.route('/')

def hello_world():
    return render_template('index.html', jobs=JOBS, company_name=COMPANY_NAME)

@app.route('/api/jobs')

def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)