from uuid import uuid4

from django.db import models
from django.utils import timezone


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class BaseModel(models.Model):
    id = models.UUIDField(
        verbose_name="Indentificador",
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    created_at = models.DateTimeField(
        verbose_name="Criado às", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="Atualizado às", auto_now=True)
    deleted_at = models.DateTimeField(
        verbose_name="Deletado às", blank=True, null=True, default=None
    )
    # for logical delete
    deleted = models.BooleanField(
        verbose_name="Deletado", default=False, db_index=True)
    # managers
    objects = BaseManager()
    objects_all = models.Manager()

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(BaseManager, self).delete()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()
