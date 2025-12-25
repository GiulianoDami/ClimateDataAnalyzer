from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
import matplotlib.pyplot as plt
import io
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        global df
        df = pd.read_csv(file) if file.filename.endswith('.csv') else pd.read_json(file)
        return redirect(url_for('analyze'))

@app.route('/analyze')
def analyze():
    if 'df' not in globals():
        return redirect(url_for('index'))
    stats = df.describe()
    return render_template('analyze.html', stats=stats.to_html())

@app.route('/generate_report')
def generate_report():
    if 'df' not in globals():
        return redirect(url_for('index'))
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Climate Data Analysis Report", ln=True, align='C')
    pdf.cell(200, 10, txt=df.describe().to_string(), ln=True, align='L')
    pdf.output("report.pdf")
    return send_file("report.pdf", as_attachment=True)

@app.route('/visualize')
def visualize():
    if 'df' not in globals():
        return redirect(url_for('index'))
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df[df.columns[0]], label=df.columns[0])
    plt.title('Trend Visualization')
    plt.xlabel('Index')
    plt.ylabel(df.columns[0])
    plt.legend()
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)