from tkinter import StringVar, Label, Entry, OptionMenu, Button,  LEFT, W, Tk, Text

from functions import decision_tree, random_forest, naive_bayes
from const import SYMPTOMS

if  __name__ == "__main__":
    # Gui_stuff-------------------------------
    # Creates the main window of the GU
    root=Tk()
    root.configure()

    # Entry variables 
    Symptom1=StringVar()
    Symptom1.set(None)
    Symptom2=StringVar()
    Symptom2.set(None)
    Symptom3=StringVar()
    Symptom3.set(None)
    Symptom4=StringVar()
    Symptom4.set(None)
    Symptom5=StringVar()
    Symptom5.set(None)
    Name=StringVar()
    
    # Headings
    w2 = Label(root, justify = LEFT, text = "Diseases Predictor using Machine Learning")
    w2.config(font = ("Elephant",30))
    w2.grid(row = 1, column = 0, columnspan = 4, padx = 100)
    w2 = Label(root, justify = LEFT, text = "A Project by Aya Samir", fg = "white", bg = "blue")
    w2.config(font=("Aharoni", 30))
    w2.grid(row = 2, column = 0, columnspan = 2, padx = 100)

    # Labels
    NameLb = Label(root, text = "Name of the Patient", fg = "yellow", bg = "black")
    NameLb.grid(row = 6, column = 0, pady = 15, sticky = W)

    S1Lb = Label(root, text = "Symptom 1", fg = "yellow", bg = "black")
    S1Lb.grid(row = 7, column = 0, pady = 10, sticky = W)

    S2Lb = Label(root, text = "Symptom 2", fg = "yellow", bg = "black")
    S2Lb.grid(row=8, column=0, pady=10, sticky=W)

    S3Lb = Label(root, text = "Symptom 3", fg = "yellow", bg = "black")
    S3Lb.grid(row=9, column=0, pady=10, sticky=W)

    S4Lb = Label(root, text = "Symptom 4", fg = "yellow", bg = "black")
    S4Lb.grid(row = 10, column = 0, pady = 10, sticky = W)

    S5Lb = Label(root, text="Symptom 5", fg="yellow", bg="black")
    S5Lb.grid(row = 11, column = 0, pady = 10, sticky = W)

    lrLb = Label(root, text="DecisionTree", fg="white", bg="red")
    lrLb.grid(row = 15, column = 0, pady = 10,sticky = W)

    destreeLb = Label(root, text = "RandomForest", fg = "white", bg = "red")
    destreeLb.grid(row = 17, column = 0, pady = 10, sticky = W)

    ranfLb = Label(root, text = "NaiveBayes", fg = "white", bg = "red")
    ranfLb.grid(row = 19, column = 0, pady = 10, sticky = W)

    # Entries
    OPTIONS = sorted(SYMPTOMS)

    NameEn = Entry(root, textvariable=Name)
    NameEn.grid(row = 6, column = 1)

    S1En = OptionMenu(root, Symptom1, *OPTIONS)
    S1En.grid(row=7, column = 1)

    S2En = OptionMenu(root, Symptom2, *OPTIONS)
    S2En.grid(row = 8, column = 1)

    S3En = OptionMenu(root, Symptom3, *OPTIONS)
    S3En.grid(row = 9, column = 1)

    S4En = OptionMenu(root, Symptom4, *OPTIONS)
    S4En.grid(row = 10, column = 1)

    S5En = OptionMenu(root, Symptom5, *OPTIONS)
    S5En.grid(row = 11, column = 1)

    dst = Button(root, text = "DecisionTree", command=decision_tree, bg = "green", fg = "yellow")
    dst.grid(row = 8, column = 3,padx = 10)

    rnf = Button(root, text = "Randomforest", command = random_forest, bg = "green", fg = "yellow")
    rnf.grid(row = 9, column = 3,padx = 10)

    lr = Button(root, text = "NaiveBayes", command = naive_bayes, bg = "green", fg = "yellow")
    lr.grid(row = 10, column = 3,padx = 10)

    # Textfileds
    t1 = Text(root, height = 1, width = 40, bg = "orange", fg = "black")
    t1.grid(row = 15, column = 1, padx = 10)

    t2 = Text(root, height = 1, width = 40, bg = "orange", fg = "black")
    t2.grid(row = 17, column = 1 , padx = 10)

    t3 = Text(root, height = 1, width = 40, bg="orange", fg = "black")
    t3.grid(row = 19, column = 1 , padx = 10)

    # To enter and run GUI 
    root.mainloop()