FROM python:3.9-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
# יצירת תיקיית הדאטה כדי שלא יהיו שגיאות הרשאה
RUN mkdir /data && chmod 777 /data
EXPOSE 5000
CMD ["python", "app.py"]