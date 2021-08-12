import factory
from flowertypes.models import RosesBouquets

class RosesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RosesBouquets 

    name = factory.Sequence(lambda n:f'Bouquet number {n}')
    description = factory.Sequence(lambda n:f'Description {n}')
    price = factory.Sequence(lambda n:f'Price {n}')