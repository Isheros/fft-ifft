FROM python:3-slim
COPY . /app/
RUN pip install pipenv

WORKDIR /app/
RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 pipenv install -d --system --ignore-pipfile

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
