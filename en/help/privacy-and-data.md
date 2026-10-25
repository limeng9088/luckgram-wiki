---
description: Understand which parts of Luckgram use Telegram, local device storage, Luckgram services, or third-party providers.
---

# How does data flow when I use Luckgram?

Different Luckgram actions use different systems. The safest useful explanation is
to identify the feature path, not to make one blanket privacy claim.

| Action | Main data path |
|---|---|
| Telegram chats, channels, account login, and ordinary calls | Telegram services and the client on your device |
| Hidden-chat state, preferences, cache, downloads, and some quick replies | Primarily the local app/device, with implementation differences |
| Luckgram account services, subscriptions, referrals, remote configuration, and feature eligibility | Luckgram services and relevant store/provider |
| AI prompts, selected chat context, translation, or transcription | Luckgram and/or the selected processing provider, depending on the feature |
| Historical wallet-linked access | Separate from the retired financial wallet; ask support about a specific old setup |
| Analytics, diagnostics, attribution, and website cookies | Luckgram and the providers disclosed by the current policy or store |

Luckgram’s current policy describes collection and processing needed for services,
usage analysis, device information, contacts or location when the relevant
permission or Telegram feature is used, and information you choose to provide. The
Apple and Google store disclosures should also be reviewed before installation.

The retired claim “we do not collect any personal data” is not used in this Help
Center because it is incompatible with those disclosures.

## Safer use

- Review operating-system permissions and disable ones you do not use.
- Check the context selected before sending an AI request.
- Keep login codes, two-step passwords, exported sessions, and wallet recovery
  material out of chats and support tickets.
- Remember that hiding a chat changes the local interface; it does not remove the
  conversation from another signed-in device.
- Read the current policy for legal definitions, retention, processors, and rights.

**Authoritative sources:** [Luckgram Privacy Policy](https://luckgram.cc/en/privacy-policy) ·
[Telegram Privacy Policy](https://telegram.org/privacy) ·
[iOS build (GitHub Releases)](https://github.com/limeng9088/luckgram-ios/releases/latest) ·
[Android APK (GitHub Releases)](https://github.com/limeng9088/luckgram-android/releases/latest)
