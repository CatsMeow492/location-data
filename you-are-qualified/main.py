skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

qualified = skills.intersection(job_skills)

print(qualified)

print(" ".join(skills & job_skills))