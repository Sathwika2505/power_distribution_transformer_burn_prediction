
from data_preprocessing import data_preprocess
from sklearn import preprocessing

def feature_engineering():
    data = data_preprocess()
    cols = ['Type of clients', 'Type of installation']
    for col in cols:
        label_encoding = preprocessing.LabelEncoder()
        data[col] = label_encoding.fit_transform(data[col])
        print(data[col].unique())
    data.to_csv('power_distribution_transformer_burn_prediction.csv', index=False)

    print(data.dtypes)

    return data
feature_engineering()

