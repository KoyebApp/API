```js
const api = new DiscardAPI({ apiKey: 'your-key' });

// Islamic
await api.quranSurah({ surah: 'yaseen' });
await api.prayerTiming({ city: 'Jakarta' });

// AI
await api.geminiPro({ text: 'What is AI?' });
await api.fluxSchnell({ text: 'Beautiful sunset' });

// Downloads
await api.dlTikTok({ url: 'https://...' });
await api.dlInstagram({ url: 'https://...' });

// URL Shorteners
await api.shortenClck({ url: 'https://github.com/...' });

// Jokes & Quotes
await api.dadJoke();
await api.randomQuote();

// Faker
await api.fakeUsers({ _quantity: 5, _locale: 'en_US', _gender: 'male', _seed: 1234 });

```
