from flask import Flask, jsonify, render_template, request, session
import pandas as pd # data wrangling

import numpy as np
import pandas as pd


app = Flask(__name__)

app.config['SECRET_KEY'] = 'pk'


@app.route('/informe')
def informe():
    inclinacion=session["inclinacion"]
    modlongitud=session["modlongitud"]
    peana=session["peana"]
    pretil=session["pretil"]
    latitud=session["latitud"]
    hp=session["hp"]
    dp=session["dp"]
    d0=session["d0"]
    di=session["di"]
    df=session["df"]

    #  devuelta navegador
    informe=render_template('notebook.html', inclinacion=inclinacion, L=modlongitud, latitud=latitud, p=peana, h0=pretil,  hp=hp,dp=dp, d0=d0,di=di, df=df)
    return jsonify( informe=informe)



@app.route('/formulario')
def formulario():
    # datos del navegador
    inclinacion = request.args.get('inclinacion', 0, type=int)
    modlongitud = request.args.get('modlongitud', 0, type=float)
    peana = request.args.get('peana', 0, type=float)
    pretil = request.args.get('pretil', 0, type=float)
    latitud = request.args.get('latitud', 0, type=float)
    # calculos


    df = pd.DataFrame(np.array([[29, 37, 39, 41, 43, 45 ], [1.600, 2.246, 2.475, 2.747, 3.078, 3.487 ]]),
                    index=['Latitud','k'])
    df=df.to_html()

    L=modlongitud
    hp=round(L*np.sin(inclinacion*np.pi/180),2)
    dp=round(L*np.cos(inclinacion*np.pi/180),2)


    h0 = pretil
    p= peana

    d0=h0/np.tan((61-latitud)*np.pi/180)
    d0=round(d0,2)

    di=(hp-p)/np.tan((61-latitud)*np.pi/180)
    di=round(di,2)

    #  figura

    # 
    session["inclinacion"]=inclinacion
    session["modlongitud"]=modlongitud
    session["peana"]=peana
    session["pretil"]=pretil
    session["latitud"]=latitud
    session["hp"]=hp
    session["dp"]=dp
    session["d0"]=d0
    session["di"]=di
    session["df"]=df



    return jsonify(d0=d0,di=di)



@app.route('/infor')
def infor():
    return render_template('informe.html')



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 8000,debug=True)
    