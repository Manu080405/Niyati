from Class1 import Python_Adv_Da

class Department(Python_Adv_Da):
  def __init__(self,name,age,dept):
    super().__init__(name,age)
    self.dept=dept
  def display(self):
    super().display()
    print("Department : ",self.dept)


res1=Department("Manu",21,"AI&DS")
res2=Department("Anu",20,"AI&DS")
res3=Department("Ranu",20,"AI&DS")
res4=Department("Reenu",21,"AI&DS")
res5=Department("Meenu",21,"AI&DS")
res1.display()
res2.display()
res3.display()
res4.display()
res5.display()