class PeekingIterator:
    def __init__(self, iterator):
        self._iterator = iterator
        self._peeked = False
        self._current = None
    def peek(self):
        if not self._peeked:
            self._current = self._iterator.next()
            self._peeked = True
        return self._current
    def next(self):
        if self._peeked:
            self._peeked = False
        else:
            self._current = self._iterator.next()
        return self._current
    def hasNext(self):
        return self._peeked or self._iterator.hasNext()
