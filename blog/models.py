from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(BaseModel):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    likes = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.title
