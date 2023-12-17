FROM python:3.10-slim

WORKDIR /core

COPY . /core

RUN pwd
RUN ls

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN pwd
RUN ls

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
