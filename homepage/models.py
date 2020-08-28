from django.db import models

# Create your models here.
class BoastsAndRoasts(models.Model):
    isroast = models.BooleanField()
    post_content = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    submissiondate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_content

    def total_votes(self):
        return self.upvotes - self.downvotes
