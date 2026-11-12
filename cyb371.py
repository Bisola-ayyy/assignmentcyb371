import pandas as pd

ds = {
    "student_id": ["CUL001", "CUL002", "CUL003", "CUL004",],
    "student_department": ["Mathematics", "English", "Religious Studies", "Agriculture"],
    "student_level": [100, 500, 400, 300],
    "attendance(%)": [85, 92, 78, 88],
    "average_score": [50, 72, 95, 81]
}

df = pd.DataFrame(ds)
print(df)
