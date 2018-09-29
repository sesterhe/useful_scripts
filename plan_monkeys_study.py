import pandas as pd
import sys
day0= sys.argv[1]
day14= pd.to_datetime(day0) + pd.DateOffset(days=14)
day28=pd.to_datetime(day0) + pd.DateOffset(days=28)
day35=pd.to_datetime(day0) + pd.DateOffset(days=35)
day56=pd.to_datetime(day0) + pd.DateOffset(days=56)
day63=pd.to_datetime(day0) + pd.DateOffset(days=63)
day84=pd.to_datetime(day0) + pd.DateOffset(days=84)
day91=pd.to_datetime(day0) + pd.DateOffset(days=91)
day98=pd.to_datetime(day0) + pd.DateOffset(days=98)
day105=pd.to_datetime(day0) + pd.DateOffset(days=105)

dates=[0,14,28,35,56,63,84,91,98,105]
manipulation=['Bleed+Inject', 'Bleed', 'Bleed+Inject','Bleed','Bleed+Inject','Bleed','Bleed+Inject','Bleed','Bleed','Bleed']

for i,dat in enumerate(dates):
	t=pd.to_datetime(day0) + pd.DateOffset(days=int(dat))
	print "day" + str(dat) + " " + str(t.date()) + " " + manipulation[i]
