#my solution
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False
#better solution

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack: [NestedInteger] = []

        for nestedInt in nestedList:
            self.stack.append(nestedInt)

        self.stack.reverse()

    def _makeStackTopAnInteger(self):
        while self.stack and not self.stack[-1].isInteger():
            nestedInt: NestedInteger = self.stack.pop(-1)

            nestedList = nestedInt.getList()
            nestedListLength = len(nestedList)

            for i in range(nestedListLength-1, -1, -1):
                self.stack.append(nestedList[i])


    def next(self) -> int:
        self._makeStackTopAnInteger()

        if self.stack:
            topInt: NestedInteger = self.stack.pop(-1)
            return topInt.getInteger()

        return None

    def hasNext(self) -> bool:
        self._makeStackTopAnInteger()

        return self.stack
