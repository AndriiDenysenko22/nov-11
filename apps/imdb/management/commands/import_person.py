import csv

from django.core.management import BaseCommand

from apps.imdb.models import Person


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str)
        parser.add_argument('--delimiter', type=str, default='\t')

    def handle(self, primary_key=None, **options):
        file_name = options.get('file')

        with open(file_name) as f:
            csv_data = csv.reader(f, delimiter=options.get('delimiter', '\t'))
            for row in csv_data:
                row_data = {
                    # 'id': primary_key,
                    'person_id': row[0],
                    'imdb_id': row[5],
                    'name': row[1],
                    'birth_year': f'{row[2]}-01-01' if row[2] != '\\N' else None,
                    'death_year': f'{row[3]}-01-01' if row[3] != '\\N' else None,
                }

                # models = Person(imdb_id=row[5], name=row[1], birth_year=row[2], death_year=row[3])
                # models.save

                person, created = Person.objects.get_or_create(person_id=row_data['person_id'], defaults=row_data)
                if not created:
                    Person.objects.filter(person_id=person.person_id).update(**row_data)
                print(person)
