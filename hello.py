from flask import Flask, render_template
from markupsafe import escape

app=Flask(__name__)
servers = ["Claudio", "Gilberto", "Jorge"]
@app.route("/")
def index():
    return render_template("index.html", servidores=len(servers))
@app.route("/tema/<charla>/<predicador>/")
def predica(charla, predicador):
    return render_template("tema.html", subject=charla, servent=predicador)
@app.route("/admin/retiro/")
@app.route("/admin/retiro/<int:retiro_id>/")
def Retiro(retiro_id=None):
    return render_template("admin/retiro.html", convi_id=retiro_id)
@app.route("/about")
def sobreNosotros():
    return f"Somos un grupo catolico"
@app.route("/contact")
def Contactenos():
    return f"Envienos un email"
if __name__ == "__main__":
    app.run(port=4000, debug=True) 
