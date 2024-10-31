import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import max6675
import requests

baseUrl = "url"

def calculateTemperature():
  cs = 15
  sck = 23
  so = 21

  max6675.set_pin(cs, sck, so, 1)
  a = max6675.read_temp(cs)
  max6675.time.sleep(2)
  return a

def sendEmail(to_address: str, subject: str, body: str) -> None:
  smtp_server = "smtp.gmail.com"
  smtp_port = 587
  from_address = "soyudem@gmail.com"
  password = "123gravedad456"

  try:
    message = MIMEMultipart()
    message["From"] = from_address
    message["To"] = to_address
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
      server.starttls()
      server.login(from_address, password)
      server.sendmail(from_address, to_address, message.as_string())
      print(f"Email sent to {to_address}")
  
  except smtplib.SMTPException as e:
    print(f"Error while sending email: {e}")


def clearFiles() -> None:
  try:
    response = requests.post(f"{baseUrl}/clearfiles")
    print(f"Clear Files - Status Code: {response.status_code}, Response: {response.text}")
  except requests.RequestException as e:
    print(f"Error clearing files: {e}")

def uploadTemperature(temp: str) -> None:
  try:
    response = requests.post(f"{baseUrl}/uploadtemperature/{temp}")
    print(f"Upload Temperature - Status Code: {response.status_code}, Response: {response.text}")
  except requests.RequestException as e:
    print(f"Error uploading temperature: {e}")

def uploadSound(base64String: str) -> None:
  payload = {"base64": base64String}
  headers = {'Content-Type': 'application/json'}
  try:
    response = requests.post(f"{baseUrl}/uploadsound", json=payload, headers=headers)
    print(f"Upload Sound - Status Code: {response.status_code}, Response: {response.text}")
  except requests.RequestException as e:
    print(f"Error uploading sound: {e}")

def downloadTemperature() -> str:
  try:
    response = requests.get(f"{baseUrl}/downloadtemperature")
    print(f"Download Temperature - Status Code: {response.status_code}, Response: {response.text}")
    return response.text
  except requests.RequestException as e:
    print(f"Error downloading temperature: {e}")
    return ""

def downloadSound() -> str:
  try:
    response = requests.get(f"{baseUrl}/downloadsound")
    print(f"Download Sound - Status Code: {response.status_code}, Response: {response.text[:10]}...")
    return response.text
  except requests.RequestException as e:
    print(f"Error downloading sound: {e}")
    return ""