<p align="Left">
  <p align="Left">
    <a href="https://github.com/borischen0203/lowerPriceNotifier/actions/workflows/cicd.yaml"><img alt="GitHub release" src="https://github.com/borischen0203/lowerPriceNotifier/actions/workflows/cicd.yaml/badge.svg?logo=github&style=flat-square"></a>
  </p>
</p>

# lowerPriceNotifier

A crawler project that checks the price on the e-commerce platform and notifies the client if the product price is lower than expected.

# How to use

Sample URLs for input

## API Endpoints

### Health Check

- **URL:** `/health`
- **Method:** `GET`
- **Description:** Checks the health of the API.
- **Example:**

```bash
curl -X GET https://lower-price-notifier.vercel.app/health
```

### Notify

- **URL:** `/notify`
- **Method:** `POST`
- **Description:** Sends a notification to the Slack channel.
- **Request Body**: JSON object with a text field.
- **Example:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text":"Hello, Slack!"}' https://lower-price-notifier.vercel.app/notify
```

## Run in Local:

## Required

-
-

### Run process

TODO

## Tech stack

- Python
- Flask
- Vercel
- make
- Github actions
