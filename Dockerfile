FROM python:3.7

ENV PYTHONUNBUFFERED 1

ENV WAITFORIT_VERSION="v2.4.1"
RUN curl -o /usr/local/bin/waitforit -sSL https://github.com/maxcnunes/waitforit/releases/download/$WAITFORIT_VERSION/waitforit-linux_amd64 && \
    chmod +x /usr/local/bin/waitforit

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:$PATH"

COPY pyproject.toml /deps/
COPY poetry.lock /deps/
ENV POETRY_VIRTUALENVS_CREATE false
RUN cd /deps && \
    poetry install --no-interaction && \
    rm -rf /deps

COPY . /code

WORKDIR /code

ENV PYTHONPATH="/code/"

ENTRYPOINT ["/code/docker-entrypoint.sh"]

CMD ["python", "app.py"]
