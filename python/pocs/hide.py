
import smtplib, ssl

port = 1026  # For SSL
#password = input("Type your password and press enter: ")

# Create a secure SSL context
#context = ssl.create_default_context()
EMAIL_HOST = 'smtp.protonmail.com'
EMAIL_HOST_USER = 'deathly_hallowz2048@protonmail.com'
EMAIL_HOST_PASSWORD = '$1lumos$2accio'
EMAIL_PORT = 1026
EMAIL_USE_TLS = True
with smtplib.SMTP_SSL(EMAIL_HOST, port, context="this is context or content") as server:
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    #server.send(EMAIL_HOST_USER,EMAIL_HOST_USER,"context")
    # TODO: Send email here 


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'apps', 'emails')