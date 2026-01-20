# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import geopy.distance as geo
import os

os.chdir('/home/draner/Documents/datasci')

cr=pd.read_csv("/chic_res.csv")
da=pd.read_csv("/detr_amen.csv")
dr=pd.read_csv("/detr_res.csv")
na=pd.read_csv("/nyc_amen.csv")
nr=pd.read_csv("/nyc_res.csv")
pa=pd.read_csv("/pitt_amen.csv")
pr=pd.read_csv("/pitt_res.csv")

def dfOfNearest(d1,d2):
  df=pd.DataFrame(columns=('id_res','lon1','lat1','amenity','id_amen','lon2','lat2','dist'))
  ind=0
  for i in d1.index:
    if i%10==0:
      print(i)
    for k in d2.index:
      d=geo.geodesic((d1.iloc[i]['@lon'],d1.iloc[i]['@lat']), (d2.iloc[k]['@lon'],d2.iloc[k]['@lat'])).km
      currentVal=df.loc[df['id_res']==d1.iloc[i]['@id']]
      currentVal=currentVal.loc[df['amenity']==d2.iloc[k]['amenity']]
      if currentVal['id_res'].sum()<1:
        ind+=1
        cIndex=ind
      elif d<currentVal['dist'].iloc[0]:
        cIndex=currentVal.index
      else:
        continue
      df.loc[cIndex]=[d1.iloc[i]['@id'],
                      d1.iloc[i]['@lon'],
                      d1.iloc[i]['@lat'],
                      d2.iloc[k]['amenity'],
                      d2.iloc[k]['@id'],
                      d2.iloc[k]['@lon'],
                      d2.iloc[k]['@lat'],
                        d]
dfOfNearest(pr, pa)