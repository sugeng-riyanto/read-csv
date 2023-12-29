from flask import Flask, render_template, request
import csv
import io
import random  # Import random module for generating sample data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')
        
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', message='No selected file')
        
        if file:
            data = []
            # Read the CSV file
            stream = io.StringIO(file.stream.read().decode('UTF-8'), newline=None)
            csv_input = csv.reader(stream)
            for row in csv_input:
                data.append(row)
            
            headers = data[0]
            rows = data[1:]
            
            return render_template('index.html', headers=headers, rows=rows)
    return render_template('index.html', message='Error uploading file')

# New route to generate and display sample data
@app.route('/generate_sample')
def generate_sample():
    # Generate 100 samples of synthetic CSV data
    data = [['Column A', 'Column B', 'Column C']]  # Headers
    for i in range(100):
        row = [random.randint(1, 100) for _ in range(3)]  # Generating random data for 3 columns
        data.append(row)

    headers = data[0]
    rows = data[1:]

    return render_template('index.html', headers=headers, rows=rows)

if __name__ == '__main__':
    app.run(debug=True)

