import pickle

# global variable
global dataset, model, aplikasi, budget, laptop

def load():
    global dataset, model, aplikasi, budget, laptop
    dataset = pickle.load(open('static/model/dataset.pkl', 'rb'))
    model = pickle.load(open('static/model/model.pkl', 'rb'))
    aplikasi = pickle.load(open('static/model/aplikasi.pkl','rb'))
    budget = pickle.load(open('static/model/budget.pkl','rb'))
    laptop = pickle.load(open('static/model/laptop.pkl','rb'))
    
def user(applist, budgetlist):
    list_app = applist
    list_budget = budgetlist
    data = [[list_app, list_budget]]
    return data

def prediksi(app_list, budget_list):
    word = ""
    stat = 0
    listapp = []
    for i in app_list:
        if i == "'" and stat==0:
            stat = 1
        elif i == "'" and stat==1:
            listapp.append(word)
            stat = 0
            word = ""
        elif i != "[" and i != ']' and i != ',':
            word = word + i
    kata = listapp[1]
    kata = kata[1:]
    listapp[1] = kata
    kata = listapp[2]
    kata = kata[1:]
    listapp[2] = kata
    app1 = aplikasi.transform([listapp[0]])
    app2 = aplikasi.transform([listapp[1]])
    app3 = aplikasi.transform([listapp[2]])
    bud = budget.transform([str(budget_list)])
    rekomendasi = model.predict([[int(app1),int(app2),int(app3),int(bud)]])
    reklaptop = laptop.inverse_transform([rekomendasi])
    
    # for a in reklaptop:
    #     index = dataset[dataset['brand']==a].index.values[0]
    
    # kol1 = dataset.loc[index,'processor_brand']
    # kol2 = dataset.loc[index,'processor_name']
    # kol3 = dataset.loc[index,'graphic']
    # kol4 = dataset.loc[index,'ram_gb']
    # kol5 = dataset.loc[index,'ram_type']
    # kol6 = dataset.loc[index,'ssd']
    # kol7 = dataset.loc[index,'hdd']
    # kol8 = dataset.loc[index,'os']
    # kol9 = dataset.loc[index,'battery']
    # kol10 = dataset.loc[index,'display_size']
    # kol11 = dataset.loc[index,'price']
    
    # return a, kol1, kol2, kol3, kol4, kol5, kol6, kol7, kol8, kol9, kol10, kol11
    return reklaptop
