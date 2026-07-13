FROM python:3.13

WORKDIR /usr/src/autoservice_manager

COPY requirements.txt /usr/src/autoservice_manager

RUN pip install --no-cache-dir -r requirements.txt

COPY AutoServiceManager/. /usr/src/autoservice_manager

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]