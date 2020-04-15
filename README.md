# DRF_JWT_example
Simple Django Rest Framework API with JSON Web Token authentication

## Usage
- Create new user
```
$ curl --header "Content-Type: application/json" -X POST http://127.0.0.1:8000/api/user/create/ --data '{"email":"ichiro@mariners.com","username":"user","password":"password"}'
```
- Try to hit protected dummy endpoint
```
$ curl --header "Content-Type: application/json" -X GET http://127.0.0.1:8000/api/hello/
```
- Obtain token
``` 
$ curl --header "Content-Type: application/json" -X POST http://127.0.0.1:8000/api/token/obtain/ --data '{"username":"user","password":"password"}'
```
- Hit endpoint again, with credentials provided
```
curl --header "Content-Type: application/json" --header "Authorization: Bearer {token}"  -X GET http://127.0.0.1:8000/api/hello/
```