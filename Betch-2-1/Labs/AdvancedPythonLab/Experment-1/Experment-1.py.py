class Check: 

    def __init__(self,s): 

        self.sen=s; 

        self.vowels={'a','e','i','o','u'}; 

        self.ch=[]; 

    def check(self): 

        self.sen=self.sen.lower() 

        for ch in self.sen: 

            self.ch.append(ch) 

        self.ch=set(self.ch) 

        if len(self.ch & self.vowels)==len(self.vowels): 

            print("sentence contain all the vowels") 

        else: 

            print(" sentence don’t contain all the vowels ") 

obj=Check(input("enter a sentence:")) 

obj.check() 
