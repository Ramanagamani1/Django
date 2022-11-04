from django.db import models


from django.utils import timezone

# Create your models here.

class TaskList(models.Model):
    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
     name=models.CharField(max_length=50)
     desc=models.TextField()
     created_at=models.DateTimeField(default=timezone.now)
     due_date=models.DateTimeField(blank=False,default=timezone.now)
     list=models.ForeignKey(TaskList,on_delete=models.CASCADE)

     def __str__(self) -> str:
         return self.name