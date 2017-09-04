import string


#VIP Charset mapping
jovanotti_charsmap = {'s': 'f','S':'F',
                     'z': 'ff','Z':'FF'}

costanzo_charsmap = {'s': 't', 'S':'T',
                    'z': 'tt','Z':'TT'}


def _vip_replace(payload,vip_charmap):
    for k, v in vip_charmap.items():
        payload = payload.replace(k, v)
    return payload


def jovanotty(payload):
    return _vip_replace(payload,jovanotti_charsmap)


def cottanzo(payload):
    return _vip_replace(payload,costanzo_charsmap)
