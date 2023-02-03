from django.db import models

# Create your models here.
class Appareil(models.Model):
    client              = models.CharField(max_length=30)
    immatriculation     = models.CharField(max_length=30)
    mise_en_circulation = models.CharField(max_length=30)
    dernier_passage     = models.CharField(max_length=30)
    immatriculation     = models.CharField(max_length=30)
    status              = models.CharField(max_length=30)

    # Change status to "En Mission"
    def in_duty(self):
        self.status = "En Mission"
        self.save()

    # Change status to "Hors Ligne"
    def out_of_duty(self):
        self.status = "Hors Ligne"
        self.save()

    # Change status to "En Maintenance"
    def in_maintenance(self):
        self.status = "En Maintenance"
        self.save()