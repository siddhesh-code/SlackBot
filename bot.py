import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import openai

# Initialize Slack client
slack_token ='xoxp-5806358566918-5813001744802-5836822728768-6b76a09265a07150262385589bc38607'
client = WebClient(token=slack_token)

# Initialize OpenAI client
openai.api_key = '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'

def get_gpt_response(prompt):
    """Get a response from GPT-3 based on the given prompt."""
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=150)
    return response.choices[0].text.strip()

def post_message_to_slack(channel, message):
    """Post a message to the specified Slack channel."""
    try:
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

# Example usage
user_message = "Translate the following English text to French: 'Hello World'"
gpt_response = get_gpt_response(user_message)
post_message_to_slack('#general', gpt_response)


def get_gpt_response(prompt):
    """Get a response from GPT-3 based on the given prompt."""
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=150)
    return response.choices[0].text.strip()

def post_message_to_slack(channel, message):
    """Post a message to the specified Slack channel."""
    try:
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

# Example usage
user_message = "Translate the following English text to French: 'Hello World'"
gpt_response = get_gpt_response(user_message)
post_message_to_slack('#general', gpt_response)
