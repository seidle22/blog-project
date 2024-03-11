FROM --platform=linux/amd64 python:3.9.16

WORKDIR /project

COPY . /project/

RUN pip install pipenv && pipenv --python 3.9 install --deploy --ignore-pipfile

CMD ["pipenv", "run", "python", "run.py"]
