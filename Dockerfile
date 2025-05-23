FROM python:3.9-slim
WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY data ./data
COPY main.py .

#DELETE THIS IN THE FUTURE!!!
COPY secret_keys.env .

EXPOSE 8080

#RUN useradd app
#USER app

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]