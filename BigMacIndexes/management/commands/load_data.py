import csv
from django.core.management import BaseCommand
from BigMacIndexes.models import BigMacIndexes


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path) as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                _, created = BigMacIndexes.objects.get_or_create(
                    date=row[0],
                    iso_a3=row[1],
                    currency_code=row[2],
                    name=row[3],
                    local_price=row[4],
                    dollar_ex=row[5],
                    USD_raw=row[6],
                    EUR_raw=row[7],
                    GBP_raw=row[8],
                    JPY_raw=row[9],
                    CNY_raw=row[10],
                    GDP_dollar=row[11],
                )
