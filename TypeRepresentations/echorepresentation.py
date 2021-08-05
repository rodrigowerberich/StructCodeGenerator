from TypeRepresentations.typerepresentation import TypeRepresentation


class EchoRepresentation(TypeRepresentation):

    def __init__(self, str_to_echo: str):
        self._str_to_echo = str_to_echo

    def get_representation(self) -> str:
        return self._str_to_echo
