#class is the blueprint of object
#Object is the instance if class

class Pinfo:
    name=""
    occupation=""
    salary= 100000000
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a= Pinfo()
b= Pinfo()
a.name="Shubham"  #updating 
a.occupation="CEO"
b.name="Shubhangi"  #updating 
b.occupation="PA"
#print(a.name)
#print(a.occupation)
a.info()
b.info()

# #Here’s a set of **simple and practical exercises** you can try **after learning about classes and objects in Python**. These will help you understand how to define classes, create objects, use methods, and apply object-oriented principles.

# ---

# ### ✅ **Exercise 1: Student Information**

# **Task:**
# Create a class `Student` with the following attributes:

# * `name`
# * `roll_number`
# * `marks`

# Add a method `display_details()` that prints the student's information.

# **Bonus:** Add a method `is_passed()` that returns True if marks >= 40, else False.

# ---

# ### ✅ **Exercise 2: Bank Account**

# **Task:**
# Create a class `BankAccount` with:

# * `account_holder_name`
# * `balance`

# Methods:

# * `deposit(amount)`
# * `withdraw(amount)`
# * `display_balance()`

# **Bonus:** Prevent balance from going negative.

# ---

# ### ✅ **Exercise 3: Circle**

# **Task:**
# Create a class `Circle` with:

# * `radius` (default = 1.0)

# Methods:

# * `get_area()` → π \* r²
# * `get_circumference()` → 2 \* π \* r

# ---

# ### ✅ **Exercise 4: Book Management**

# **Task:**
# Create a class `Book` with:

# * `title`
# * `author`
# * `price`

# Add a method `get_discounted_price(discount_percent)`.

# ---

# ### ✅ **Exercise 5: Employee Salary Calculator**

# **Task:**
# Create a class `Employee` with:

# * `name`
# * `salary`
# * `designation`

# Add a method `give_raise(amount)` to increase the salary.

# ---

# ### ✅ **Exercise 6: Rectangle Class**

# **Task:**
# Create a class `Rectangle` with:

# * `length`
# * `width`

# Methods:

# * `get_area()`
# * `get_perimeter()`

# ---

# ### ✅ **Exercise 7: Inheritance Practice**

# **Task:**
# Create a base class `Vehicle` with `brand` and `speed`.
# Create a derived class `Car` that adds `fuel_type`.

# Add a method in `Car` to display all details.

# ---

# Would you like me to give a **code example for any one** of these exercises?





 