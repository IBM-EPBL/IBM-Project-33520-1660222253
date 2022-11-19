FROM python:latest
WORKDIR /app
ADD app.py .
COPY requirements.txt app.py
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install flask
EXPOSE 5000
CMD ["python","app.py"]
