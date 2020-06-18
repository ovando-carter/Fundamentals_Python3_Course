#
#relational operators
def greater_than(x,y):
  if x > y:
    return x
  if y > x:
    return y
  if x == y: 
    return "These numbers are the same"


##
def graduation_reqs(credits, gpa):
 if (credits >= 120) and (gpa >= 2.0): # you can make this a one variable check if you remove the and and the second condition
    return "You have enough credits to graduate!"
  else: 
    return "You did not graduate" 

print(graduation_reqs(120,2.0))
print(greater_than(3,4))


## 
def graduation_mailer(gpa, credits): #a conditional statement that checks if the student has either a gpa over 2, or credits over 120/ 
  if (gpa >= 2.0) or (credits >= 120):
    return True
  
## use of not
def graduation_reqs2(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if not (gpa >= 2.0) and not (credits >= 120): # you can also just use else: here to save a lot of typing. 
    return "You do not meet either requirement to graduate!"

print(graduation_reqs2(2,120))

## grade converter
def grade_converter(gpa):
  if gpa >= 4.0:
    return "A"
  elif gpa >= 3.0:
    return "B"
  elif gpa >= 2.0:
    return "C"
  elif gpa >= 1.0:
    return "D"
  elif gpa >= 0.0:
    return "F"

print(grade_converter(0.0))


## selects applicants who meet certain requirements. 
def applicant_selector(gpa,ps_score,ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    return "This applicant should be accepted."
  elif (gpa >= 3.0) and (ps_score >= 90) and not (ec_count >= 3):
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."