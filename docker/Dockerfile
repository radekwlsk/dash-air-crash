FROM python:3.7.4-slim
ARG USER_ID=1000

ENV PYTHONUNBUFFERED 1
ENV HOME=/home/dash

# Create the user and group to run the Django application as
RUN addgroup --system --gid $USER_ID dash \
    && adduser --system --home $HOME --uid $USER_ID --ingroup dash dash

COPY ./docker/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh \
    && chmod +x /start.sh

COPY ./app /app
RUN chown -R dash /app

USER dash
ENV PATH "${PATH}:${PYTHONUSERBASE:-/home/dash/.local}/bin"

RUN pip install --no-cache-dir --user -r /app/requirements.txt

WORKDIR /app

CMD ["/start.sh"]