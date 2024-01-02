from django.db import models

# from datetime import datetime
#
# # print(datetime.now().weekday())
# Create your models here.
streams = [('S', 'S'), ('H', 'H')]
class_names = [('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6')]
sex = [('M', 'M'), ('F', 'F')]


class Subjects(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Teachers(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, unique=True)
    subjects = models.ManyToManyField(Subjects, related_name='teacher_subjects')

    def __str__(self):
        teacher_subs = [str(sub) for sub in self.subjects.all()]
        return f"{self.f_name} {self.l_name} teaches {', '.join(teacher_subs)}"


class ClassRooms(models.Model):
    class_name = models.CharField(max_length=100, choices=class_names)
    stream = models.CharField(max_length=5, choices=streams)
    class_teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='class_teacher')
    class_monitor = models.CharField(max_length=50)
    teacher_in = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='current_teacher', blank=True,
                                   null=True)
    state = models.BooleanField(db_default=False)

    def __str__(self):
        return f"{self.class_name} {self.stream} {'Occupied' if self.state else 'Empty'}"


class Records(models.Model):
    date = models.DateField(auto_now_add=True)
    day = models.CharField(max_length=20)
    week = models.CharField(max_length=20)
    class_name = models.ForeignKey(ClassRooms, on_delete=models.CASCADE, related_name='class_taught')
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='Who_taught')
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_taught')
    entry_time = models.TimeField(auto_now_add=True)
    exit_time = models.TimeField(blank=True)
    duration = models.TimeField(blank=True)

    def __str__(self):
        return f"{self.date} {self.day}"
