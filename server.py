from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    your_name = request.form['your_name']
    plus_one = request.form.get('plus_one', '')
    
    with open('rsvps.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([your_name, plus_one])
    
    return redirect('/confirm')

@app.route('/admin')
def admin():
    with open('rsvps.csv', newline='') as file:
        reader = csv.reader(file)
        rsvps = list(reader)
    return render_template('admin.html', rsvps=rsvps)

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

