# matplotlib

## import
```
import matplotlib
import matplotlib.pyplot as plt
```

## in .py
```python
#指定默认字体，在~/.matplotlib/fontList.json中发现simhei
matplotlib.rcParams['font.family']='simhei'  
#解决负号'-'显示为方块的问题  
matplotlib.rcParams['axes.unicode_minus']=False  
```

## in .ipynb
### 调整大小
```python
import pylab
pylab.rcParams['figure.figsize'] = (15.0, 8.0)
```

> 可以考虑使用live templates固定plt->...
