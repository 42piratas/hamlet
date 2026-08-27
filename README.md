# hamlet

[![Project Status: Inactive](https://www.repostatus.org/badges/latest/inactive.svg)](https://www.repostatus.org/#inactive)

> Polonius: What do you read, my lord?
> Hamlet: Words, words, words.

A chatbot that answers in Shakespeare quotes. Live at **<https://hamlet.42labs.io>**.

> [!NOTE]
> **Unmaintained, and staying online.** Built in 2016, kept running as an artifact of
> how this was done before LLMs. Nothing here is being developed; issues and pull
> requests may sit indefinitely. The site works — that is the whole point of leaving
> it up.

## How it works

Flask + jQuery front end. The server picks an apt quote from `shakespeare.json` with a pre-LLM IR pipeline: [TF–IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) cosine similarity over a pre-computed corpus index, [Porter stemming](https://tartarus.org/martin/PorterStemmer/), [WordNet](https://wordnet.princeton.edu/) synonym expansion (NLTK), and [TextBlob](https://textblob.readthedocs.io/en/dev/) sentiment as a tiebreaker. Returns `{quote, source}`.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run --port 5001
```

## License

Open source — [AGPL-3.0](LICENSE). Commercial — contact ahoy@42labs.io.

---
If it earned its keep, [coffee is appreciated](https://buymeacoffee.com/42piratas). ☕
