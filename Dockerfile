FROM python:3.10

ENV TIMDb_API_KEY=MUST_BE_PROVIDED
LABEL TIMDb_API_KEY_REQUIRED=true

WORKDIR /app

COPY . .
RUN rm -rf venv
RUN pip install -r requirements.txt

# Expose the port that the Flask app will run on
EXPOSE 5000

ENTRYPOINT [ "./run.sh" ]
