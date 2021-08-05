from CPP.cpptypematcher import CppTypeMatcher
from Parser.processentryline import ProcessEntryLine
from Parser.parseresultinterface import ParseResult


class ProcessEntryLineCpp(ProcessEntryLine):

    def comment(self, regex_result: ParseResult, context):
        print(f'/* {regex_result.parts()[0]} */')

    def data_type_start(self, regex_result, context):
        print('struct ', regex_result.parts()[0], 'Msg {', sep='')

    def data_field(self, regex_result, context):
        name_str = regex_result.parts()[0]
        raw_type_str = regex_result.parts()[1]
        type_str = CppTypeMatcher().process_type_str(raw_type_str)
        print(f'     {type_str} {name_str};')

    def data_type_end(self, regex_result, context):
        print('};')
