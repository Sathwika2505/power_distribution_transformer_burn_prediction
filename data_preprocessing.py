import pandas as pd
from data_extraction import data_extraction
from sklearn import preprocessing

def data_preprocess():
    data= data_extraction()
    data.rename(columns={'Average earth discharge density DDT [Rays/km^2-año]' : 'Average earth discharge density', 'Maximum ground discharge density DDT [Rays/km^2-año]' : 'Maximum ground discharge density', 'Burning rate  [Failures/year]' : 'Burning rate', 
                         'Criticality according to previous study for ceramics level' : 'Criticality from previous study', 'Electric power not supplied EENS [kWh]' : 'Electric power not supplied'}, inplace=True)
    print(data.columns)
    cols = ['Type of clients', 'Type of installation']
    for col in cols:
        label_encoding = preprocessing.LabelEncoder()
        data[col] = label_encoding.fit_transform(data[col])
        print(data[col].unique())
        
    return data

data_preprocess()