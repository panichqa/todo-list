from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def __str__(self):
        return f"{self.content} - {'Done' if self.is_done else 'Not Done'} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
