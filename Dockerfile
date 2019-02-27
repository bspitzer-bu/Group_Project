FROM python

WORKDIR /root/gpcr-atlas/

COPY requirements/ requirements/

COPY src/ src/

RUN pip install -r requirements/development.txt

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]
