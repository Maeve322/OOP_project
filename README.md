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
Name           Stmts   Miss  Cover 
----------------------------------
shop.py           96      8    92%
test_shop.py      91      1    99%
----------------------------------
TOTAL            187      9    95%
```