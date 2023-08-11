#Create income calculator

#Create parent class employee_profile
class employee_profile:
#Initialize function for parent class employee_profile
    def __init__(self, fname, lname, job, code):
      self.fname = fname
      self.lname = lname
      self.job = job
      self.id = code
      print(f'First Name: ',  self.fname, 'Last Name: ', self.lname, 'Job role: ', self.job, 'ID: ', self.id)


fname = input('Enter first name:')
lname = input('Enter last name: ')
job = input('Enter job role:')
code = input('Enter job code:')

EP = employee_profile(fname, lname, job, code)
print(EP)
#Create child class income_profile of parent class
class income_profile:

  def __init__(self,hours, hourly_rate ):
    self.hours = hours
    self. hourly_rate = hourly_rate
    
  def total_income(self): 
    #Used If statements to calculate overtime and normal time payments 
    if int(self.hours) <= 40:
       print("Your payment this week is: ", float(self.hours) * float(self.hourly_rate))
    elif int(self.hours) > 40:
       print("Your over-time payment this week is: ", (float(self.hourly_rate) * 2.5) * float(self.hours))
    elif int(self.hours) == 0:
       print("NO PAYMENT THIS WEEK")
  
    
   
hours = input('Enter your weekly hours: ')
hourly_rate = input('Enter the hourly rate: ')




my_income = income_profile(hours, hourly_rate)
my_income.total_income()
