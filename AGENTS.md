# hamlet

A chatbot that answers in Shakespeare quotes, live at <https://hamlet.42labs.io>. Flask and jQuery
over a pre-LLM information-retrieval pipeline: TF-IDF cosine similarity across a pre-computed
corpus index, Porter stemming, WordNet synonym expansion, and TextBlob sentiment as a tiebreaker.
It returns a quote and its source.

**Stage: unmaintained, and staying online.** Built in 2016 and kept running as an artifact of how
this was done before LLMs. Nothing here is being developed; issues and pull requests may sit
indefinitely. The site working is the entire point of leaving it up. Do not scope feature work
here without the operator asking for it.

**Dual-licensed** — AGPL-3.0 open source, commercial on request (`LICENSING.md`). It was published
under MIT until 2026; the README is the user documentation.

## How work flows

Branch, work from a worktree under `.worktrees/`, open a PR against `main`. The LGTM gate and a
Vercel preview deploy run on every PR. The `.claude/` CLU guards enforce worktree-only writes and
refuse a self-merge, but only while a CLU run is active. `main` is not branch-protected, so the
gate is advisory.

## Crew

The roles this project is worked by, and what each one needs. **No personas live here** — an agent
arrives already knowing who it is, and reads this project to learn the project.

| Role | What this project needs from it |
|------|---------------------------------|
| Engineering | Only what keeps the deploy alive — a dependency that breaks the build, nothing more |
| Sysadmin | The Vercel deployment, the `hamlet.42labs.io` domain, branch protection and the gate |

No architect, reviewer, content or data role is in use: nothing new is scoped here by design.

**After any context loss, re-read your anchor under `~/.agent-anchors/hamlet/`** (canon §17). None
exists yet.

## Key files

- `README.md` — what it is, how the retrieval pipeline works, how to run it locally
- `app.py` — the Flask server and the whole pipeline
- `shakespeare.json` — the corpus
- `data/` — the vendored NLTK/WordNet corpus. `app.py` puts it on `nltk.data.path`, and `vercel.json` ships it via `includeFiles` — deploy-critical, not a scratch directory
- `templates/`, `static/` — the front end
- `requirements.txt` — pinned dependencies
- `vercel.json` — the deploy configuration
- `MEMO-CODEX-URGENT.md` — untracked. Its gate item is done; branch protection is still open
