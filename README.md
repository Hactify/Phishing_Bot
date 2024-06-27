# Recon 🛡️

## Part-1 : [Explanation Video part 1](https://youtu.be/Ot1H5_no8ZI)
## Part-2 : [Explanation Video part 2](https://youtu.be/meD-VA5vk6E)

### Make Sure you have pytorch installed.
### To install Pytorch : pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
### If you face difficulty while installing pytorch goto https://pytorch.org/get-started/locally/ 
### Also install transformmers by pip install transformers

# Overview

# Problem we Solved ⁉️
The problem is divided into two parts the first is to gather the email Id of persons in a particular domain, and gather their information the next is to send a phishing mail that looks legitimate to the user in that domain for this we trained a model on phishing mails that contains phishing Emails text and safe Email text , the model then generates a phishing mail which also contains a link and then sends it to the desired user. Now the other part of the project is that , it then receives the mail sent by the bot and checks weather the mail is legitimate or not if the mail is a phishing mail it will not click on the link and exit by saying that the mail received is spam and if it is not spam it will open the link.

The project is divided into two parts:

### Part 1: Generating and Sending Phishing Emails
Email Gathering: The first step is to gather email addresses of individuals within a specific domain. This involves scraping or collecting email addresses from a domain, along with gathering any relevant information about the users.
Phishing Email Generation: The next step involves generating phishing emails. This is achieved by training an AI model using a dataset that contains examples of both phishing and legitimate emails. The model learns the characteristics of phishing emails and is then used to generate a new phishing email that appears legitimate.
Email Sending: The generated phishing email, which includes a phishing link, is sent to the targeted users within the domain.

### Part 2: Detecting and Handling Received Emails
Email Receiving: The system receives the emails sent by the bot. This involves connecting to an email server, retrieving unseen emails from a specified sender.
Phishing Detection: The received emails are then analyzed to determine whether they are legitimate or phishing attempts. The same AI model, trained on the dataset of phishing and safe emails, is used to classify the emails.
Link Interaction Decision:
If the email is classified as phishing, the system will avoid clicking on any links within the email and will exit with a message indicating that the email is spam.
If the email is classified as legitimate, the system will interact with the links contained in the email.

# The challenges we ran into 🚧

Firstly the model was not able to recognize the difference between legitimate mails and phishing mails. So, we required the need for pre preprocessing the data and refining it making it clearer for the model to enhance its detection. 

We faced problems regarding the integration of AI model into our code but at the end it got integrated successfully. 

Initially we were not able to detect how we will be able to scrape data out of the email that we found from the domain but eventually we figured out the solution for it

## Features 😎

- Dashboard
- Profiling
- Domain email finder
- Phishing Email generation
- Smart email recognition
- Bulk Email sender

# Technology Stack ⚙️💻
1. Python
2. Pytorch
3. Pandas
4. Naive Bayes Algorithm
5. HTML, CSS, JS
6. GPT-2 Tokenizer
7. Sklearn
8. Git
9. PostgreSQL
10. Flask
