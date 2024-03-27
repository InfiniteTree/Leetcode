# 创建一个示例字典
student_grades = {"Alice": 95, "Bob": 88, "Charlie": 92, "David": 78}

# 创建字典的迭代器
iterator = iter(student_grades)

# 遍历字典并逐个获取键值对
while True:
    try:
        name = next(iterator)
        grade = student_grades[name]
        print(f"{name}: {grade}")
    except StopIteration:
        break