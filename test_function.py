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
