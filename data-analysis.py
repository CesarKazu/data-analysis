import pandas as pd
from pandas import Series, DataFrame
import folium
from folium import plugins

path = 'datasets/'
filenames = {'2018_1', '2018_2', '2018_3', '2018_4', '2018_5', '2018_6', '2018_7', '2018_8', '2018_9', '2018_10', '2018_11', '2018_12', '2019_1', '2019_2', '2019_3', '2019_4'}
extension = '.xls'

def populaDataFrame():
    dfList = list()

    for file in filenames:
        df= pd.DataFrame(pd.read_csv((path+file+extension), sep='\t', encoding='UTF-16 LE'))
        dfList.append(df)

    df = pd.concat(dfList)
    return df

df = populaDataFrame()
df.reset_index()

geolocalizacoes = df[['LATITUDE', 'LONGITUDE']].copy()
geolocalizacoes.isnull().sum()

geolocalizacoes.dropna(inplace=True)
geolocalizacoes.isnull().sum()

coordenadas = []
lat = geolocalizacoes['LATITUDE'].values

long = geolocalizacoes['LONGITUDE'].values

mapa = folium.Map(location=[-23.1791, -45.8872],tiles='OpenStreetMap',zoom_start=12)
 
for la,lo in zip(lat,long):
    folium.Marker(
        location=[la, lo],
    ).add_to(mapa)
    coordenadas.append([float(la.replace(",", ".")),float(lo.replace(",", "."))])
    
mapa.add_child(plugins.HeatMap(coordenadas))
mapa.add_child(coordenadas)
