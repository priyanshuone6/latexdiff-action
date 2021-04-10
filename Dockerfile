FROM python:latest

ADD script.py /script.py

RUN chmod +x script.py
ENTRYPOINT ["/script.py"]