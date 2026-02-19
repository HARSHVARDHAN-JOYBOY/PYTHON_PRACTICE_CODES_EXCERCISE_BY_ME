class Employee:
    def __init__(self,emp_id,name,basic_salary):
        self.__emp_id=emp_id
        self.__name=name
        self.__basic_salary=basic_salary

    def calculate_salary(self):

        # HRA=(20/100)*self.__basic_salary
        # DA=(10/100)*self.__basic_salary
        # PF=(12/100)*self.__basic_salary



        HRA=(20/100)*self.__basic_salary
        DA=(10/100)*self.__basic_salary
        PF=(12/100)*self.__basic_salary


        sal=self.__basic_salary+HRA+DA
        sal=sal-(PF)
        print(f"Salary in account :{sal}")
s1=Employee(101,"anishsurve",1000000)
s1.calculate_salary()