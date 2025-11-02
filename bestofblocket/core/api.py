from ninja import NinjaAPI
from ninja import Schema
from typing import List

from .models import Ad


api = NinjaAPI()


class AdSchema(Schema):
    title: str
    slug: str
    text: str | None


@api.get("/ads/", response=List[AdSchema])
def ad_list(request):
    return list(Ad.objects.all())


@api.get("/ads/{id}", response=AdSchema)
def ad_detail(request, id: int):
    return Ad.objects.get(id=id)
