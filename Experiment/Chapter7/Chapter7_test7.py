import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,20,1)
plt.xlim(0,10)
plt.ylim(0,100)
plt.xlabel('x轴',fontproperties='SimHei',fontsize=16)
plt.ylabel('y轴',fontproperties='SimHei',fontsize=16)
plt.plot(x,x ** 2 ,'red',lw=2)
plt.plot(x,x * 2 +1,'b',linestyle='dashed',lw=2)
plt.legend(['x ** 2','2 * x + 1'])     	              #设置图例.
plt.show()
