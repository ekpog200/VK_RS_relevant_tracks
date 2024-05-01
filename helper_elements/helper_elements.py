import numpy as np
import pandas as pd
from collections import Counter, defaultdict

def count_na(df):
    """
    В данной функции мы будем считать кол-во нулевых значений у файла. Это информативнее, чем pd.value_counts
    
    input: dataframe
    output: если значение NA, то считает её
    """
    counter=pd.DataFrame(df.isnull().astype('int').sum(axis=0), columns=["Null_Count"]) # делаем датафрейм с NA_count
    counter['% Count']=df.isnull().astype('int').sum(axis=0)*100/len(df) # % от общего числа пустых
    return counter


def genres(genre_ids):
    '''
    У нас фича genre_id разделена на | если у песни присутствует разные категории. Это никак не подходит для графиков, поэтому, надо перебрать значения и 
    перейти к словарю
    '''
    genre_dictionary = defaultdict(int)
    for genre_id in genre_ids:
        if type(genre_id) == str:
            genre_list = genre_id.split('|')
            for genre in genre_list:
                genre_dictionary[genre] += 1
    return genre_dictionary
