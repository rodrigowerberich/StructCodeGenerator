from processentryline import ProcessEntryLine
from parseresultinterface import ParseResult


class ProcessEntryLineC(ProcessEntryLine):

    def comment(self, regex_result: ParseResult, context):
        print(f'/*{regex_result.parts()[0]} */')

    def data_type_start(self, regex_result: ParseResult, context):
        context.data_type_name = regex_result.parts()[0]
        print('typedef struct {')

    def data_field(self, regex_result: ParseResult, context):
        print(f'    {regex_result.parts()[1]} {regex_result.parts()[0]}')

    def data_type_end(self, regex_result: ParseResult, context):
        print('} ', context.data_type_name, 'Msg;', sep='')
