from django.db import models







class New(models.Model):
    img = models.ImageField(upload_to="img", blank=True, null=True)
    video = models.FileField(upload_to="video", blank=True, null=True)
    title = models.TextField()
    text = models.TextField()
    data = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    
