# -*- coding: utf-8 -*-
def _(obj):
    if type(obj) != type(u""):
        return unicode(obj, 'utf-8')
    else:
        return obj
