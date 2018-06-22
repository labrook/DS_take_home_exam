import numpy as np


class Expander(object):
    def __init__(self, aa):
        self.aa = aa
    def doit(self, bb):
        cc = np.empty((len(bb), len(self.aa)))
        for ii in range(bb.shape[0]):
            cc[ii,self.aa.index(bb[ii])]=1
            
        return np.asarray(cc)

    
def do_work(data, places=[]):
    if places == []:
        places = range(data.shape[1])
    new_data = []
    for i in places:
        stuff=[]
        for value in data[:,i]:
            if value not in stuff: stuff.append(value)
        thing = Expander(stuff)
        new_data.append(thing.doit(data[:,i]))
    for i in range(data.shape[1]):
        if i in places:
            continue
        else:
            new_data.append(data[:,[i]])
    return np.concatenate(new_data,axis=1)


def test1():
    arr = np.asarray([['spam', 11], ['spam', 3.14], 
                      ['eggs', -20], ['spam', 42]])
    out = do_work(arr)
    assert ((out == 0) | (out == 1)).all()

    return True


def test2():
    arr = np.asarray([['spam', 11], ['spam', 3.14], 
                      ['eggs', -20], ['spam', 42]])
    out = do_work(arr, [0])
    assert out.shape == (4, 3)
    assert all(arr[:, -1] == out[:, -1])

    return True


def test3():
    arr = np.array([['spam'], ['spam'], ['eggs'], ['spam']])
    out = do_work(arr)
    assert out.shape == (4, 2)
    assert np.all(out == np.array([[0, 1], [0, 1], [1, 0], [0, 1]]))

    return True


if __name__ == '__main__':
    test1()
    test2()
    test3()
    print('Passed all tests!')
