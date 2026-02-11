class Python_Adv_Da:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def display(self):
    print("Name : ",self.name)
    print("Age : ",self.age)


class Department(Python_Adv_Da):
  def __init__(self,name,age,dept):
    super().__init__(name,age)
    self.dept=dept
  def display(self):
    super().display()
    print("Department : ",self.dept)


res1=Department("Manu",21,"AI&DS")
res1.display()