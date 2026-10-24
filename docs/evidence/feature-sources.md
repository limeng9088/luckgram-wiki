# Public feature evidence

Verified on 2026-09-03. The public feature pages cite this ledger where a compact
source list is preferable to repeating implementation details.

## Product and distribution

- [Luckgram](https://luckgram.cc)
- [Features](https://luckgram.cc/features)
- [Download and availability](https://luckgram.cc/download)
- [FAQ](https://luckgram.cc/faq)
- [Privacy Policy](https://luckgram.cc/privacy-policy)
- [Terms of Use](https://luckgram.cc/terms-of-use)
- [iOS build (GitHub Releases)](https://github.com/limeng9088/luckgram-ios/releases/latest)
- [Android APK (GitHub Releases)](https://github.com/limeng9088/luckgram-android/releases/latest)

## Public source repositories

- [Luckgram for iOS](https://github.com/limeng9088/luckgram-ios)
- [Luckgram for Android](https://github.com/limeng9088/luckgram-android)
- Luckgram Desktop

## Pinned source receipts

| Capability | Receipt |
|---|---|
| iOS account ceiling | `AccountUtils.swift:7` |
| iOS Luckgram settings and account tools | `LuckgramSettingsController.swift:442` |
| iOS call recording | `CallRecorder.swift:40` |
| iOS local quick replies | `QuickRepliesController.swift:144` |
| iOS speech-to-text | `TgSpeechToTextManager.swift:35` |
| Android Luckgram settings | `LuckgramSettingsActivity.java:119` |
| Android account tools | `LuckgramSettingsActivity.java:260` |
| Android quick replies | `QuickRepliesHelper.kt:12` |
| Android voice tools | `VoiceTranscribeHelper.kt:12` |
| Android account-limit preferences | `LuckgramPrefs.kt:4` |
| Desktop AI/rich-message protocol surface | `api.tl:2198` |
| Desktop communities protocol surface | `api.tl:2704` |
| Desktop media text recognition | `media_view_recognition_selection.cpp:1` |

## Interpretation

- A public page labeled **Available** needs a current product or store source and
  a compatible client surface.
- **Beta** follows the official product label.
- **Limited rollout** means the surface exists but general release or parity is not
  established.
- **Source-visible** is evidence for maintainers, not a promise to users.
- Telegram-native behavior is not presented as a Luckgram-exclusive feature.


## Later review

The [October 10 product review](product-review-2026-10-10.md) supersedes
wallet availability, ATT earning, account-shop status and source-priority claims
in this September snapshot. Do not reuse the earlier claims as current guidance.
