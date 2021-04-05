# pull official base image
FROM python:3.9.2-alpine


# Directorye for the "app" user
RUN mkdir -p /home/appuser

# Create App User
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

#Create even more directories
ENV HOME=/home/appuser
ENV APP_HOME=/home/appuser/django_app
RUN mkdir ${APP_HOME}
RUN mkdir $APP_HOME/static
WORKDIR ${APP_HOME}

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .


RUN chown -R appuser:appgroup ${APP_HOME}

USER appuser

# run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
