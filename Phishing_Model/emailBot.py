import imaplib
import email
from email.header import decode_header
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import joblib
from bs4 import BeautifulSoup

# Load your spam detection model and vectorizer
spam_model = joblib.load('spam_detection_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Account credentials
username = "timepasskarraha2@gmail.com"
password = "xwjb pose vamr ddax"

# Function to extract links from email body
def extract_links(email_body):
    url_pattern = re.compile(r'https?://[^\s]+')
    return url_pattern.findall(email_body)

# Function to preprocess email body
def preprocess_body(body):
    soup = BeautifulSoup(body, 'html.parser')
    text = soup.get_text()
    return text

# Function to interact with a URL using Selenium
def interact_with_url(url):
    driver.get(url)
    try:
        # Increase the timeout
        button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Click Me')]"))
        )
        button.click()
        print("Clicked the button!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Setup Selenium WebDriver (this example uses Edge WebDriver)
edge_driver_path = r'D:\Downloads\edgedriver_win64\msedgedriver.exe'
service = EdgeService(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service)

# Create an IMAP4 class with SSL
mail = imaplib.IMAP4_SSL("imap.gmail.com")
# Authenticate
mail.login(username, password)

# Select the mailbox you want to check
mail.select("inbox")

# Search for specific mails
status, messages = mail.search(None, 'FROM', '"abhisheksingh.vizag@gmail.com"', 'UNSEEN')

# Check if the search was successful
if status == 'OK':
    mail_ids = messages[0].split()

    # Fetch the email
    for i in mail_ids:
        status, msg_data = mail.fetch(i, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                email_subject = decode_header(msg["subject"])[0][0]
                if isinstance(email_subject, bytes):
                    email_subject = email_subject.decode()
                email_from = msg.get("from")
                print(f"From: {email_from}")
                print(f"Subject: {email_subject}")

                # If the email message is multipart
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            body = part.get_payload(decode=True).decode()
                            if "attachment" not in content_disposition:
                                print("Body:", body)
                                
                                # Preprocess email body
                                email_features = vectorizer.transform([processed_body])
                                is_spam = spam_model.predict(email_features)[0]

                                if is_spam:
                                    print("This email is classified as spam. Links will not be opened.")
                                else:
                                    print("This email is not spam. Opening links...")
                                    links = extract_links(body)
                                    for link in links:
                                        try:
                                            interact_with_url(link)
                                            print(f"Successfully interacted with link: {link}")
                                        except Exception as e:
                                            print(f"Error interacting with link {link}: {str(e)}")
                        except Exception as e:
                            print(f"An error occurred while processing part: {e}")
                else:
                    content_type = msg.get_content_type()
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        print("Body:", body)
                        
                        # Preprocess email body
                        processed_body = preprocess_body(body)
                        
                        # Predict if the email is spam
                        email_features = vectorizer.transform([processed_body])
                        is_spam = spam_model.predict(email_features)[0]
                        
                        if is_spam:
                            print("This email is classified as spam. Links will not be opened.")
                        else:
                            print("This email is not spam. Opening links...")
                            links = extract_links(body)
                            for link in links:
                                interact_with_url(link)
else:
    print("No messages found")

# Close the browser after interactions
driver.quit()