import os
import pandas as pd
import plotly.graph_objects as go
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)
dir = os.path.join(app.root_path, 'static')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["csv_file"]
        if file:
            filepath = os.path.join("data.csv")
            file.save(filepath)
            df = pd.read_csv(filepath)

            fig1 = plot_all_values(df)
            fig2 = plot_first_X_values(df)
            fig3 = plot_last_Y_values(df)

            fig1.write_html(os.path.join(dir, "plot1.html"))
            fig2.write_html(os.path.join(dir, "plot2.html"))
            fig3.write_html(os.path.join(dir, "plot3.html"))

            return render_template("index.html", plot1="static/plot1.html", plot2="static/plot2.html", plot3="static/plot3.html")
    
    return render_template("index.html")


def plot_all_values(df):
    fig = go.Figure()
    for column in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[column], mode='lines', name=column))
    
    fig.update_layout(title="Toate Valorile", xaxis_title="Index", yaxis_title="Values")
    return fig


def plot_first_X_values(df):
    fig = go.Figure()
    for column in df.columns:
        fig.add_trace(go.Scatter(x=df.head(8).index, y=df.head(8)[column], mode='lines', name=column))
    
    fig.update_layout(title="Primele X Valori", xaxis_title="Index", yaxis_title="Values")
    return fig


def plot_last_Y_values(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.tail(24).index, y=df.tail(24)['Durata'], mode='lines', name="Durata"))
    fig.add_trace(go.Scatter(x=df.tail(24).index, y=df.tail(24)['Puls'], mode='lines', name="Puls"))
    
    fig.update_layout(title="Ultimele Y Valori", xaxis_title="Index", yaxis_title="Values")
    return fig


# Static route to serve files
@app.route('/static/<filename>')
def upload_file(filename):
    return send_from_directory(dir, filename)


if __name__ == "__main__":
    app.run(debug=True)
