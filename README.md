## Learning OOP in Python

### 1 Install requirements

```bash
pip install -r requirements.txt
``` 

### 2 Run task
<p>*unix</p>

```bash
coverage run -m pytest -cov-report=html OOP_test.py

```

### 3 Test coverage
```
Name           Stmts   Miss  Cover   Missing
--------------------------------------------
OOP_begin.py      66      5    92%   32, 43-50, 59
OOP_test.py       66      1    98%   90
--------------------------------------------
TOTAL            132      6    95%
```