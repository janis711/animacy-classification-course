FROM python:3.9.13
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install git+https://github.com/forTEXT/gitma
CMD ["jupyter", "notebook", "animacy_annotation.ipynb", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]


