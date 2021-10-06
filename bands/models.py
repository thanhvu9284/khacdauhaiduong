from django.db import models

# Create your models here.
class Band(models.Model):
    """A model of a rock band."""    
    name = models.CharField("Tên ban nhạc",max_length=200)
    can_rock = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Ban nhạc"

class Member(models.Model):
    """A model of a rock band member."""
    name = models.CharField("Tên thành viên", max_length=200)
    instrument = models.CharField("Công cụ",choices=(
            ('g', "Đàn Guitar"),
            ('b', "Bass"),
            ('d', "Trống"),
        ),
        max_length=1
    )
    band = models.ForeignKey(
        "Band",
        on_delete=models.CASCADE,
    )
    class Meta:
        verbose_name_plural = "Thành viên Ban nhạc"