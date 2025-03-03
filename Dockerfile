# Basis-Image mit Python 3.9.13
FROM python:3.9.13

# Setze Arbeitsverzeichnis
WORKDIR /app

# Kopiere die notwendigen Dateien
COPY requirements.txt .
COPY postBuild .

# Installiere alle Pakete aus requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Setze Datei-Upload-Limits auf unbegrenzt
RUN echo "fs.file-max = 524288" >> /etc/sysctl.conf && \
    echo "* soft nofile 524288" >> /etc/security/limits.conf && \
    echo "* hard nofile 524288" >> /etc/security/limits.conf

# Mache postBuild ausführbar und führe es aus
RUN chmod +x postBuild && ./postBuild

