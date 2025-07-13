class TwoDigits:
    regex = '[0-9]+'

    def to_python(self, value):
        number = int(value)
        if number > 15:
            return number
        else:
            raise ValueError('Error numero equivocado')

    def to_url(self, value):
        return value


class validYearConverter:
    regex = r'([2-9]\d{3-9}\d{2}|199\d)'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value
