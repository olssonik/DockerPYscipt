FROM python:3.9-slim
WORKDIR /
COPY cpu.py .
RUN pip install psutil
CMD ["python", "cpu.py"]