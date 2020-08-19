from django.db import models
from users.models import CustomUser
from django.utils import timezone
User =  CustomUser



class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='categories')
    text = models.TextField(max_length=60, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='notes')
    note = models.TextField(max_length=1000,blank=False,null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')
    created_on = models.DateTimeField(auto_now_add=True)
    reminder = models.DateTimeField()

    def __str__(self):
        return f"{self.user.get_full_name()} : {self.note}"

    @property
    def passed(self):
        re = self.reminder
        today = timezone.now()
        if re<today:
            return 'Passed!'
        return ''
