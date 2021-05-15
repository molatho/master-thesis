class ScriptProcessor(IProcessor):
    def __init__(self, script: Script, inDirection: ProcessingDirection = ProcessingDirection.ANY):
        super().__init__(inDirection)
        self._script_ = script

    def process(self, msg: Message, direction: ProcessingDirection, context: StateContext) -> Tuple[Message,  ProcessingResult]:
        _locals = {'msg': msg, 'direction': direction,
                   'res': ProcessingResult.SUCCESS,
                   'context': context}
        _globals = {
            'SUCCESS': ProcessingResult.SUCCESS,
            'ERROR': ProcessingResult.ERROR,
            'INCOMPLETE': ProcessingResult.INCOMPLETE,
            'DROP': ProcessingResult.DROP,
            'BACK': ProcessingResult.BACK,
        }
        try:
            exec(self._script_.body, _globals, _locals)
        except Exception as e:
            print(f'Script error: {str(e)}')
            return (_locals['msg'], ProcessingResult.ERROR)
        return (_locals['msg'], _locals['res'])
