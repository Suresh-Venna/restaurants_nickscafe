From python:3.6-alpine
Expose 8000
RUN apk add --no-cache gcc python3-dev musl-dev
ADD . /nickscafedocker
WORKDIR /nickscafedocker
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD [ "python", "nickscafedocker/manage.py", "runserver", "0.0.0.0:8000" ]