from django.db import models
class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=16, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Если торг уместен, то True(1), если нет - False(0)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id}, {self.title}, {self.price}" 
    class Meta():
        db_table =  "advertisement"
