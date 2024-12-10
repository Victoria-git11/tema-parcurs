#X la mine este 8(DELIMART)
#Y=8 (Alexiana Cristina Victoria 8*3/3=8)
class Employee:
    everyone = []
    emp_count = 0
    def __init__(self,name,salary,department):
        self.name= name
        self.salary=salary
        self.department=department
        self.everyone.append(self) #append imi adauga la finalul listei un nou obiect self(mgr/em)
        Employee.emp_count+=1
    def display_employee(self):
        print(self.department)
 
class Manager(Employee):
    all_Managers=[]
    mgr_count=0
    def __init__(self,name,salary,department):
        super().__init__(name,salary,department)
        Manager.mgr_count+=1

mgr1=Manager("Ionescu", 40000, "Human Resources")
mgr2=Manager("Marian",35000, "IT")
mgr3=Manager("Ioana",50000, "Design")
mgr4=Manager("Floricica",28000, "Contabilitate")
mgr5=Manager("Vasilescu",20000,"Publicitate")
mgr6=Manager("Savu",50000,"Fizica Cuantica")
mgr7=Manager("Angelica",70000,"Relatii clienti")
mgr8=Manager("Ciolacu",20000, "Contabilitate")

em1=Employee("Bibi",5000,"Human Resources")
em2=Employee("Gigi",12000,"IT")

count = 0
print("   Managers:")
for all in Employee.everyone:
    Employee.display_employee(all)
    count+=1
    if count == Manager.mgr_count :
        print("\n   Employees:")

print(f"\nNumarul de manageri este: {mgr1.mgr_count}")
print(f"Numarul total de angajati este: {em1.emp_count}")
