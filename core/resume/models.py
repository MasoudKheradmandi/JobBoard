from django.db import models
from account.models.company import Company
from job.models import Job
from account.models.user import User
from account.validator import validate_resume_size
# Create your models here.

class SendResume(models.Model):
    reciver = models.ForeignKey(Company, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Job, on_delete=models.CASCADE,null=True)
    cv_file = models.FileField(validators=[validate_resume_size],blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.reciver.name} for {self.post}"