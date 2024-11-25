from django.db import models

class APILog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  
    user = models.CharField(max_length=255)  
    request_data = models.TextField()  
    response_data = models.TextField() 

    def __str__(self):
        return f"Log {self.id} - {self.user} - {self.timestamp} - {self.request_data} - {self.response_data}"