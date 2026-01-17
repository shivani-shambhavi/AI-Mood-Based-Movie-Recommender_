
import pandas as pd
def load_data(path):
    df=pd.read_csv(path)
    df['text']=df['emotion'].astype(str)+" "+df['description'].astype(str)
    return df
