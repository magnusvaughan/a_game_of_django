import json
from pprint import pprint
from django.core.management.base import BaseCommand, CommandError
from characters.models import Character

class Command(BaseCommand):
    help = 'Populates the DB from a JSON file'

    def handle(self, *args, **options):
        data_string = open('/Users/magnusvaughan/side/a_game_of_django/characters/json/character.json').read()
        data = json.loads(data_string)

        for person in data:
    
            from characters.models import Character
            record = Character(id=person['Id'], name=person['Name'], is_female=person['IsFemale'], culture=person['Culture'], titles=person['Titles'], aliases=person['Aliases'], born=person['Born'], died=person['Died'], father=person['Father'], mother=person['Mother'], spouse=person['Spouse'], children=person['Children'], allegiances=person['Allegiances'], books=person['Books'], pov_books=person['PovBooks'], played_by=person['PlayedBy'], tv_series=person['TvSeries'])
            record.save()
