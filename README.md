# flask-docker-to-heroku


### Running locally
```
docker build -t sce-flask-template .
docker run -p PORT_ON_MACHINE:PORT_IN_CONTAINER IMAGE_TAG
docker run -p 8080:5000 sce-flask-template
```


### Deploying to Heroku

```
heroku login

heroku create sce-flask-template

heroku container:login

heroku container:push web --app sce-flask-template

heroku container:release web --app sce-flask-template

heroku logs --tail --app sce-flask-template

https://sce-flask-template.herokuapp.com/
```