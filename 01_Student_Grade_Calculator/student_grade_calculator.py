def calculate_grade(average):
  if average>=90:
    return "A+"
  elif average>=80:
    return "A"
  elif average>=70:
    return "B"
  elif average>=60:
    return "C"
  elif averge>=50:
    return "D"
  else:
    return "F"
name=input("Enter the Student Name : ")
maths=float(input("Enter Maths Marks : "))
english=float(input("Enter English Marks :"))
social=float(input("Enter Social MArks :"))
total=maths+english+social
average=total//3
grade=calculate_grade(average)
print("Name:",name)
print("Total Marks:",total)
print("Average:", round(average,2))
print("Grade:",grade)
