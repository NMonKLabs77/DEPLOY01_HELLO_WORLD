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

EP1 = employee_profile("Nehemiah", "Monrose", "Junior Developer", "123456")
print(EP1)

subjects = ["Mathematics",  "English"]
for x in subjects:
    print(x.upper())
    if "English" in x:
        print("There are a million words I can think of that stats with the letter A")
    elif "Geography" in x:
        print("Tectonic plates ")
    if "Mathematics" in x:
        print(28890 * 6789 / (145 * 23))
