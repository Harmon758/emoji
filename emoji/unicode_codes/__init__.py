# -*- coding: utf-8 -*-

from emoji.unicode_codes.en import *
from emoji.unicode_codes.es import *
from emoji.unicode_codes.pt import *


__all__ = [
    'EMOJI_UNICODE', 'UNICODE_EMOJI',
    'EMOJI_UNICODE_ENGLISH', 'UNICODE_EMOJI_ENGLISH',
    'EMOJI_ALIAS_UNICODE_ENGLISH', 'UNICODE_EMOJI_ALIAS_ENGLISH',
    'EMOJI_UNICODE_SPANISH', 'UNICODE_EMOJI_SPANISH',
    'EMOJI_UNICODE_PORTUGUESE', 'UNICODE_EMOJI_PORTUGUESE',
]


EMOJI_UNICODE = {
    'en': EMOJI_UNICODE_ENGLISH,
    'es': EMOJI_UNICODE_SPANISH,
    'pt': EMOJI_UNICODE_PORTUGUESE,
}

UNICODE_EMOJI = {
    'en': UNICODE_EMOJI_ENGLISH,
    'es': UNICODE_EMOJI_SPANISH,
    'pt': UNICODE_EMOJI_PORTUGUESE,
}
