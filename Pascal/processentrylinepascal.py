from Pascal.pascaltypematcher import PascalTypeMatcher
from Parser.processentryline import ProcessEntryLine
from Parser.parseresultinterface import ParseResult


class ProcessEntryLinePascal(ProcessEntryLine):

    def comment(self, regex_result: ParseResult, context):
        print('{ ', regex_result.parts()[0], ' }', sep='')

    def data_type_start(self, regex_result, context):
        print(f'{regex_result.parts()[0]}Msg = packed record')

    def data_field(self, regex_result, context):
        name_str = regex_result.parts()[0]
        raw_type_str = regex_result.parts()[1]
        type_str = PascalTypeMatcher().process_type_str(raw_type_str)
        print(f'     {name_str}:    {type_str};')

    def data_type_end(self, regex_result, context):
        print(f'end ;')
