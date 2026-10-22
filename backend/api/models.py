from django.db import models

# Create your models here.

class Product(models.Model):
    nom = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auteur_du_produit = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def get_prix_in_dollars(self):
        return f"{self.prix} $"
    
    def get_description_normal(self):
        return f"Nom : {self.nom} - Prix : {self.prix} $"

    def __str__(self) -> str:
        return self.nom 