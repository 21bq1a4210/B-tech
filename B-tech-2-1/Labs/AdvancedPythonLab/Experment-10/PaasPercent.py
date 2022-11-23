import matplotlib.pyplot as plt
data=pd.read_excel("")
x = data.iloc [0:10,0]
y = data.iloc [0:10, 13]
plt.subplot (2,2,1)
plt.plot (x, y)
plt.subplot (2,2,2)
plt.bar (x,y, color = 'orange')
plt.Subplot (2,2, 3)
plt.scatter (x,y)
plt.subplot (2,2,4)
plt.pie (y, labels = x)
plt.show()
