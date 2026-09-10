# ragathon.starter.kit - A ChunkRace, Pre-Installation Kit

*This repository is intentionally minimal. It sets up your environment ahead of
challenge day — it does not contain the challenge itself, the dataset, or any
hint about what you will be asked to build.*

## What this is for

ChunkRace is a 4-hour RAG (Retrieval-Augmented Generation) mini-challenge. To
make the best use of your time on the day itself, install and verify your
environment **now**, so you don't lose challenge time on setup.

## What you will need on challenge day (not provided here)

- The actual dataset and challenge instructions (distributed at kickoff)
- API keys for Groq and/or Gemini (distribution details will be shared at
  kickoff — free tier only, no paid tools required)

## Setup

Requirements: Python ≥ 3.14 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

This installs:

- `chromadb` — local vector store
- `groq` — Groq API client
- `google-genai` — Gemini API client
- `sentence-transformers` — embedding model library

You do not need to use both LLM providers — either Groq or Gemini will work
for the challenge. Both SDKs are installed so you can pick on the day.

## Pre-download the embedding model

To avoid depending on network access on challenge day, download and cache
the embedding model now:

```bash
uv run python download_embedding_model.py
```

This downloads ~470MB once. On challenge day, this step will be instant
since the model is already cached locally.

## Verify your setup

```bash
uv run python sanity_check.py
```

Expected output:

```
ChromaDB: OK
Groq SDK: OK
Gemini SDK: OK
sentence-transformers: OK

Environment ready. See you on challenge day.
```

If anything prints `MISSING`, re-run `uv sync` and check your Python version
(`python --version`, must be ≥ 3.14).

## What NOT to prepare in advance

There is deliberately no starter code, no dataset, and no architecture hints
in this repository. The actual challenge kit (code skeleton, dataset, and
detailed instructions) will be distributed at the start of the event. Trying
to guess the architecture in advance won't help — the goal is to solve the
challenge within the allotted time, starting from the same point as everyone
else.

---

# ChunkRace — Kit de pré-installation

*Ce dépôt est volontairement minimal. Il prépare ton environnement avant le
jour du défi — il ne contient ni le défi lui-même, ni le dataset, ni aucun
indice sur ce qui sera demandé.*

## À quoi ça sert

ChunkRace est un mini-défi RAG (Retrieval-Augmented Generation) de 4 heures.
Pour profiter au maximum de ton temps le jour J, installe et vérifie ton
environnement **maintenant**, pour ne pas perdre de temps de défi sur
l'installation.

## Ce dont tu auras besoin le jour J (non fourni ici)

- Le vrai dataset et les instructions du défi (distribués au kickoff)
- Des clés API Groq et/ou Gemini (modalités de distribution communiquées au
  kickoff — free tier uniquement, aucun outil payant requis)

## Installation

Prérequis : Python ≥ 3.14 et [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

Ceci installe :

- `chromadb` — vector store local
- `groq` — client API Groq
- `google-genai` — client API Gemini
- `sentence-transformers` — bibliothèque du modèle d'embedding

Tu n'as pas besoin des deux fournisseurs LLM — Groq ou Gemini suffira pour le
défi. Les deux SDK sont installés pour que tu puisses choisir le jour J.

## Pré-télécharger le modèle d'embedding

Pour éviter de dépendre du réseau le jour du défi, télécharge et mets en
cache le modèle d'embedding dès maintenant :

```bash
uv run python download_embedding_model.py
```

Ceci télécharge ~470 Mo une seule fois. Le jour J, cette étape sera
instantanée puisque le modèle sera déjà en cache localement.

## Vérifier ton installation

```bash
uv run python sanity_check.py
```

Sortie attendue :

```
ChromaDB: OK
Groq SDK: OK
Gemini SDK: OK
sentence-transformers: OK

Environment ready. See you on challenge day.
```

Si quelque chose affiche `MISSING`, relance `uv sync` et vérifie ta version de
Python (`python --version`, doit être ≥ 3.14).

## Ce qu'il ne faut PAS préparer à l'avance

Il n'y a volontairement aucun code de départ, aucun dataset, aucun indice
d'architecture dans ce dépôt. Le vrai kit du défi (squelette de code, dataset,
instructions détaillées) sera distribué au début de l'événement. Essayer de
deviner l'architecture à l'avance ne t'aidera pas — l'objectif est de résoudre
le défi dans le temps imparti, en partant du même point que tout le monde.
