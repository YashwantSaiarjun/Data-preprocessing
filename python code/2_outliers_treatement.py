df.info()

## n_hot_rooms
uv=np.percentile(df.n_hot_rooms,[99])[0]
uv
df[(df.n_hot_rooms>uv)]
df[(df.n_hot_rooms>3*uv)]=3*uv

## rainfall
lv=np.percentile(df.rainfall,[1])[0]
lv
df[(df.rainfall<0.3*lv)]=0.3*lv


sns.jointplot(x='crime_rate',y='price',data=df)
sns.jointplot(x='n_hot_rooms',y='price',data=df)
sns.jointplot(x='rainfall',y='price',data=df)
