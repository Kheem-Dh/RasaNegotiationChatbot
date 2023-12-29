# Rasa Chatbot for Product Negotiation

This project is a chatbot built using Rasa, an open-source machine learning framework for automated text and voice-based conversations. The primary function of this chatbot is to negotiate prices for products, specifically for items like the Samsung Galaxy S10 and iPhone 8.

## Features

- Responds to basic greetings and farewells.
- Engages in small talk about the user's mood.
- Conducts price negotiations for Samsung Galaxy S10 and iPhone 8.
- Custom action to handle price negotiation logic.

## Installation

To run this project, you need to have Python installed on your machine. The project was developed using Python 3.9.

### Clone the Repository

```bash
git clone https://github.com/Kheem-Dh/RasaNegotiationChatbot.git
cd RasaNegotiationChatbot
```

## Setup Virtual Environment

It's recommended to use a virtual environment to avoid conflicts with other projects or system-wide packages.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Install Dependencies

Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Configuration

`endpoints.yml`
Make sure the endpoints.yml file is properly set up for the action server:

```bash
action_endpoint:
  url: "http://localhost:5055/webhook"
```

`credentials.yml`
Configure your credentials.yml file if you're integrating with external channels like Slack, Facebook Messenger, etc.

## Running the Bot

### Start the Action Server

Run the following command in a separate terminal to start the action server:

```bash
rasa run actions
```

## Train the Model

Before you can chat with your bot, you need to train it:

```bash
rasa train
```

## Start Rasa Server

In a new terminal, start the Rasa server:

```bash
rasa shell
```

## Usage

Once the Rasa server is running, you can start chatting with the bot in the terminal.

## Custom Actions

The actions.py file contains the custom actions used for negotiating prices. Ensure that this file is properly maintained and updated as per your negotiation logic.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.
