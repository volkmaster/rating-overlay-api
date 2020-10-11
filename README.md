# Age of Empires II Definitive Edition Stream Overlay API


[![CircleCI](https://circleci.com/gh/volkmaster/rating-overlay-api/tree/master.svg?style=shield)](https://app.circleci.com/pipelines/github/volkmaster/rating-overlay-api)


## Installation

- Install poetry: `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`
- Create virtual environment: `python -m venv venv`
- Activate virtual environment: `source venv/bin/activate`
    - *On Windows run* `.\venv\Scripts\activate`
- Install dependencies: `poetry install`

Alternatively, using docker: `docker-compose build`

### Setup pre-commit hook

Run `pre-commit install`

## Running

Run `ENV=development FLASK_ENV=development PYTHONPATH=$PWD python app.py`

- *On Windows run* `SET ENV=development& SET FLASK_ENV=development& SET PYTHONPATH=%cd%& python app.py`

Alternatively, using docker: `docker-compose up`
    - To run the container in detached mode: `docker-compose up -d`
    - To stop the container running in detached mode: `docker-compose stop`

## Testing

Run `ENV=development FLASK_ENV=development PYTHONPATH=$PWD python -m pytest`

- *On Windows run* `SET ENV=development& SET FLASK_ENV=development& SET PYTHONPATH=%cd%& python -m pytest`

Alternatively, using docker: `docker-compose run rating-overlay-api python -m pytest`


## Configuring CI

- You need to create a GitHub repository with the same name as the project.
- You need to enable the project on CircleCI (also set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_REGION` environment variables).

## Deploying

- Run `zappa deploy <stage>`, replacing `<stage>` with the desired state.
- Run `zappa undeploy <stage>`, replacing `<stage>` with the desired state.
- Run `zappa update <stage>`, replacing `<stage>` with the desired state.

To check the logs, run `zappa tail <stage>`, replacing `<stage>` with the desired state.

See `zappa_settings.yml` for the available stages.

To get the API Gateway URL for the desired state, run `aws ssm get-parameter --name "/rating-overlay-api/<stage>/api_url"`.
- Before executing the command set AWS profile: `AWS_PROFILE=aoe` *( Windows:* `SET AWS_PROFILE=aoe` *)* 



