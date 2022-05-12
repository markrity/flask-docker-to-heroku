# flask-docker-to-heroku

```
heroku login

heroku create sce-flask-template

heroku container:login

heroku container:push web --app sce-flask-template

heroku container:release web --app sce-flask-template

heroku logs --tail --app sce-flask-template

https://sce-flask-template.herokuapp.com/
```