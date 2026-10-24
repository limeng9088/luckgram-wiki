# Public feature evidence

Verified on 2026-09-03. The public feature pages cite this ledger where a compact
source list is preferable to repeating implementation details.

## Product and distribution

- [Luckgram](https://luckgram.me)
- [Features](https://luckgram.me/features)
- [Download and availability](https://luckgram.me/download)
- [FAQ](https://luckgram.me/faq)
- [Privacy Policy](https://luckgram.me/privacy-policy)
- [Terms of Use](https://luckgram.me/terms-of-use)
- [Apple App Store](https://apps.apple.com/app/id1608870673)
- [Google Play](https://play.google.com/store/apps/details?id=app.luckgram)

## Public source repositories

- [Luckgram for iOS](https://github.com/luckgram/Luckgram-iOS)
- [Luckgram for Android](https://github.com/luckgram/Luckgram-Android)
- [Luckgram Desktop](https://github.com/luckgram/luckgram-desktop)

## Pinned source receipts

| Capability | Receipt |
|---|---|
| iOS account ceiling | [`AccountUtils.swift:7`](https://github.com/luckgram/Luckgram-iOS/blob/47c59dac6fc6b93b741fbc197c1f79524bfbf65c/submodules/AccountUtils/Sources/AccountUtils.swift#L7) |
| iOS Luckgram settings and account tools | [`LuckgramSettingsController.swift:442`](https://github.com/luckgram/Luckgram-iOS/blob/47c59dac6fc6b93b741fbc197c1f79524bfbf65c/Luckgram/NGUI/Sources/LuckgramSettingsController.swift#L442) |
| iOS call recording | [`CallRecorder.swift:40`](https://github.com/luckgram/Luckgram-iOS/blob/47c59dac6fc6b93b741fbc197c1f79524bfbf65c/Luckgram/NGCallRecorder/Sources/CallRecorder.swift#L40) |
| iOS local quick replies | [`QuickRepliesController.swift:144`](https://github.com/luckgram/Luckgram-iOS/blob/47c59dac6fc6b93b741fbc197c1f79524bfbf65c/Luckgram/NGQuickReplies/Sources/Presentation/QuickRepliesController.swift#L144) |
| iOS speech-to-text | [`TgSpeechToTextManager.swift:35`](https://github.com/luckgram/Luckgram-iOS/blob/47c59dac6fc6b93b741fbc197c1f79524bfbf65c/Luckgram/NGSpeechToText/Sources/TgSpeechToTextManager.swift#L35) |
| Android Luckgram settings | [`LuckgramSettingsActivity.java:119`](https://github.com/luckgram/Luckgram-Android/blob/76f9b4022e2e3c0108d9722a63aef8f35974b556/TMessagesProj/src/main/java/app/luckgram/LuckgramSettingsActivity.java#L119) |
| Android account tools | [`LuckgramSettingsActivity.java:260`](https://github.com/luckgram/Luckgram-Android/blob/76f9b4022e2e3c0108d9722a63aef8f35974b556/TMessagesProj/src/main/java/app/luckgram/LuckgramSettingsActivity.java#L260) |
| Android quick replies | [`QuickRepliesHelper.kt:12`](https://github.com/luckgram/Luckgram-Android/blob/76f9b4022e2e3c0108d9722a63aef8f35974b556/TMessagesProj/src/main/java/app/luckgram/QuickRepliesHelper.kt#L12) |
| Android voice tools | [`VoiceTranscribeHelper.kt:12`](https://github.com/luckgram/Luckgram-Android/blob/76f9b4022e2e3c0108d9722a63aef8f35974b556/TMessagesProj/src/main/java/app/luckgram/VoiceTranscribeHelper.kt#L12) |
| Android account-limit preferences | [`LuckgramPrefs.kt:4`](https://github.com/luckgram/Luckgram-Android/blob/76f9b4022e2e3c0108d9722a63aef8f35974b556/luckgram-features/src/main/java/com/appvillis/luckgram/LuckgramPrefs.kt#L4) |
| Desktop AI/rich-message protocol surface | [`api.tl:2198`](https://github.com/luckgram/luckgram-desktop/blob/4e5f92b2d007df2a09f8dea77dec6a1077bc7be3/Telegram/SourceFiles/mtproto/scheme/api.tl#L2198) |
| Desktop communities protocol surface | [`api.tl:2704`](https://github.com/luckgram/luckgram-desktop/blob/4e5f92b2d007df2a09f8dea77dec6a1077bc7be3/Telegram/SourceFiles/mtproto/scheme/api.tl#L2704) |
| Desktop media text recognition | [`media_view_recognition_selection.cpp:1`](https://github.com/luckgram/luckgram-desktop/blob/4e5f92b2d007df2a09f8dea77dec6a1077bc7be3/Telegram/SourceFiles/media/view/media_view_recognition_selection.cpp#L1) |

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
