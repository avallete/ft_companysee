import json
from datetime import date
from django.core.management.base import BaseCommand
from django.db import transaction
from company.models import Company, CompanyResult


class Command(BaseCommand):
    help = 'Populate database with mock_data.json'

    def handle(self, *args, **options):
        data = {}
        try:
            with open('mock_data.json', 'r') as fd:
                data = json.load(fd)
        except (IOError, ValueError) as e:
            print("Error with mock_data.json opening: %s" % e)
        # If file successfully loaded and parsed with json
        if data:
            with transaction.atomic():
                for element in data:
                    company = Company(name=element['name'],
                                      sector=element['sector'],
                                      siren=element['siren'])
                    company.save()
                    for result in element['results']:
                        CompanyResult(ca=result['ca'],
                                      margin=result['margin'],
                                      ebitda=result['ebitda'],
                                      loss=result['loss'],
                                      date=date(year=result['year'], month=01, day=01),
                                      company=company).save()
                    print('Company "%s" created.' % company.name)
