InnerProduct API Readme
===

## <font color=red>Server side</font>
### How to “USE”
>In your terminal:
```python
$ python innerproduct.py
```


## <font color=red>Client side</font>
### How to “USE”
#### <font color=green>POST request (user)</font>
>In your terminal:
```python
$  curl -H "Content-Type: application/json; charset=utf-8" -X POST --data '{"x":[], "y":[]}' http://<your_domain>/innerproduct
```

#### <font color=green>GET request (admin)</font>
>In your terminal:
```python
$  curl http://<your_domain>/info
```






