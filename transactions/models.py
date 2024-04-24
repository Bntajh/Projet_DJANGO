from django.db import models
from django.core.exceptions import ValidationError

CATEGORY_CHOICES = [
    (0, "Non catégorisé"),
    (1, "Revenus"),
    (2, "Dépenses fixes"),
    (3, "Salaire"),
    (4, "Dividendes"),
    (5, "Cotisations"),
    (6, "Taxes et impôts"),
    (7, "Autres"),
]

class SubCategory(models.Model):
    name = models.CharField(max_length=1000)
    category = models.IntegerField(choices= CATEGORY_CHOICES )

    def __str__(self) -> str:
        return self.name

class Transaction(models.Model):
    #definir les champs des models
    label = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)  #date de la transaction
    amount = models.DecimalField(max_digits= 10, decimal_places=2) #montant de la transaction
    vat_percentage = models.IntegerField(default=0)    #taux d'imposition en pourcentage (par défaut 0 si pas de TVA)
    vat_amount = models.DecimalField(max_digits= 10, decimal_places=2, default=0)  #montant du VAT (TVA ou TAUX DE TVA)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total montant de toutes les transactions
    category = models.IntegerField(choices = CATEGORY_CHOICES)
    sub_
    category = models.ForeignKey(
        SubCategory,
        null=True, 
        blank= True, 
        on_delete=models.SET_NULL, #
        related_name="transactions")
    
    def __str__(self) -> str: #
        return self.label
    
    def save(self, *args, **kwargs):
        if self.sub_category and self.sub_category.category != self.category:
            raise ValidationError(
                " Sub category must have same category than transaction"
            )
        return super().save(*args, **kwargs)
