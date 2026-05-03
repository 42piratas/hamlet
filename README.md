# Hamlet

> Polonius: What do you read, my lord?
> Hamlet: Words, words, words.

A chatbot that answers in Shakespeare quotes. Live at **<https://hamlet.42labs.io>**.

### How it works

Flask + jQuery front end; the server picks an apt quote from `shakespeare.json` using [TextBlob](https://textblob.readthedocs.io/en/dev/) sentiment + a hand-rolled tokenizer, then returns `{quote, source}`. Built in 2016, kept online as an artifact of the pre-LLM era.

### UI

- IM-style speech bubbles: user on the right with a person avatar, Hamlet on the left with the Yorick-skull glyph.
- Header with brand mark + an info button that re-opens the welcome modal.
- Welcome modal (`Hark!`) shown once per browser via `localStorage`.
- 42labs footer (`© 2026 42LABS`).

### Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run --port 5001
```

### Deploy

Hosted on Vercel (`@vercel/python` builder, `vercel.json` rewrites all routes to `app.py`). Deploy the current branch with `vercel --prod`.
