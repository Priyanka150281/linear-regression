
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading data
data = pd.read_csv("weight-height.csv")
print(data.shape)
data.head()


#Collecting X and Y
X = data['Height'].values
Y = data['Weight'].values


#Mean of X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

#Total Number of Values
m=len(X)

#Using the formula to calculate b1 and b0
numer=0
denom=0
for i in range(m):
    numer=numer+(X[i]-mean_x)*(Y[i]-mean_y)
    denom=denom+(X[i]-mean_x)**2
b1=numer/denom
b0=mean_y-(b1*mean_x)

#print coefficients
print(b1,b0)
    
#plotting values and Regression line
max_x = np.max(X)+100
min_x = np.min(X)-100

#Calculating line values x and y
x = np.linspace(min_x,max_x,1000)
y=b0+b1*x

#plotting line
plt.plot(x,y,color='#58b970' , label='Rgression Line')

#plotting scatter points
plt.scatter(X,Y, c='#ef5423' , label='Scatter plot')

plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()
plt.show()

#Calculating R-squared

ss_t=0
ss_r=0
for i in range(m):
    y_pred = b0+b1*X[i]
    ss_t = ss_t+(Y[i]-mean_y)**2
    ss_r = ss_r+(Y[i]-y_pred)**2
r2=1-(ss_r/ss_t)
print(r2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    
    