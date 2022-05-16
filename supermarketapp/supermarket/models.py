from django.db import models
import uuid

class Loai(models.Model):
    id = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True)
    name = models.TextField(default="", max_length=255)
    def __str__(self) -> str:
        return f"{self.name}"

class MatHang(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.TextField(default="", max_length=255)
    gia = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    loai = models.ForeignKey(
        Loai,
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )
    
