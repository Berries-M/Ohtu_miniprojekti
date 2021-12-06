# pylint: disable=invalid-name
"""Hyväksymistestausluokka
"""

#Pylint disablettu toistaiseksi
from stub_io import StubIO # pylint: disable=import-error

class ReadingtipLibrary: # pylint: disable=invalid-name
    """Luokka joka vastaa vaatimusten testaamisesta
    """

    def __init__(self):
        """Luokan konstruktori
        """
        self._io = StubIO()

    def input(self, value):
        """Luo syötteen
        """
        self._io.initial_add(value)

    def output_should_contain(self, value):
        """Tarkistaa tulosteen
        """
        outputs = self._io.output

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )


    def run_application(self):
        """Käynnistää sovelluksen
        """
        self._io.start()

    def last_output_should_contain(self, value):
        """Tarkistaa viimeisen tulosteen
        """
        if len(self._io.output) > 0:
            last_output = self._io.output.pop()
        else:
            last_output =  ""
        if last_output != value:
            raise AssertionError(
                f"{value} is not in {last_output}"
            )


    def database_must_be_empty(self):
        """Tarkistaa onko tietokanta tyhjä
        """
        if len(self._io.database) > 0:
            raise AssertionError(
                "Database is not empty"
            )
