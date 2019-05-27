#DEFINING EXAMS
print("Please enter the marks obtained in following examinations:")
print("Marks obtained in each subject cannot exceed 100")

#INPUT THE MARKS OBTAINED
#PAPER1
Paper1 = int(input("English: "))
if Paper1 > 100:
    print("Invalid input of marks obtained")
    exit()
elif Paper1 < 40:
    result = "FAIL"
else:
    pass

#PAPER2
Paper2 = int(input("Urdu: "))
if Paper2 > 100:
    print("Invalid input of marks obtained")
    exit()
elif Paper2 < 40:
    result = "FAIL"
else:
    result = "PASS"

#PAPER3
Paper3 = int(input("Maths: "))
if Paper3 > 100:
    print("Invalid input of marks obtained")
    exit()
elif Paper3 < 40:
    result = "FAIL"
else:
    result = "PASS"

#PAPER4
Paper4 = int(input("Science: "))
if Paper4 > 100:
    print("Invalid input of marks obtained")
    exit()
elif Paper4 < 40:
    result = "FAIL"
else:
    result = "PASS"

#PAPER5
Paper5 = int(input("Islamiat: "))
if Paper5 > 100:
    print("Invalid input of marks obtained")
    exit()
elif Paper5 < 40:
    result = "FAIL"
else:
    result = "PASS"

#SUM UP THE MARKS
TotalMarks = Paper1 + Paper2 + Paper3 + Paper4 + Paper5
print("Total Marks obtained: " + str(TotalMarks) + " Out of 500")

#PECENTAGE OBTAINED
PercentageObtained = int(TotalMarks) / 500
print("Percentage obtained: " + str (PercentageObtained*100) + " %")

#GRADE
if float(PercentageObtained) >= .8 :
    GradeObtained = "A+"
    result = "PASS"
elif .8 > float(PercentageObtained) >= .7:
    GradeObtained = "A"
    result = "PASS"
elif .7 > float(PercentageObtained) >= .6:
    GradeObtained = "B"
    result = "PASS"
elif .6 > float(PercentageObtained) >= .5:
    GradeObtained = "C"
    result = "PASS"
elif .5 > float(PercentageObtained) >= .4:
    GradeObtained = "D"
    result = "PASS"
else:
    GradeObtained = "N/A"
    result = "FAIL"

#RESULT
if str(result) == "FAIL":
    print("Result = FAIL")
else:
    print("Grade Obtained: " + GradeObtained)
    print("Result = PASS")

#PRINT REPORT CARD
print(
    '''
       ================================MARKSHEET=================================
       |                                                                        |
       |                                                                        |
       |                                                                        |
       |   MARKS OBTAINED:                                                      |
       |                                                                        |
       |   SUBJECTS:                                                            |
       |                                                                        |
       |   ENGLISH: ''' + str(Paper1) + ''' /100                                                     |
       |   URDU: ''' + str(Paper2) + ''' /100                                                        |
       |   MATHS: ''' + str(Paper3) + ''' /100                                                       |
       |   SCIENCE: ''' + str(Paper4) + ''' /100                                                     |
       |   ISLAMIAT: ''' + str(Paper5) + ''' /100                                                    |
       |                                                                        |
       |   TOTAL MARKS OBTAINED: ''' + str(TotalMarks) + ''' Out of 500                                 |
       |                                                                        |
       |   PERCENTAGE: ''' + str(int(PercentageObtained*100)) + ''' %                                                   |
       |                                                                        |
       |   GRADE: ''' + str(GradeObtained) + '''                                                            |
       |                                                                        |
       |   RESULT: ''' + str(result) + '''                                                         |
       |                                                                        |
       |                                                                        |
       |                                                                        |
       |                                                                        |
       |                                                                        |
       |                                                                        |
       """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
''')
