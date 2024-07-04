import pandas as pd

def data_extraction():
    df1 = pd.read_excel(r"Dataset_Year_2019.xlsx")
    #print("======================",df1.shape)
    df2 = pd.read_excel(r"Dataset_Year_2020.xlsx")
    #print(df2.shape)
    df1.rename(columns={'Burned transformers 2019' : 'Burned transformers'}, inplace=True)
    df2.rename(columns={'Burned transformers 2020' : 'Burned transformers'}, inplace=True)
    print(df2.columns)
    merged_df = pd.concat([df1, df2])
    #print("-------------",merged_df.shape)
    #print("-------------",merged_df.columns)
    merged_df.to_csv("df.csv")
    
    return merged_df

data_extraction()
    
    
    