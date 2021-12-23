#----------------------------------------------------------------------------------
# Varaible Transformation
#----------------------------------------------------------------------------------

# crime rate
sns.jointplot(x='crime_rate',y='price',data=df) #before follows log graph concept
df.crime_rate=np.log(1+df.crime_rate)
sns.jointplot(x='crime_rate',y='price',data=df) #after follows log graph concept

# dist 1,2,3,4 collab as avg
df['avg_dist']=(df.dist1+df.dist2+df.dist3+df.dist4)/4
del df['dist1']
del df['dist2']
del df['dist3']
del df['dist4']

new_describe_table=df.describe()
