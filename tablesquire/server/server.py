import flask
import flask.ext.sqlalchemy
import flask.ext.restless

from tablesquire.server.db import models

app = flask.Flask(__name__)
app.config['DEBUG'] = True

manager = flask.ext.restless.APIManager(app, session=models.get_session())

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(models.Session, methods=['GET', 'POST', 'DELETE'])

# start the flask loop
app.run(host='0.0.0.0', debug=True)
