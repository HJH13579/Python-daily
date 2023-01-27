todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]

todo_work = input()
todo_day_left = int(input())

todo_tuple = (todo_work, todo_day_left)

todo.append(todo_tuple)

print(todo)