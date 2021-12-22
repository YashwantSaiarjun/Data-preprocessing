#Outliers

# n_hot_rooms
uv=quantile(df$n_hot_rooms,0.99)
df$n_hot_rooms[df$n_hot_rooms>3*uv]<-3*uv

# rainfall
lv=quantile(df$n_hot_rooms,0.01)
df$n_hot_rooms[df$n_hot_rooms<0.3*lv]<-0.3*lv

summary(df$n_hot_rooms)
summary(df$rainfall)
