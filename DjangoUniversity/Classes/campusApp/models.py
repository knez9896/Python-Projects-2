from django.db import models

# UniversityCampus model stores campus information including name, state, and unique ID
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    campus_id = models.IntegerField()

    class Meta:
        verbose_name_plural = "University Campus"

    def __str__(self):
        return self.campus_name