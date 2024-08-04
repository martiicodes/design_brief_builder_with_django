from django.db import models

class DesignBrief(models.Model):
    client_name = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    email = models.EmailField()
    project_description = models.TextField()
    objectives = models.TextField()
    target_audience = models.TextField()
    competitors = models.TextField()
    deliverables = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()

    def __str__(self):
        return self.project_name
