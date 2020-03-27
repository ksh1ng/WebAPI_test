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



## <font color=blue>Progress Record</font>

-  3/13/2020 (2.5hr)
    - P1~P7 and P11 
    - 了解如何撰寫一個API和其GET/POST methods

-  Todo: handle more requests per second
    -  ref:API的架構問題和stateless Docs.google.com/presentation/d/1ycF5l0uKNBc7yp0klJfrbuBrQGorNGkEkT8an9mAIKE/edit

-   3/25/2020 (2.5hr)
    -    測試規格規定的效能，並設定情境驗證效能是否符合規格





## <font color=blue>References</font>
- Building a REST API using Python and Flask | Flask-RESTful
https://www.youtube.com/watch?v=s_ht4AKnWZg

- jsonify - flask - Python documentation
https://kite.com/python/docs/flask.jsonify

- 在flask中使用jsonify和json.dumps的区别
https://blog.csdn.net/Duke_Huan_of_Qi/article/details/76064225

- Measure Web App Performance in Requests Per Second
https://www.youtube.com/watch?v=CXAF8uOduzk
