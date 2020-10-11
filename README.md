# rating-overlay-api


## Running

Run `FLASK_ENV=development PYTHONPATH=$PWD python app.py`

- *On Windows run* `SET FLASK_ENV=development & SET PYTHONPATH=%cd% & python app.py`

Alternatively, using docker: `docker-compose -f rating-overlay-api.compose.yml -f rating-overlay-api.compose.dev.yml up`


## Testing

Run `FLASK_ENV=development PYTHONPATH=$PWD pytest`

- *On Windows run* `SET FLASK_ENV=development & SET PYTHONPATH=%cd% & pytest`

Alternatively, using docker: `docker-compose -f rating-overlay-api.compose.yml -f rating-overlay-api.compose.dev.yml run app pytest`


## Configuring CI

- You need to create a GitHub repository with the same name as the project.
- You need to enable the project on CircleCI.

## Deploying

- Run `zappa deploy <stage>`, replacing `<stage>` with the desired state.
- Run `zappa undeploy <stage>`, replacing `<stage>` with the desired state.
- Run `zappa update <stage>`, replacing `<stage>` with the desired state.

To check the logs, run `zappa tail <stage>`, replacing `<stage>` with the desired state.

See `zappa_settings.yml` for the available stages.


