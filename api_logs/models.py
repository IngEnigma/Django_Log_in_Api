from django.db import models

class APILog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  
    username = models.CharField(max_length=255)  
    model = models.CharField(max_length=50)
    request_data = models.TextField()  
    response_data = models.TextField() 

    def __str__(self):
        return f"Log {self.id} - {self.username} - {self.model} - {self.timestamp} - {self.request_data} - {self.response_data}"