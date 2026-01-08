residuals = [-0.4 ,0.8 , -1 , 1.2 , -0.6]
SSR = 0
for i in residuals:
    SSR += i*i
SST = 0
y = [3, 5, 4, 7, 6]
ybar = 5
for i in y:
    SST+=(i-ybar)**2
print("SST equals to:",SST)
print("R^2:",1 - SSR/SST)