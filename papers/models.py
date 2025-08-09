from django.db import models

class Paper(models.Model):
    PAPER_CHOICES = [
        ('1st year', 'First Year'),
        ('2nd year', 'Second Year'),
        ('3rd year', 'Third Year'),
        ('4th year', 'Fourth Year'),
    ]

    subject_name = models.CharField(max_length=100)
    paper_type = models.CharField(max_length=10, choices=PAPER_CHOICES)
    uploaded_file = models.FileField(upload_to='papers/')
    year = models.IntegerField()

    def __str__(self):
        return f"{self.subject_name} ({self.paper_type} - {self.year})"
