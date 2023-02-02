import csv

from django.core.management import BaseCommand

from apps.imdb.models import PersonMovie, Person, Movie


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str)
        parser.add_argument('--delimiter', type=str, default='\t')

    def handle(self, primary_key=None, **options):
        file_name = options.get('file')

        with open(file_name) as f:
            csv_data = csv.reader(f, delimiter=options.get('delimiter', '\t'))
            for row in csv_data:
                try:
                    a = Person.objects.get(person_id=row[2])

                    row_data = {
                        'imdb': Movie.objects.get(imdb_id=row[0]),
                        'person': a,
                        'order': row[1],
                        'category': row[3] if row[3] != '\\N' else None,
                        'job': row[4] if row[4] != '\\N' else None,
                        'characters': row[5].split(',') if row[5] != '\\N' else [],
                    }

                except Person.DoesNotExist:
                    continue
                personmovie, created = PersonMovie.objects.get_or_create(person__person_id=row[2],
                                                                         # movie__imdb=row[0],
                                                                         defaults=row_data)
                if not created:
                    PersonMovie.objects.filter(id=personmovie.id).update(**row_data)

                print(row_data)
                # print(type(Movie))
