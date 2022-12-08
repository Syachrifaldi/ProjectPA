from flask import Flask, render_template, request, redirect, url_for, g
import pickle
import numpy as np
import pandas as pd
from model import load, user, prediksi

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

global data, software, biaya

load()

@app.route('/build', methods=['GET','POST'])
def build():
    if request.method == 'POST':
        applist = request.form.getlist('category')
        budgetlist = request.form.getlist('budget')
        # user(applist, budgetlist)
        return redirect(url_for('predict',app_list=applist,budget_list=budgetlist))
    else:
        return render_template('screen2.html',request_method=request.method)


# def load():
#     global data
#     data = pickle.load(open('static/model/dataset.pkl', 'rb'))


@app.route('/build/predict/<app_list>/<budget_list>')
def predict(app_list,budget_list):
    # global software = app_list
    # global biaya = budget_list
    # model = pickle.load(open('static/model/model.pkl', 'rb'))
    # aplikasi = pickle.load(open('static/model/aplikasi.pkl','rb'))
    # budget = pickle.load(open('static/model/budget.pkl','rb'))
    # laptop = pickle.load(open('static/model/laptop.pkl','rb'))
    # word = ""
    # stat = 0
    # listapp = []
    # for i in app_list:
    #     if i == "'" and stat==0:
    #         stat = 1
    #     elif i == "'" and stat==1:
    #         listapp.append(word)
    #         stat = 0
    #         word = ""
    #     elif i != "[" and i != ']' and i != ',':
    #         word = word + i
    # kata = listapp[1]
    # kata = kata[1:]
    # listapp[1] = kata
    # kata = listapp[2]
    # kata = kata[1:]
    # listapp[2] = kata
    # app1 = aplikasi.transform([listapp[0]])
    # app2 = aplikasi.transform([listapp[1]])
    # app3 = aplikasi.transform([listapp[2]])
    # bud = budget.transform([str(budget_list)])
    # rekomendasi = model.predict([[int(app1),int(app2),int(app3),int(bud)]])
    # reklaptop = laptop.inverse_transform([rekomendasi])
    
    # for a in reklaptop:
    #     index = data[data['brand']==a].index.values[0]
    
    # kol1 = data.loc[index,'processor_brand']
    # kol2 = data.loc[index,'processor_name']
    # kol3 = data.loc[index,'graphic']
    # kol4 = data.loc[index,'ram_gb']
    # kol5 = data.loc[index,'ram_type']
    # kol6 = data.loc[index,'ssd']
    # kol7 = data.loc[index,'hdd']
    # kol8 = data.loc[index,'os']
    # kol9 = data.loc[index,'battery']
    # kol10 = data.loc[index,'display_size']
    # kol11 = data.loc[index,'price']

    # inputan = user()
    hasil_rekomendasi = prediksi(app_list, budget_list)
    dataset = pickle.load(open('static/model/dataset.pkl', 'rb'))
    
    for a in hasil_rekomendasi:
        index = dataset[dataset['brand']==a].index.values[0]
    kol1 = dataset.loc[index,'processor_brand']
    kol2 = dataset.loc[index,'processor_name']
    kol3 = dataset.loc[index,'graphic']
    kol4 = dataset.loc[index,'ram_gb']
    kol5 = dataset.loc[index,'ram_type']
    kol6 = dataset.loc[index,'ssd']
    kol7 = dataset.loc[index,'hdd']
    kol8 = dataset.loc[index,'os']
    kol9 = dataset.loc[index,'battery']
    kol10 = dataset.loc[index,'display_size']
    kol11 = dataset.loc[index,'price']
    
    return render_template('screen3.html', hasil = hasil_rekomendasi,  kol_1=kol1, kol_2 = kol2, kol_3 =kol3, kol_4=kol4, kol_5=kol5, kol_6=kol6, kol_7=kol7, kol_8=kol8, kol_9=kol9, kol_10=kol10, kol_11=kol11)
           
  
# @app.route('/list_user')
# def show_data():
#     build()
#     return g.software, g.biaya

# show_data()

@app.route('/build/predict/<app_list>/<budget_list>/<recommendations>/<reklaptop>')
def recommendations( reklaptop,number_of_recommendations = 3):
    cosine = pickle.load(open('static/model/cosine.pkl','rb'))
    index = data[data['brand']==reklaptop].index.values[0]
    similarity_scores = list(enumerate(cosine[index]))
    similarity_scores_sorted = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommendations_indices = [t[0] for t in similarity_scores_sorted[1:(number_of_recommendations+1)]]
    # lappy = 1
    
    for i in recommendations_indices:
        next = print((data['brand'].iloc[i]))
        
    return render_template('screen4.html', hasil=next )


if __name__ == "__main__":
    app.run()
