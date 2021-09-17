FROM tiangolo/uwsgi-nginx-flask:python3.8
WORKDIR /app

COPY Pipfile.lock /app
COPY Pipfile /app

RUN pip install pipenv

RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 pipenv install -d --system --ignore-pipfile

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
