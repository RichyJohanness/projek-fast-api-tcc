# Gunakan image dasar
FROM python:3.9

# Atur direktori kerja
WORKDIR /app

# Salin requirements.txt dan install dependensi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin kode aplikasi
COPY . .

# Ekspos port
EXPOSE 8080

# Jalankan aplikasi
CMD ["python", "dior.py"]
