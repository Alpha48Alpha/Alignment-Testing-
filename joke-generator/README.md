# 😄 Random Joke Generator

A lightweight Node.js/Express application that serves random jokes fetched from [JokeAPI](https://jokeapi.dev).

---

## Features

- **Random joke on every load** — a new joke is fetched automatically each time you open the page.
- **Category filtering** — choose between *Any*, *General*, *Programming*, or *Knock-Knock* jokes.
- **Fetch without reload** — click **New Joke** to get another joke via AJAX (no full page refresh).
- **Safe mode** — NSFW, political, racist, sexist, and explicit content is blocked at the API level.
- **JSON API endpoint** — `/api/joke?type=<category>` returns joke data as JSON for programmatic use.

---

## Project Structure

```
joke-generator/
├── server.js          # Express backend — proxies JokeAPI, exposes /api/joke
├── public/
│   ├── index.html     # Frontend UI (vanilla JS, no framework)
│   └── style.css      # Dark-theme styling
├── package.json       # Dependencies & npm scripts
└── README.md          # This file
```

---

## Setup

### Prerequisites

- [Node.js](https://nodejs.org/) v16 or later

### Install & Run

```bash
cd joke-generator
npm install
npm start
```

The server starts on **http://localhost:3000** (or the port set in the `PORT` environment variable).

---

## API Reference

### `GET /api/joke`

Returns a random joke as JSON.

#### Query Parameters

| Parameter | Values | Default | Description |
|-----------|--------|---------|-------------|
| `type`    | `any` \| `general` \| `programming` \| `knock-knock` | `any` | Joke category filter |

#### Response — Single joke

```json
{
  "type": "single",
  "joke": "Why do Java developers wear glasses? Because they don't C#."
}
```

#### Response — Two-part joke

```json
{
  "type": "twopart",
  "setup": "Why don't scientists trust atoms?",
  "delivery": "Because they make up everything!"
}
```

#### Error response

```json
{
  "error": "No joke found for the selected category."
}
```

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT`   | `3000`  | Port the Express server listens on |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Runtime | Node.js |
| Backend | Express.js |
| HTTP client | node-fetch |
| Jokes source | [JokeAPI v2](https://v2.jokeapi.dev) |
| Frontend | Vanilla HTML / CSS / JavaScript |
