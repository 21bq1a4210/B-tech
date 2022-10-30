from matplotlib import pyplot as plt
import numpy as np
x1=['audi','benz','bmw','jaguar','Landrover']
y1=[200,250,280,265,285]

x2=['ikon','figo','figo aspire','eco sport','endeavor']
y2=[190,160,175,165,185]

x3=['Suzuki','Brezza','XL6','Baleno','Scross']
y3=[110,120,135,145,155]

plt.figure(figsize=(15,5S))
plt.title('Cars Sales Information')
plt.bar(x1,y1,color='r',label='2019',align='center')
plt.bar(x2,y2,color='m',label='2020',align='center')
plt.bar(x3,y3,color='g',label='2021',align='center')
plt.xlabel('Car Models')
plt.ylabel('Sales in Crores')
plt.legend(loc='upper right')
plt.xticks(rotation=90)

plt.yticks(rotation=90)
plt.show()
