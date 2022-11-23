from numpy import  *
a0=array(10)                         # 0D or sclar array 
a1=array([1,2,3])                    # 1D array (collection of 0D)
a2=array([[1,2,3],[4,5,6]])          # 2D array (collection of 1D)
a3=array([[[1,2,3],[4,5,6],[7,8,9]]])# 3D array (collection of 2D)

print(f"a0 dim={a0.ndim}, a0 shape={a0.shape}, a0 size={a0.size}")
print(f"a1 dim={a1.ndim}, a1 shape={a1.shape}, a1 size={a1.size}")
print(f"a2 dim={a2.ndim}, a2 shape={a2.shape}, a2 size={a2.size}")
print(f"a3 dim={a3.ndim}, a3 shape={a3.shape}, a3 size={a3.size}")
