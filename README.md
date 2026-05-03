# Hamlet

> Polonius: What do you read, my lord?
> Hamlet: Words, words, words.

A chatbot that answers in Shakespeare quotes. Live at **<https://hamlet.42labs.io>**.

### How it works

Flask + jQuery front end. The server picks an apt quote from `shakespeare.json` with a pre-LLM IR pipeline: [TF–IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) cosine similarity over a pre-computed corpus index, [Porter stemming](https://tartarus.org/martin/PorterStemmer/), [WordNet](https://wordnet.princeton.edu/) synonym expansion (NLTK), and [TextBlob](https://textblob.readthedocs.io/en/dev/) sentiment as a tiebreaker. Returns `{quote, source}`. Built in 2016, kept online as an artifact of the pre-LLM era.

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
