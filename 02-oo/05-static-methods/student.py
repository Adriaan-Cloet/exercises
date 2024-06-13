# functie op class niveau
# waarom -> je moet geen object maken van de class om de methode te gebruiken
# in de class zetten omdat die iets met de class te maken heeft
# we zetten dit in de class voor het structureren van het programma
# is dus om alles dat met elkaar te maken heeft bij elkaar te zetten


class Duration:
    def __init__(self, *, duration_in_seconds):
        self.__duration_in_seconds = duration_in_seconds

    @staticmethod
    def from_seconds(amount):
        return Duration(duration_in_seconds=amount)

    @staticmethod
    def from_minutes(amount):
        return Duration(duration_in_seconds=amount * 60)

    @staticmethod
    def from_hours(amount):
        return Duration(duration_in_seconds=amount * 3600)

    @property
    def seconds(self):
        return self.__duration_in_seconds

    @property
    def minutes(self):
        return self.__duration_in_seconds / 60

    @property
    def hours(self):
        return self.__duration_in_seconds / 3600
