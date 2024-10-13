import uuid
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4(),editable=False,unique=True,primary_key=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Todo(BaseModel):
    todo_title = models.CharField(max_length=100)
    todo_desc = models.CharField(max_length=500)
    is_done = models.BooleanField(default=False)