
##ipython

```python
%run helloworld.py
```

    helloworld!
    

%timeit与%time区别在于timeit多次执行，计算平均时间


```python
import numpy as np
a = np.random.randn(100, 100)
%timeit np.dot(a,a)
```

    83.6 µs ± 2.89 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    

