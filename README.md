# WiFi Server

## Usage

ESP32(Installed MicroPython or CircuitPython)

Rewrite html=
```python
def web_page():
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
  <h1>Hello World</h1>
</body>
</html>
 """
``` 
## Execute

```sh
%Run -c $EDITOR_CONTENT
```

On your phone or PC
Verify SSID and Password

Browser
```
http://192.168.5.1
```
