from django.db import models

class Report(models.Model):
    COURSE_CATEGORY_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    ]

    course_category = models.CharField(max_length=2, choices=COURSE_CATEGORY_CHOICES)
    report_name = models.CharField(max_length=100)
    upload_files = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.report_name
