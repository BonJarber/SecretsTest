# Security Policy

## Security Improvements Made

This repository has been updated to address critical security vulnerabilities:

### 1. Hardcoded Secrets Removed
- **Issue**: API keys, passwords, and other sensitive credentials were hardcoded in source code
- **Fix**: All hardcoded secrets have been replaced with environment variables using `python-dotenv`
- **Files Modified**: 
  - `config.py` - All hardcoded credentials replaced with `os.getenv()` calls
  - `main.py` - All hardcoded API keys and passwords replaced with environment variables

### 2. Debug Mode Disabled
- **Issue**: Flask application was running with `debug=True` in production
- **Fix**: Debug mode is now controlled via `FLASK_DEBUG` environment variable and defaults to `False`
- **File Modified**: `main.py`

### 3. Configuration Management
- **New Files**:
  - `.env.example` - Template for environment variables
  - `.gitignore` - Ensures `.env` files are not committed to version control
  - `SECURITY.md` - This file documenting security improvements

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your actual credentials (NEVER commit this file!)
nano .env
```

### 3. Run the Application
```bash
python main.py
```

## Environment Variables Required

The following environment variables must be configured in your `.env` file:

### AWS Configuration
- `AWS_ACCESS_KEY_ID`
- `AWS_ACCESS_SECRET_KEY`
- `MWS_AUTH_TOKEN`

### Google Configuration
- `GCP_PRIVATE_KEY_ID`
- `GCP_PRIVATE_KEY`
- `GOOGLE_API_KEY`
- `GOOGLE_CAPTCHA_KEY`

### GitHub Configuration
- `GITHUB_KEY`
- `GITHUB_CLIENT_ID`
- `GITHUB_APP_SECRET`
- `GITHUB_OAUTH_CLIENT_ID`
- `GITHUB_OAUTH_SECRET`

### Slack Configuration
- `SLACK_CLIENT_ID`
- `SLACK_CLIENT_SECRET`
- `SLACK_SIGNING_SECRET`
- `SLACK_APP_TOKEN`
- `SLACK_OAUTH_ACCESS_TOKEN`
- `SLACK_WEBHOOK`

### Stripe Configuration
- `STRIPE_SECRET_KEY`
- `STRIPE_PUBLISHABLE_KEY`
- `STRIPE_RESTRICTED_KEY`

### Facebook Configuration
- `FACEBOOK_ACCESS_TOKEN`

### Square Configuration
- `SQUARE_ACCESS_TOKEN`
- `SQUARE_OAUTH_SECRET`

### PayPal Configuration
- `PAYPAL_BRAINTREE_ACCESS_TOKEN`

### Twilio Configuration
- `TWILIO_API_KEY`
- `TWILIO_ACCOUNT_SID`
- `TWILIO_APP_SID`

### Mailgun Configuration
- `MAILGUN_API_KEY`

### Database Configuration
- `DATABASE_PASSWORD`
- `REDIS_PASSWORD`
- `POSTGRES_PASSWORD`

### Application Configuration
- `PASSWORD`
- `APP_SECRET`
- `API_KEY`
- `APIKEY`
- `ACCESS_TOKEN`
- `FLASK_SECRET_KEY`
- `FLASK_DEBUG` (set to `False` in production)

### Generic Secrets
- `SOURCE_1` through `SOURCE_7`

## Security Best Practices

1. **Never commit `.env` files** - They contain sensitive credentials
2. **Rotate credentials regularly** - Change API keys and passwords periodically
3. **Use strong, unique passwords** - Avoid weak passwords like "password" or "admin"
4. **Keep dependencies updated** - Regularly update Python packages for security patches
5. **Disable debug mode in production** - Always set `FLASK_DEBUG=False`
6. **Use HTTPS** - Always use encrypted connections for API requests
7. **Implement proper authentication** - Use secure authentication mechanisms
8. **Apply principle of least privilege** - Grant only necessary permissions

## Reporting Security Issues

If you discover a security vulnerability, please report it to the repository maintainers immediately. Do not create public issues for security vulnerabilities.

## Compliance

This security fix addresses the following vulnerability types:
- CWE-798: Use of Hard-coded Credentials
- CWE-489: Active Debug Code
- CWE-200: Exposure of Sensitive Information

## Version History

- **v2.0** (2025-10-26): Security hardening - Removed all hardcoded secrets, disabled debug mode
- **v1.0** (original): Initial version with hardcoded credentials (vulnerable)
