#In Progress

import os  
import tkinter as tk
from tkinter import *
from tkinter import StringVar  
from tkinter import ttk     ## ttk is the Python binding to the newer "themed widgets" added in Tk version 8.5
from tkinter import filedialog
from tkinter.ttk import *   # for defining style
import sklearn
import pickle
import pandas as pd
import numpy as np
#from tkcalendar import Calendar, DateEntry

try:                        #(this for Win10 thats why its mentioned as try - to avoid errors in Linux,Mac,etc.)
   from ctypes import windll     #this part is maximazing pixels in texts 
   windll.shcore.SetProcessDpiAwareness(1)
except:
   pass

gui = tk.Tk()

gui.geometry("600x600")
gui.title("Predicting Bank Loan Status")
gui.minsize(600, 600)
gui.resizable(False, False)
gui.columnconfigure((0,4), weight=60)
gui.rowconfigure((0,30), weight=60)

s = ttk.Style()
s.theme_use("default")

Name_Surname = tk.StringVar(gui, value = 'e.g. David Mahhoson')
model_path = tk.StringVar(gui, value = r'Example: C:\Users\David\Desktop\BSrev_rf.pkl')
scaler_path = tk.StringVar(gui, value = r'Example: C:\Users\David\Desktop\scaler.pkl')
predict_text = tk.StringVar(gui, value = ' ')

var = tk.DoubleVar()
cu_score = tk.StringVar()
def sel():
    selection = "Credit Score = " + str(var.get())
    #label.config(text = selection)
    cu_score.set(selection)

   
combo_credit_score = Combobox(gui)

Credit_Score_list = range(0,8000)
combo_credit_score['values']= Credit_Score_list
combo_credit_score.current(0) #setting default value
def get_cred_score_cb():
    global Credit_Score
    Credit_Score = combo_credit_score.get()

       

def get_model_path():
       global model_name
       file = filedialog.askopenfilename(filetypes = (("Saved Models","*.pkl"),("all files","*.*")))
       model_path.set(file)
       folder_path = os.path.dirname(os.path.abspath(file))   #formatting to 'T:\\Data\\DBDesign'
       os.chdir (folder_path)  #Setting Working Directory
       cwd = os.getcwd()
       #print(f"Current WD set as: {cwd}")
       model_letters_count = (len(folder_path) - len(file))+1
       model_name = file[model_letters_count:]
       #print(f"model name is: {model_name}")

def get_scaler_path():
       global scaler_name
       file = filedialog.askopenfilename(filetypes = (("Saved Scalers","*.pkl"),("all files","*.*")))
       scaler_path.set(file)
       folder_path = os.path.dirname(os.path.abspath(file))   #formatting to 'T:\\Data\\DBDesign'
       os.chdir (folder_path)  #Setting Working Directory
       cwd = os.getcwd()
       #print(f"Current WD set as: {cwd}")
       scaler_letters_count = (len(folder_path) - len(file))+1
       scaler_name = file[scaler_letters_count:]
       #print(f"model name is: {scaler_name}")




def predict_clicked(*args):
       get_cred_score_cb()  
       Credit_Score_feat =  int(var.get())
       print (f"Credit score is : {Credit_Score_feat}")
       print(type(Credit_Score_feat))

       sc_file = pickle.load(open(scaler_name, "rb"))
       
       
       scaler_result = sc_file.transform([[445412, 709, 1167493, 8, 17.2, 1, 228190, 1, 0]])
       term_arr = np.array([[0.0 , 1.0 ]])
       pred_input = np.concatenate((term_arr, scaler_result), axis=None)

       model = pickle.load(open(model_name, "rb"))
       prediction = model.predict([pred_input])

       result = f"Result is {prediction}"
       predict_text.set(result)


'''
       Short_term = 0.0
       Long_term = 1.0
       Loan_Amount = -0.40188364926595954
       Credit_Score_feat =  int(var.get())
       print(Credit_Score_feat)
       print(type(Credit_Score_feat))
       print("*************")
       Annual_Income = 0.34743006086034717
       Years_current_job = 0.34743006086034717
       Years_Credit_History = 0.34743006086034717
       Number_Credit_Problems = 0.34743006086034717
       Current_Credit_Balance  = 0.34743006086034717
       Bankruptcies = 0.34743006086034717
       Tax_Liens  = 0.34743006086034717             




       prediction=model.predict([[
           Short_term,
           Long_term,
           Loan_Amount,
           Credit_Score_feat,
           Annual_Income,
           Years_current_job,
           Years_Credit_History,
           Number_Credit_Problems,
           Current_Credit_Balance,
           Bankruptcies,
           Tax_Liens
           ]])
'''


       

#Gui Application Details 
tk.Label(gui,text="           ").grid(row=0,column=0)
tk.Label(gui,text="           ").grid(row=0,column=1)
tk.Label(gui,text="           ").grid(row=0,column=2)
tk.Label(gui,text="           ").grid(row=0,column=3)
tk.Label(gui,text="           ").grid(row=0,column=4)

tk.Label(gui,text="Customer Name and Surname").grid(row=1,column=1)
#tk.Button(gui, text="Calendar",command=get_dep_date,bg="azure3").grid(row=1,column=3)
Entry(gui,textvariable=Name_Surname).grid(row=1,column=3)
tk.Label(gui,text="         ").grid(row=2,column=1)

tk.Label(gui,text="Customer's Credit Score: ").grid(row=3,column=1)
#Entry(gui,textvariable=departure_time_var).grid(row=3,column=3)
tk.Scale(gui, variable = var, from_=0, to=8000, orient=HORIZONTAL).grid(row=3, column=3)
tk.Button(gui, text="Get Scale Score",command=sel,bg="azure3").grid(row=4,column=3)
#tk.Label(gui,text="         ").grid(row=5,column=1)
tk.Label(gui,textvariable=cu_score, fg= "green",).grid(row=5,column=3)
tk.Label(gui,text="         ").grid(row=7,column=1)

tk.Button(gui, text="Select Saved Model",command=get_model_path,bg="azure3").grid(row=15,column=1)
tk.Label(gui,textvariable=model_path, fg='RoyalBlue4').grid(row=16,column=1, columnspan=3)
tk.Label(gui,text="         ").grid(row=17,column=1)
tk.Button(gui, text="Select Saved Scaler",command=get_scaler_path,bg="azure3").grid(row=18,column=1)
tk.Label(gui,textvariable=scaler_path, fg='RoyalBlue4').grid(row=19,column=1, columnspan=3)
tk.Label(gui,text="         ").grid(row=20,column=1)

tk.Button(gui, text="Predict", command=predict_clicked, bg="white").grid(row=21,column=1)
tk.Button(gui,text="Quit", command=gui.destroy, bg="white").grid(row=21,column=3)
tk.Label(gui,text="         ").grid(row=22,column=1)

tk.Label(gui,textvariable=predict_text, fg= "red", font=("Arial Bold", 15)).grid(row=20,column=1, columnspan=3)

gui.mainloop()
