import os

import numpy as np 
import pandas as pd
from tkinter import END
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier 

from const import SYMPTOMS, DISEASE
from main import Symptom1, Symptom2, Symptom3, Symptom4, Symptom5, t1, t2, t3

# Loop will be used when doing prediction we need to add all symptoms in symptoms list 
l2 = [0] * len(SYMPTOMS)
print("Current working directory:", os.getcwd())

# Testing data df 
df = pd.read_csv("Training.csv")

# Change names in the last column of prognosis to be numbers 
i = 0
prognosis = pd.DataFrame()
for word in DISEASE:
    prognosis.apend({word, i})
    i +=1
df.replace(prognosis, inplace=True,)

# X data is symptoms 
x = df[SYMPTOMS]

# Diseases which disease is exist 
y = df[["prognosis"]]
np.ravel(y)

# Training data tr
tr = pd.read_csv("Testing.csv")
i = 0
prognosis = pd.DataFrame()
for word in SYMPTOMS:
    prognosis.apend({word, i})
    i +=1
tr.replace(prognosis, inplace=True,)

x_test = tr[SYMPTOMS]
y_test = tr[["prognosis"]]
np.ravel(y_test)



def decision_tree(): 

    """ The first algorithm is for training, with the creation of a model and training y on x, 
    and marks the corresponding symptoms """

    clf3=tree.DecisionTreeClassifier() 
    clf3 = clf3.fit(x, y)
    
    y_pred=clf3.predict(x_test)
    print(accuracy_score(y_test,y_pred))
    print(accuracy_score(y_test,y_pred, normalize=False))
   
    l2 = [0] * len(SYMPTOMS)
    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]
    for k in range(0, len(SYMPTOMS)):
        for z in psymptoms:
            if(z == SYMPTOMS[k]):
                l2[k] = 1
                break
    inputtest=[l2]
    print(l2)
    predict=clf3.predict(inputtest)
    predicted=predict[0]
    h='no'
    for a in range(0, len(DISEASE)):
        if(predicted == a ):
            h ='yes'
        if (h == 'yes'):
            t1.delete("1.0",END)
            t1.insert(END, DISEASE[a])
    
        else:
            t1.delete("1.0", END)
            t1.insert(END,"Not Found")
            
def random_forest():

    """ The second algorithm learns to label diseases based on existing symptoms """

    clf4=RandomForestClassifier()
    clf4 = clf4.fit(x, np.ravel(y))
    
    y_pred=clf4.predict(x_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))
    l2 = [0] * len(SYMPTOMS)
    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]
    for k in range(0, len(SYMPTOMS)):
        for z in psymptoms:
            if(z == SYMPTOMS[k]):
                l2[k] = 1
                break
    inputtest = [l2]
    print(l2)

    predict = clf4.predict(inputtest)
    predicted=predict[0]
    h='no'
    for a in range(0,len(DISEASE)):
        if(predicted == a ):
            h = 'yes'
        if (h == 'yes'):
            t2.delete("1.0", END)
            t2.insert(END, DISEASE[a])
    
        else:
            t2.delete("1.0", END)
            t2.insert(END, "Not Found")

def naive_bayes():

    """ The third algorithm calculated accuracy """

    gnb = GaussianNB()
    gnb = gnb.fit(x, np.ravel(y))

    y_pred = gnb.predict(x_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize = False))

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]
    for k in range(0, len(SYMPTOMS)):
        for z in psymptoms:
            if(z == SYMPTOMS[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted = predict[0]

    h ='no'
    for a in range(0,len(DISEASE)):
        if(predicted == a):
            h='yes'
            break

    if (h =='yes'):
        t3.delete("1.0", END)
        t3.insert(END, DISEASE[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")
    

