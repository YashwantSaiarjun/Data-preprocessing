#----------------------------------------------------------------------------------
# Dummy varaibles creation
#----------------------------------------------------------------------------------

df=pd.get_dummies(df)
df.info()

# unwanted columns after creating dummies
del df['airport_NO']
del df['airport_6.0']
del df['airport_46.19856']
del df['waterbody_6.0']
del df['waterbody_46.19856']
del df['waterbody_None']

df.info()
