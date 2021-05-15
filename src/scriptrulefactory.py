class ScriptRuleFactory(IFactory):
    def __init__(self) -> None:
        super().__init__(RULE_SCRIPT)

    def build(self, plant: Site, obj: Dict[str, Any]) -> Any:
        _scriptobj = obj['config']
        _name = obj['name']
        _script = plant.build(SCRIPT, _scriptobj)
        return ScriptRule(_name, _script)
