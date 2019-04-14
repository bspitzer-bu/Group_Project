from import_export import resources
from .models import Gpcr

class GpcrResource(resources.ModelResource):
    class Meta:
        model = Gpcr