FROM python:3.12.5


SHELL ["/bin/bash", "-c"]


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt-get update && apt-get -qy install gcc libjpeg-dev libxslt-dev libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash buha && chmod 777 /opt /run


WORKDIR /buha

RUN mkdir /buha/static && mkdir /buha/media && chown -R buha:buha /buha && chmod 755 /buha

COPY --chown=buha:buha . .

RUN pip install -r requirements.txt

USER buha

CMD ["gunicorn","-b","0.0.0.0:8001","soaqaz.wsgi:application"]

ENV BOT_TOKEN = '5641597027:AAGuUaoQpMPmsxqZwXz1KNwJF6I1P1Pvih0'