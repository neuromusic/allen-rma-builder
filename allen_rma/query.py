import copy

def filt(key,op,value):
    if op==None or value==None:
        return "[%s]" % (key)
    else:
        return "[%s$%s'%s']" % (key,op,value)

def parser(lookup):
    lookup = lookup.split('__')
    crit = lookup[0]
    try:
        key = lookup[1]
    except IndexError:
        key = 'name'
    try:
        op = lookup[2]
    except IndexError:
        op = 'il'
        
    return crit,key,op

class Q(object):
    """docstring for Query"""
    def __init__(self, model):
        super(Q, self).__init__()
        self.model = model
        self._criteria = {}
        self._include = []
        self._options = {}
        self._string = ''

    @property
    def string(self):
        s = "model::%s" % self.model

        if len(self._criteria)>0:
            s += ',rma::criteria'
            for k,v in self._criteria.iteritems():
                s += ',%s' % k
                for f in v['filters']:
                    s += f
        if len(self._include)>0:
            s += ',rma::include'
            for inc in include:
                s += ',%s' % inc

        if len(self._options)>0:
            s += ',rma::options'
            for k,v in self._options.iteritems():
                s += ',%s' % k
                for f in v['filters']:
                    s += f
        return s

    def criteria(self,**kwargs):
        for lookup,val in kwargs.iteritems():
            
            crit,key,op = parser(lookup)

            if crit in self._criteria:
                self._criteria[crit]['filters'].append(filt(key,op,val))
            else:
                self._criteria[crit] = {}
                self._criteria[crit]['filters'] = [filt(key,op,val),]
        return copy.deepcopy(self)
    