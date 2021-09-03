# Given a list of salaries you eed to take the bbonus everbody is getting as input and 
# increase all the salaries by that amount, output the resulting list

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())

final_salaries = map(lambda x: x + bonus, salaries)

final_salaries = list(final_salaries)

print(final_salaries)

