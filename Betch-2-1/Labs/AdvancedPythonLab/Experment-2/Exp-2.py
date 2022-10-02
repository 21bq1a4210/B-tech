class Check: 

    def __init__(self,let,li): 

        self.let=let 

        self.li=li 

    def check(self): 

        for i in self.li: 

            i=i.lower() 

            li_set=set(i) 

            if li_set.issubset(self.let): 

                print(i.capitalize()) 

let={'a','k','e','o','t','p','n'} 

li=["Arun","Varun","Zebra","Kent","Eat","Pot","Net","Peak","Peacok","Nato","Toe","Poke","Knife","Peot","Venus","Ant"] 

obj=Check(let,li) 

obj.check() 
