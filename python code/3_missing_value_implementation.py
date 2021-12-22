df.info()

df.n_hos_beds=df.n_hos_beds.fillna(df.n_hos_beds.mean())
df.info()
