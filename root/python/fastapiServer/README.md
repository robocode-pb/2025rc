[Download project](https://download-directory.github.io/?url=https://github.com/robocode-pb/2024rc/tree/main/Fr/WebMiddle/python/fastapiServer)

# fastapi server

``` bash
pip install fastapi uvicorn
python dbInit.py
```

```bash
python -m uvicorn main:app --reload
```

Щоб протестувати без https запустіть хром у небезпечному режимі
``` bash
start chrome --disable-web-security --user-data-dir="C:\chrome_dev"
```

http://127.0.0.1:8000/docs
