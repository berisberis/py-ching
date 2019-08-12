FROM python:3.6-alpine3.7

ENV WORKDIR "/var/www"
ENV FLASK_APP iching
ENV FLASK_ENV development

# Install system libraries
RUN apk upgrade --update && apk --no-cache add \
    bash nano

# Cleanup
RUN rm -rf /var/cache/apk/* \
    && find / -type f -iname \*.apk-new -delete \
    && rm -rf /var/cache/apk/*

ADD ./entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh

RUN mkdir -p ${WORKDIR}

WORKDIR ${WORKDIR}

ADD ./requirements.txt ./
RUN pip install -r requirements.txt


ADD ./iching /var/www/iching

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/iching/static

# EXPOSE 80

ENTRYPOINT ["/opt/entrypoint.sh"]

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]