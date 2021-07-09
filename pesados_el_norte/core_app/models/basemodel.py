from django.db.models import Model, BooleanField, DateTimeField


class BaseModel(Model):
    is_active = BooleanField("is active?", default=True)
    created_at = DateTimeField("created on", auto_now_add=True)
    updated_at = DateTimeField("last modified on", auto_now=True)

    def delete(self, using=None, keep_parents=False):
        self.is_active = False

    delete.alters_data = True

    class Meta:
        abstract = True
