FROM python:3.10-slim

# İş qovluğu təyin edin
WORKDIR /app

# Ətraf mühit dəyişənlərini təyin edin
ENV DJANGO_SETTINGS_MODULE=django_app.settings

# Requirements faylını kopyalayın və paketləri yükləyin
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Layihə fayllarını kopyalayın
COPY . .
