#missing values implementation
mean(df$n_hos_beds,na.rm=TRUE)
df$n_hos_beds[is.na(df$n_hos_beds)]<-mean(df$n_hos_beds,na.rm=TRUE)

summary(df$n_hos_beds)
