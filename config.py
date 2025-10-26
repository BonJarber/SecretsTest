# Configuration files - Using environment variables for secure credential management
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

'''Common Key Types with obvious names'''

# AWS
## AWS Access Key ID
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')

## AWS Secret Access Key
AWS_ACCESS_SECRET_KEY = os.getenv('AWS_ACCESS_SECRET_KEY', '')

## AWS MWS Auth Token
MWS_AUTH_TOKEN = os.getenv('MWS_AUTH_TOKEN', '')

# Google
## GCP Credentials
GCP_PRIVATE_KEY_ID = os.getenv('GCP_PRIVATE_KEY_ID', '')
GCP_PRIVATE_KEY = os.getenv('GCP_PRIVATE_KEY', '')

## Google API Key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '')

## Google Captcha
GOOGLE_CAPTCHA_KEY = os.getenv('GOOGLE_CAPTCHA_KEY', '')

# Github
## Github Personal Access Token
GITHUB_KEY = os.getenv('GITHUB_KEY', '')

## Github App
GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID', '')
GITHUB_APP_SECRET = os.getenv('GITHUB_APP_SECRET', '')

## Github OAuth App
GITHUB_OAUTH_CLIENT_ID = os.getenv('GITHUB_OAUTH_CLIENT_ID', '')
GITHUB_OAUTH_SECRET = os.getenv('GITHUB_OAUTH_SECRET', '')

# Slack
## Slack App
SLACK_CLIENT_ID = os.getenv('SLACK_CLIENT_ID', '')
SLACK_CLIENT_SECRET = os.getenv('SLACK_CLIENT_SECRET', '')

## Slack Signing Secret
SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET', '')

## Slack App token
SLACK_APP_TOKEN = os.getenv('SLACK_APP_TOKEN', '')

## Slack OAuth Access Token
SLACK_OAUTH_ACCESS_TOKEN = os.getenv('SLACK_OAUTH_ACCESS_TOKEN', '')

## Slack Webhook
SLACK_WEBHOOK = os.getenv('SLACK_WEBHOOK', '')

# Stripe
## Stripe Secret Key
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')

## Stripe Publishable Key
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', '')

## Stripe Restricted Key
STRIPE_RESTRICTED_KEY = os.getenv('STRIPE_RESTRICTED_KEY', '')

# Facebook
## Access Token
FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', '')

# Square
## Square Access Token
SQUARE_ACCESS_TOKEN = os.getenv('SQUARE_ACCESS_TOKEN', '')

## Square OAuth Secret
SQUARE_OAUTH_SECRET = os.getenv('SQUARE_OAUTH_SECRET', '')

# Paypal
## Braintree Access Token
PAYPAL_BRAINTREE_ACCESS_TOKEN = os.getenv('PAYPAL_BRAINTREE_ACCESS_TOKEN', '')

# Twilio
## Twilio API Key
TWILIO_API_KEY = os.getenv('TWILIO_API_KEY', '')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', '')
TWILIO_APP_SID = os.getenv('TWILIO_APP_SID', '')

# Mailgun
## Mailgun API Key
MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY', '')

# Okta
## Okta API Key
# TBD


'''Common Key Types with obscure names'''

# AWS
## AWS Access Key ID
VAR_1 = os.getenv('AWS_ACCESS_KEY_ID', '')

## AWS Secret Access Key
VAR_2 = os.getenv('AWS_ACCESS_SECRET_KEY', '')

## AWS MWS Auth Token
VAR_3 = os.getenv('MWS_AUTH_TOKEN', '')

# Google
## GCP Credentials
VAR_4 = os.getenv('GCP_PRIVATE_KEY_ID', '')
VAR_5 = os.getenv('GCP_PRIVATE_KEY', '')

## Google API Key
VAR_6 = os.getenv('GOOGLE_API_KEY', '')

## Google Captcha
VAR_7 = os.getenv('GOOGLE_CAPTCHA_KEY', '')

# Github
## Github Personal Access Token
VAR_8 = os.getenv('GITHUB_KEY', '')

## Github App
VAR_9 = os.getenv('GITHUB_CLIENT_ID', '')
VAR_10 = os.getenv('GITHUB_APP_SECRET', '')

## Github OAuth App
VAR_11 = os.getenv('GITHUB_OAUTH_CLIENT_ID', '')
VAR_12 = os.getenv('GITHUB_OAUTH_SECRET', '')

# Slack
## Slack App
VAR_13 = os.getenv('SLACK_CLIENT_ID', '')
VAR_14 = os.getenv('SLACK_CLIENT_SECRET', '')

## Slack Signing Secret
VAR_15 = os.getenv('SLACK_SIGNING_SECRET', '')

## Slack App token
VAR_16 = os.getenv('SLACK_APP_TOKEN', '')

## Slack OAuth Access Token
VAR_17 = os.getenv('SLACK_OAUTH_ACCESS_TOKEN', '')

## Slack Webhook
VAR_18 = os.getenv('SLACK_WEBHOOK', '')

# Stripe
## Stripe Secret Key
VAR_19 = os.getenv('STRIPE_SECRET_KEY', '')

## Stripe Publishable Key
VAR_20 = os.getenv('STRIPE_PUBLISHABLE_KEY', '')

## Stripe Restricted Key
VAR_21 = os.getenv('STRIPE_RESTRICTED_KEY', '')

# Facebook
## Access Token
VAR_22 = os.getenv('FACEBOOK_ACCESS_TOKEN', '')

# Square
## Square Access Token
VAR_23 = os.getenv('SQUARE_ACCESS_TOKEN', '')

## Square OAuth Secret
VAR_24 = os.getenv('SQUARE_OAUTH_SECRET', '')

# Paypal
## Braintree Access Token
VAR_25 = os.getenv('PAYPAL_BRAINTREE_ACCESS_TOKEN', '')

# Twilio
## Twilio API Key
VAR_26 = os.getenv('TWILIO_API_KEY', '')
VAR_27 = os.getenv('TWILIO_ACCOUNT_SID', '')
VAR_28 = os.getenv('TWILIO_APP_SID', '')

# Mailgun
## Mailgun API Key
VAR_29 = os.getenv('MAILGUN_API_KEY', '')

'''Generic Credentials with obvious names'''

# Generic db password
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '')

# Generic weak redis password
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')

# Generic weak postgres password
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')

# Generic weak password
PASSWORD = os.getenv('PASSWORD', '')

# Generic application secret
APP_SECRET = os.getenv('APP_SECRET', '')

# Generic api key
API_KEY = os.getenv('API_KEY', '')

# Generic api key
APIKEY = os.getenv('APIKEY', '')

# Generic api key
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', '')

'''Generic Credentials with obscure names that flow into password sinks'''

# Generic password
SOURCE_1 = os.getenv('SOURCE_1', '')

# Generic weak password
SOURCE_2 = os.getenv('SOURCE_2', '')

# Generic weak password
SOURCE_3 = os.getenv('SOURCE_3', '')

# Generic app secret
SOURCE_4 = os.getenv('SOURCE_4', '')

# Generic api key
SOURCE_5 = os.getenv('SOURCE_5', '')

# Generic api key
SOURCE_6 = os.getenv('SOURCE_6', '')

# Generic api key
SOURCE_7 = os.getenv('SOURCE_7', '')


'''False Positives'''

# Github Hashes

## Obvious name
GITHUB_COMMIT_SHA_HASH = '120ba2f7db8affd023e83964e5d8afbd10d20fe8'

## Less obvious name
COMMIT_SHA = '637831c685a5f906c65d6af8389e7988619a3514'

## Obscure name
LATEST = '699865bd61fda628b0bea3080ae73d5f11572a74'

# Public Keys

## SSH RSA public key
PUBLIC_KEY_SSH = 'AAAAB3NzaC1yc2EAAAADAQABAAAAgQCqGKukO1De7zhZj6+H0qtjTkVxwTCpvKe4eCZ0FPqri0cb2JZfXJ/DgYSF6vUpwmJG8wVQZKjeGcjDOL5UlsuusFncCzWBQ7RKNUSesmQRMSGkVb1/3j+skZ6UtW+5u09lHNsj6tQ51s1SPrCBkedbNf0Tp0GbMJDyR4e9T04ZZw=='

## Public key file
PUBLIC_KEY_FILE = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCqGKukO1De7zhZj6+H0qtjTkVxwTCpvKe4eCZ0\nFPqri0cb2JZfXJ/DgYSF6vUpwmJG8wVQZKjeGcjDOL5UlsuusFncCzWBQ7RKNUSesmQRMSGkVb1/\n3j+skZ6UtW+5u09lHNsj6tQ51s1SPrCBkedbNf0Tp0GbMJDyR4e9T04ZZwIDAQAB\n-----END PUBLIC KEY-----'
