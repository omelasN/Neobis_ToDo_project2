from django.db import models

# Create your models here.
class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


    def __str__(self):
        return self.text


