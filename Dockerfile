FROM python:3.7

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt update
#RUN apt install -y nginx

#RUN rm /etc/nginx/sites-available/default

#COPY scripts/default.conf /etc/nginx/sites-available/default



COPY . .

RUN chmod +x ./entrypoint.sh


CMD ["./entrypoint.sh", "python", "manage.py", "runserver", "0.0.0.0:8000"]

