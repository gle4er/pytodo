FROM python:3.10.9-slim

RUN useradd -ms /bin/bash pytodo && pip install pipenv
USER pytodo
WORKDIR /home/pytodo
ENV PYTHONPATH "${PYTHONPATH}:/home/pytodo"
COPY . /home/pytodo
RUN pipenv install
EXPOSE 8000
CMD ["bash", "-c", "pipenv run alembic upgrade head && pipenv run uvicorn main:app --host 0.0.0.0 --port 8000"]
