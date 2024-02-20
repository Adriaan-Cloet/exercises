# ex vraag 1 -> flags

# klasse Flag
class Flag:
    def __init__(self, country, colors, horizontal):
        self.country = country
        self.colors = colors # moet hier niet privé staan omdat de setter een privé waarde gaat geven
        self.horizontal = horizontal

    # @field.setter
    # def field(self, value):
    #     if value < 0:
    #         raise valueError()
    #     self.__field = value
    
    # @property
    # def field(self):
    #     return self.__field

    @property
    def colors(self):
        return self.__colors

    @colors.setter
    def colors(self, value):
        if value is None or len(value) == 0:
            raise ValueError
        self.__colors = value

    