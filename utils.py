# Standard library import
import logging

# Third-party imports
from twilio.rest import Client
from decouple import config


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = config("TWILIO_ACCOUNT_SID")
auth_token = config("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
twilio_number = config('TWILIO_NUMBER')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# def send_message(to_number, body_text):
#     try:

#         message = client.messages.create(
#             body=body_text,
#             from_=f'whatsapp:{twilio_number}',  # Use the Twilio WhatsApp number from your config
#             to='whatsapp:+13109546871'  # Use the dynamic number passed to the function
#         )
#         # message = client.messages.create(
#         #     from_=f"whatsapp:{twilio_number}",
#         #     body=body_text,
#         #     to=f"whatsapp:{to_number}"
#         #     )
#         # message = client.messages.create(
#         #                       body=body_text,
#         #                       from_='whatsapp:+14155238886',
#         #                       to='whatsapp:+13109546871'
#         #                   )
#         logger.info(f"Message sent to {to_number}: {message.body}")
#     except Exception as e:
#         logger.error(f"Error sending message to {to_number}: {e}")


def send_message(to_number, body_text):
    # Log the phone number to inspect its format before sending
    logger.info(f"Attempting to send message to: {to_number}")

    # Ensure `to_number` is in the correct format, e.g., '+13109546871'
    if not to_number.startswith('whatsapp:'):
        to_number = f'whatsapp:{to_number}'

    try:
        message = client.messages.create(
            body=body_text,
            from_=f'whatsapp:{twilio_number}',
            to=to_number
        )
        logger.info(f"Message sent to {to_number}: {message.body}")
    except Exception as e:
        logger.error(f"Error sending message to {to_number}: {e}")



# def send_message(to_number, body_text):
#     try:
#         message = client.messages.create(
#             from_=f"{twilio_number}",
#             body=body_text,
#             to=f"{to_number}"
#             )
#         logger.info(f"Message sent to {to_number}: {message.body}")
#     except Exception as e:
#         logger.error(f"Error sending message to {to_number}: {e}")