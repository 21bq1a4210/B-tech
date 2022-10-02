class BubbleSort:
    def __init__(self,a):
        self.a=a
        BubbleSort._Sort(self)
    @staticmethod  
    def _Sort(self):
        for i in range(len(a)):
            for j in range(len(a)-i-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
                    print(f"iteration:{i+1} res:{a}")
        print()
        print(f"final sorted result:{a}")
a=[20,3,17,19,25,35,9,42,16,27]
obj=BubbleSort(a)

