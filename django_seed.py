from django_seed import Seed

seeder = Seed.seeder()

from api1.models import Imovel
from api2.models import Anuncio
from api3.models import Reserva

seeder.add_entity(Imovel, 5)
seeder.add_entity(Anuncio, 3)
seeder.add_entity(Reserva, 8)

inserted_pks = seeder.execute()
