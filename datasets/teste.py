import pandas as pd
from pandas import Series, DataFrame
import folium
from folium import plugins

excel_file = 'DadosBO_2019_2(ROUBO DE CELULAR).xls'
dfList = list()
df = pd.read_csv(excel_file, sep='\t', lineterminator='\n')
dfList.append(df)
dfList.reset_index()
