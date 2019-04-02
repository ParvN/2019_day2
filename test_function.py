import numpy as np
import pytest
import maxima  
from maxima import find_maxima

#def test_first_set():
  # x = [0,1,2,1,2,1,0]
   # x = [1, 2, 2, 1]   
   #assert  find_maxima(x) == [1,2]

test_case_1 = [([0, 1, 2, 1, 2, 1, 0],[2,4]),([-i**2 for i in range(-3, 4)],[3]),([np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)],[16,78]),
([4, 2, 1, 3, 1, 2],[0,3,5]),([4, 2, 1, 3, 1, 5],[0,3,5]),([4, 2, 1, 3, 1],[0,3]),([1, 2, 2, 3, 1],[1,3]),([1, 3, 2, 2, 1],[1,3]),([3, 2, 2, 3],[0,3])]

@pytest.mark.parametrize('inp,exp',test_case_1)
def test_case_1_maxima(inp,exp):
    out = find_maxima(inp)
    assert out ==exp

def test_randomized():
    #given
    seedval =0
    rand_gen = np.random.RandomState(seed = seedval)
    numel = rand_gen.randint(0,1000)
    test_vec = rand_gen.random_integers(low=1,high=20,size=numel)
    print(f'test_vec:{test_vec}')
    
    #When
    out =find_maxima(test_vec)
    
    #Then
    if out[0]==0:
        assert test_vec[0] > test_vec[1]
    else:
        for k in range(1,out[0]):
            assert test_vec[k]>=test_vec[k-1]
    if len(out)>3 :
        up=False
        for i,j in zip(out[1:-2],out[2:-1]):
            for k in range(i,j):
                if test_vec[k] >test_vec[k-1]:
                    up = True
                if test_vec[k] < test_vec[k-1]:
                    assert not up
