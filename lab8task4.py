def employee_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


employee_info(name="Aimal", age=18, salary=50000, designation="AI ENGINEER")