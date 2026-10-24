# Product evidence review — October 10, 2026

This public ledger records implementation evidence, not a release certificate.
Source review precedes Wiki and website marketing. A public source hook proves
that a client integrates a surface; it does not prove that a service or an
installed version enables it. Private implementation details and team plans are
excluded from this ledger.

## Corrections

- Wallet financial functionality is retired: [public update](https://t.me/luckgramapp/1017). Historical sign-in is separate.
- [ATT update](https://t.me/luckgramapp/1011): old earning instructions are not a current reward promise.
- [Account shop](https://t.me/luckgramapp/1015) and [country selection](https://t.me/luckgramapp/1023) have public announcements; stock and entitlement still require a current check.
- HyperLancer: operator-approved holding statement on October 10 says work on a relaunch is underway. No date, escrow availability or payment guarantee is approved.

## Public implementation references

Every reference below is pinned to a source revision. “Source-visible” is the
maximum availability claim supported by code alone. Historical notes on the
older feature-sources page retain their original review date.

| Feature | Platforms inspected | Public implementation evidence | Availability boundary |
|---|---|---|---|
| Expanded accounts | iOS, Android | Luckgram-iOS:1 · Luckgram-Android:1 · Luckgram-Android:302 | Source-visible; matching installed release not verified |
| Account session backup/import/export | iOS, Android | Luckgram-iOS:474 · Luckgram-Android:1 | Source-visible; matching installed release not verified |
| Hidden chats | iOS, Android | Luckgram-Android:327 | Source-visible; matching installed release not verified |
| Double Bottom | iOS, Android | Luckgram-iOS:14 · Luckgram-iOS:1 · Luckgram-Android:1 | Source-visible; matching installed release not verified |
| Local quick replies | iOS, Android | Luckgram-iOS:1 · Luckgram-Android:1 | Source-visible; matching installed release not verified |
| Incoming translation | iOS, Android | Luckgram-iOS:1 · Luckgram-iOS:1 · Luckgram-Android:1 | Source-visible; matching installed release not verified |
| Outgoing translation | iOS, Android | Luckgram-iOS:1 · Luckgram-Android:1 | Source-visible; matching installed release not verified |
| Speech to text and cleanup | iOS, Android | Luckgram-iOS:561 · Luckgram-Android:1 | Source-visible; matching installed release not verified |
| AI assistant | iOS, Android | Luckgram-iOS:2236 | Source-visible; matching installed release not verified |
| AI chat analysis | iOS, Android | Luckgram-Android:1 | Source-visible; matching installed release not verified |
| AI shortcuts | iOS, Android | Luckgram-iOS:625 · Luckgram-Android:205 | Source-visible; matching installed release not verified |
| Keyword search/folders | iOS, Android | Luckgram-iOS:575 · Luckgram-Android:208 | Source-visible; matching installed release not verified |
| In-chat Luckgram menu | iOS, Android | Luckgram-iOS:625 · Luckgram-Android:205 | Source-visible; matching installed release not verified |
| Profile ID and registration estimate | iOS, Android | Luckgram-iOS:635 · Luckgram-Android:1 | Source-visible; matching installed release not verified |
| Phone-number display/privacy | iOS, Android | Luckgram-iOS:601 · Luckgram-Android:198 | Source-visible; matching installed release not verified |
| Profile links and extra actions | iOS, Android | Wiki:1 · Luckgram-Android:1 | Source-visible; matching installed release not verified |
| Forward as copy and message actions | iOS, Android | Luckgram-Android:1 · Wiki:1 · Luckgram-iOS:2271 | Source-visible; matching installed release not verified |
| Round video from local media | iOS, Android | Luckgram-iOS:1 · Luckgram-iOS:180 · Luckgram-Android:1 | Source-visible; matching installed release not verified |
| Camera and media preferences | iOS, Android | Luckgram-iOS:590 · Luckgram-Android:186 | Source-visible; matching installed release not verified |
| Call recording | iOS | Luckgram-iOS:1 · Luckgram-iOS:1 · Luckgram-iOS:407 | Source-visible; matching installed release not verified |
| Luckgram Calls | iOS | Luckgram-iOS:543 | Source-visible; matching installed release not verified |
| Contact sync and enrichment | iOS, Android, backend | Luckgram-Android:1 | Source-visible; matching installed release not verified |
| Tabs, folders, keyboard and app preferences | iOS, Android | Luckgram-iOS:551 · Luckgram-iOS:633 · Luckgram-Android:1 | Source-visible; matching installed release not verified |
| Immediate app lock | iOS | Luckgram-iOS:1 | Source-visible; matching installed release not verified |
| Local cache/media handling | iOS, Android | Wiki:1 · Luckgram-Android:1 | Source-visible; matching installed release not verified |
| Sensitive-content access | iOS, Android, backend | Luckgram-Android:237 | Source-visible; matching installed release not verified |
| Luckgram subscriptions and restore | iOS, Android, backend | Luckgram-Android:1 · Wiki:1 | Source-visible; matching installed release not verified |
| Ads and pinned placements | iOS, Android, backend | Luckgram-Android:1 | Source-visible; matching installed release not verified |
| Apps Center and NiceHub discovery | iOS, Android, backend | Wiki:1 | Source-visible; matching installed release not verified |
| Data-sharing preferences | iOS, Android | Luckgram-iOS:415 · Luckgram-Android:142 | Source-visible; matching installed release not verified |
| Desktop AI compose and tones | Desktop | luckgram-desktop:2695 | Source-visible; matching installed release not verified |
| Desktop rich messages | Desktop | luckgram-desktop:2188 | Source-visible; matching installed release not verified |
| Desktop communities | Desktop | luckgram-desktop:3070 | Source-visible; matching installed release not verified |
| Desktop ephemeral bot messages | Desktop | luckgram-desktop:3082 | Source-visible; matching installed release not verified |
| Desktop media text recognition | Desktop | luckgram-desktop:1 | Source-visible; matching installed release not verified |
| Telegram baseline features | iOS, Android, Desktop | Wiki:1 | Source-visible; matching installed release not verified |
| External beta/marketplace claims | unknown | Wiki:1 | Source-visible; matching installed release not verified |
| Select messages by author | iOS | Luckgram-iOS:2390 | Source-visible; matching installed release not verified |
| Message metadata and moderation shortcut | iOS | Luckgram-iOS:2322 | Source-visible; matching installed release not verified |

## How to use the review

Retirement corrections take precedence over old stores, marketing and source
left behind for compatibility. Check a user’s actual platform/version and offered
controls before giving an exact path. Do not infer prices, stock, service health,
unlimited usage or recovery guarantees from implementation alone.

Validation: `scripts/check-docs.sh` checks navigation and required documents.
It does not test app binaries or live services.
