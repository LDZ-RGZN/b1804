def makeBold(fn):
    def wrapped():
        return 'b' + fn()
    return wrapped

def makeItalic(fn):
    def wrapped():
        return 'i' + fn()
    return wrapped
@makeBold
def test1():
    return 'hello world-1'
@makeItalic
def test2():
    return 'hello world-2'

@makeBold
@makeItalic
def test3():
    return 'hello world-3'
