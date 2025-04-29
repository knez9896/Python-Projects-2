from django.db import models

class UniversityClasses(models.Model):
    Title = models.CharField(max_length=200)
    CourseNumber = models.IntegerField()
    InstructorName = models.CharField(max_length=200)
    Duration = models.FloatField()

    class Meta:
        verbose_name_plural = "UniversityClasses"

    def __str__(self):
        return self.Title
