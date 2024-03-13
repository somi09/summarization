#
FROM --platform=linux/amd64 python:3.9

#
WORKDIR /code

#
COPY ./requirements.txt ./requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

#
COPY . .

#
CMD uvicorn src.main:backend_app --reload --workers 4 --host 0.0.0.0 --port 8000
# CMD ["tail", "-f", "/dev/null"]