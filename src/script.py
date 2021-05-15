def process(msg, context):
    _upgrade = msg.latest_data.fields.get('Upgrade')
    _status = msg.latest_data.fields.get('::Status')
    _upgradeToWs = _upgrade.lower() == 'websocket' if _upgrade else False
    _status101 = _status.find('101') != -1 if _status else False
    context.memory['http_to_ws']['http']['serverUpgrade'] = _upgradeToWs and _status101
    return SUCCESS


res = process(msg, context)
