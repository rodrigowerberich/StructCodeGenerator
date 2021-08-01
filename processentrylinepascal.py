from processentryline import ProcessEntryLine
from parseresultinterface import ParseResult
import re


class ProcessEntryLinePascal(ProcessEntryLine):

    def comment(self, regex_result: ParseResult, context):
        print('{ ', regex_result.parts()[0], ' }', sep='')

    def data_type_start(self, regex_result, context):
        print(f'{regex_result.parts()[0]}Msg = packed record')

    def data_field(self, regex_result, context):
        # Very simple naive solution
        type_str = regex_result.parts()[1]
        array_number_regex = re.findall(r'(\w+)\[(\d+)\]', type_str)
        if array_number_regex:
            array_number_regex = array_number_regex[0]
            type_str = array_number_regex[0]
            number = int(array_number_regex[1])
            type_str = f'array[{0}..{number-1}] of {type_str}'
        else:
            if type_str.lower() == 'int':
                type_str = 'LongInt'
        print(f'     {regex_result.parts()[0]}:    {type_str};')

    def data_type_end(self, regex_result, context):
        print(f'end ;')
