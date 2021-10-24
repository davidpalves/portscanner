# Port Scanner

This is only for educational purposes use it on your own risk.

![portscanner](https://user-images.githubusercontent.com/14933043/138602136-b2f0d674-123e-492f-9dbe-5d072aeb982b.gif)


## install all dependencies using
```
pip install -r requirements.txt
```
------------

## Basic Usage
```
python portscanner.py -u ip_address
```
Or
```
python portscanner.py --url ip_address
```

#### Arguments accepted

For getting the all arguments you can use, execute `python portscanner.py -h`

```
usage: portscanner.py [-h] --url URL [--timeout TIMEOUT]
                      [--lowest-port LOWEST_PORT]
                      [--highest-port HIGHEST_PORT]

Scan open ports easily

optional arguments:
  -h, --help            show this help message and exit
  --url URL, -u URL     URL to be scanned
  --timeout TIMEOUT, -t TIMEOUT
                        Set connection timeout value (in seconds)
  --lowest-port LOWEST_PORT, -lp LOWEST_PORT
                        Define which port (0-65535) should start being scanned
  --highest-port HIGHEST_PORT, -hp HIGHEST_PORT
                        Define which port (0-65535) should finish being
                        scanned

```
