## Learning OOP in Python

### 1 Install requirements

```bash
pip install -r requirements.txt
``` 

### 2 Run task
<p>*unix</p>

```bash
$ coverage run -m pytest -cov-report=html test_shop.py
$ coverage html
```

### 3 Test coverage
```
Name                Stmts   Miss  Cover
---------------------------------------
Mixins.py               5      0   100%
ShopExceptions.py       5      1    80%
shop.py               112      9    92%
test_shop.py          102      1    99%
---------------------------------------
TOTAL                 224     11    95%
```