# Variable transformation

#crime rate
plot(df$price,df$crime_rate)#before VT
df$crime_rate=log(1+df$crime_rate)
plot(df$price,df$crime_rate)#after VT

# avg distance
df$avg_dist=(df$dist1+df$dist2+df$dist3+df$dist4)/4

df2=df[,-7:-10]

df<-df2
rm(df2)
