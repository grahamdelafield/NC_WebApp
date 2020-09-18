from flask import Flask, redirect, url_for, render_template, Response, send_file, jsonify
import pandas as pd
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("about.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def analysis():
    return render_template("data.html")

@app.route("/download")
def download():
    return render_template("download.html")

@app.route("/lab/<labname>")
def direct_to_lab(labname):
    labs = {
        'li':"https://www.lilabs.org",
        'odorico': "https://www.surgery.wisc.edu/research/researchers-labs/odorico/"
    }
    return redirect(labs[labname])

@app.route("/authors")
def authors():
    return render_template("authors.html")

@app.route("/all_data")
def ret_all_data():
    return send_file("data/test_file.zip")

@app.route('/download/<filename>', methods=['GET'])
def ret_file(filename):
    
    files = {
        'all_data': 'data/all_data.zip',
        'ecm_only': 'data/Identified ECM.xlsx',
        'ecm_quant': 'data/Quantified ECM and pairwise comparisons.xlsx',
        'protein': 'data/Identified proteins.xlsx',
        'protein_quant': 'data/Quantified proteins and pairwise comparisons.xlsx',
    }
    return send_file(files[filename], as_attachment=True, 
                     attachment_filename=files[filename][5:])

@app.route("/table.json")
def ret_table():
    df = pd.read_excel(r"C:\Users\graha\desktop\Code\Python\NC_WebApp\data\Pancreas proteome data summary_for searching.xlsx", skiprows=range(2))
    groups = {
        '1':'J vs F',
        '2':'Y vs F',
        '3':'O vs F',
        '4':'Y vs J',
        '5':'O vs J',
        '6':'O vs Y',
    }
    data = []
    for i in df.index:  
        sub = df.iloc[i, :18]
        columns = [c for c in sub.index]
        for i, c in enumerate(columns):
            if c[-2] == '.':
                lookup = c[-1]
                name = groups[lookup]+' '+c[:-2]
                columns[i] = name
        sub.index = columns
        # print((sub.to_dict()))
        data.append(sub.to_dict())
        to_dump = {'data':data}
    return jsonify(to_dump)

if __name__ == "__main__":
    app.run(debug=True)