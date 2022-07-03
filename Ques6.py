def student_data(student_id, **kwargs):
    print("\nStudent ID:", student_id)
    if "student_name" in kwargs:
        print("Student Name :", kwargs['student_name'])
    if "student_name" and "student_class" in kwargs:
        print("Student Name :", kwargs['student_name'])
        print("Student Class :", kwargs['student_class'])

student_data(student_id = '21102125', student_name = 'Himanshu Rathoria')

student_data(student_id='21102125', student_name='Himanshu Rathoria', student_class='XII')