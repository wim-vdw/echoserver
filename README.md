# echoserver

```shell
# Start Flask app in debug mode. 
flask --app echoserver run --debug

# Start production app with 2 workers.
gunicorn --workers=2 --access-logfile - 'echoserver:create_app()'
```
