employee_list = ['Chris','Mary','Sawyer','Anita','Peyton','Catherine','Bobby',
                 'Johnathan','Issaac','Jamie']
subList1= employee_list[0:5]
subList2= employee_list[5:10]#splitting the list into two sublists
print(subList1, subList2)
del subList1[1]#deleting the second element in the first sublist
print(subList1)
subList2.append('Kriti Brown')#adding the element Jack to the second sublist
print(subList2)
mergedList= subList1+subList2#merging the two sublists
print(mergedList)
salaryList= [30000,40000,20000,50000,80000,100000,90000,70000,60000,80000]
salaryRaise = salaries_with_raise = [salary * 1.04 for salary in salaryList]
print(salaryList, salaryRaise)
salary_2 = salaryRaise[::-1]
print('Salary_2', salary_2)
top_3 = salary_2[0:3]#slicing the list to get the top 3 salaries
print('Top 3 salaries', top_3)
