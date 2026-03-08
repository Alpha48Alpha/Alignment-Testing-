const express = require('express');
const fetch = require('node-fetch');
const path = require('path');
const rateLimit = require('express-rate-limit');

const app = express();
const PORT = process.env.PORT || 3000;

// Apply rate limiting to all routes (max 100 requests per minute per IP)
const limiter = rateLimit({
  windowMs: 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false
});
app.use(limiter);

// Category mapping from UI labels to JokeAPI categories.
// 'knock-knock' is not a JokeAPI category, so those jokes are served
// entirely from the local fallback set.
const CATEGORY_MAP = {
  general: 'Misc',
  programming: 'Programming',
  any: 'Any'
};

// Fallback jokes used when the external API is unreachable
const FALLBACK_JOKES = {
  general: [
    { type: 'twopart', setup: 'Why don\'t scientists trust atoms?', delivery: 'Because they make up everything!' },
    { type: 'twopart', setup: 'What do you call a fish without eyes?', delivery: 'A fsh!' },
    { type: 'single',  joke: 'I told my wife she was drawing her eyebrows too high. She looked surprised.' },
    { type: 'twopart', setup: 'Why can\'t you give Elsa a balloon?', delivery: 'Because she\'ll let it go!' },
    { type: 'single',  joke: 'I used to hate facial hair, but then it grew on me.' }
  ],
  programming: [
    { type: 'twopart', setup: 'Why do programmers prefer dark mode?', delivery: 'Because light attracts bugs!' },
    { type: 'twopart', setup: 'How many programmers does it take to change a light bulb?', delivery: 'None — that\'s a hardware problem.' },
    { type: 'single',  joke: 'A SQL query walks into a bar, walks up to two tables and asks: "Can I join you?"' },
    { type: 'twopart', setup: 'Why do Java developers wear glasses?', delivery: 'Because they don\'t C#!' },
    { type: 'single',  joke: 'There are only 10 types of people: those who understand binary and those who don\'t.' }
  ],
  'knock-knock': [
    { type: 'twopart', setup: 'Knock knock. Who\'s there? Lettuce.', delivery: 'Lettuce in — it\'s cold out here!' },
    { type: 'twopart', setup: 'Knock knock. Who\'s there? Interrupting cow.', delivery: 'Interrupting cow wh— MOO!' },
    { type: 'twopart', setup: 'Knock knock. Who\'s there? Nobel.', delivery: 'Nobel, that\'s why I knocked!' },
    { type: 'twopart', setup: 'Knock knock. Who\'s there? Atch.', delivery: 'Atch who? Bless you!' },
    { type: 'twopart', setup: 'Knock knock. Who\'s there? Tank.', delivery: 'Tank who? You\'re welcome!' }
  ]
};

function getRandomFallback(typeParam) {
  const key = FALLBACK_JOKES[typeParam] ? typeParam : null;
  const pool = key
    ? FALLBACK_JOKES[key]
    : [].concat(...Object.values(FALLBACK_JOKES));
  return pool[Math.floor(Math.random() * pool.length)];
}

app.use(express.static(path.join(__dirname, 'public')));

/**
 * GET /api/joke
 * Query params:
 *   type  - one of: general | programming | knock-knock | any (default: any)
 *
 * Returns JSON:
 *   { type: "single"|"twopart", joke?, setup?, delivery?, source? }
 */
app.get('/api/joke', async (req, res) => {
  const typeParam = (req.query.type || 'any').toLowerCase();

  // knock-knock jokes are served exclusively from the local set
  if (typeParam === 'knock-knock') {
    return res.json({ ...getRandomFallback('knock-knock'), source: 'local' });
  }

  const category = CATEGORY_MAP[typeParam] || 'Any';

  const apiUrl =
    `https://v2.jokeapi.dev/joke/${category}` +
    `?safe-mode` +
    `&blacklistFlags=nsfw,religious,political,racist,sexist,explicit`;

  try {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 5000);
    let response;
    try {
      response = await fetch(apiUrl, { signal: controller.signal });
    } finally {
      clearTimeout(timer);
    }
    if (!response.ok) {
      const fallback = getRandomFallback(typeParam);
      return res.json({ ...fallback, source: 'local' });
    }
    const data = await response.json();

    if (data.error) {
      const fallback = getRandomFallback(typeParam);
      return res.json({ ...fallback, source: 'local' });
    }

    if (data.type === 'single') {
      return res.json({ type: 'single', joke: data.joke, source: 'jokeapi' });
    }
    return res.json({
      type: 'twopart',
      setup: data.setup,
      delivery: data.delivery,
      source: 'jokeapi'
    });
  } catch (err) {
    // External API unreachable — serve a local fallback
    const fallback = getRandomFallback(typeParam);
    return res.json({ ...fallback, source: 'local' });
  }
});

// Serve the frontend for every other route
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Joke Generator running at http://localhost:${PORT}`);
});
