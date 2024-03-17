
# making lists for users' data
names = []
ages = []
sums = []
incomes = []
incomes_sums = []

# setup of incomes 
min_salary = 19242
tax = 0.13
job_teacher = ["Teacher", min_salary + 16632]
pension = ["Pension", min_salary]
scholarship = ["Scholarship", ]

#setup of payments and expense
card_maintenance = 50
flat_payment = 2000
groceries = 1500
bills = 1700

worker_payment = None
student_payment = flat_payment + groceries + bills
teen_payment = card_maintenance + groceries
elder_payment = None

#adding up users' data
names.extend(["John Smith", "Helen Parker", "Riley Evans"])
ages.extend([67, 39, 16])
sums.extend([5954.02, 16873.17, 9366.50])
incomes.extend([pension[0], job_teacher[0], None])

#making a dictionary list for users
users = {
    1: [names[0], sums[0], ages[0]],
    2: [names[1], sums[1], ages[1]],
    3: [names[2], sums[2], ages[2]]
}


