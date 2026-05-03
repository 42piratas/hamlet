# Hamlet

> Polonius: What do you read, my lord?
> Hamlet: Words, words, words.

A chatbot that answers in Shakespeare quotes. Live at **<https://hamlet.42labs.io>**.

### How it works

Flask + jQuery front end; the server picks an apt quote from `shakespeare.json` using [NLTK](https://www.nltk.org) and [TextBlob](https://textblob.readthedocs.io/en/dev/) sentiment + tokenization, then returns `{quote, source}`.

### Design

Forced dark theme, terminal-style chat, centered 760px column. Tokens, fonts, spacing follow the [42labs design system](https://42labs.io/design). See `static/css/style.css`.

### Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run --port 5001
```

### Deploy

Hosted on Vercel (`@vercel/python` builder, `vercel.json` rewrites all routes to `app.py`). Deploy the current branch with `vercel --prod`.
