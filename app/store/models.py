from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

from app.core.models import BaseModel


class TrashStations(BaseModel):
    title = models.CharField(verbose_name="Nome da Estação", max_length=255)
    quantity_max = models.IntegerField(verbose_name="Quantidade Máxima", default=100)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-title"]
        verbose_name = "Estação de Lixo"
        verbose_name_plural = "Estações de Lixo"

    @property
    def volume_percent(self):
        return 0


class Discarts(BaseModel):
    station = models.ForeignKey(TrashStations, verbose_name="Estação de Lixo", on_delete=models.PROTECT, related_name="discarts")
    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.PROTECT, related_name="users")
    quantity = models.IntegerField(verbose_name="Quantidade Descartada")

    def __str__(self) -> str:
        return f"{self.station.title} - {self.quantity}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Descarte"
        verbose_name_plural = "Descartes"


class NotificationStatus(TextChoices):
    CREATED = "created", _("Criado")
    CLOSE = "closed", _("Fechado")


class Notifications(BaseModel):
    station = models.ForeignKey(TrashStations, verbose_name="Estação de Lixo", on_delete=models.PROTECT, related_name="stations")
    checker = models.ForeignKey(User, verbose_name="Conferente", on_delete=models.PROTECT, related_name="checkers")
    status = models.IntegerField(verbose_name="Situação", choices=NotificationStatus.choices, default=NotificationStatus.CREATED)

    def __str__(self) -> str:
        return f"{self.station.title} - {self.status}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"
