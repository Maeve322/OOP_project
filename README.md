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
shop.py           83      5    94%   40, 51-58, 67
test_shop.py     100      1    99%   130
--------------------------------------------
TOTAL            183      6    97%
```