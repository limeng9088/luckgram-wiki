# Help troubleshooting evidence — October 12, 2026

This public ledger backs the troubleshooting sections added on 2026-10-12 to
[App problems](../../help/app-problems.md), [Groups and channels](../../help/groups-and-channels.md)
and [Add and manage accounts](../../getting-started/accounts.md). Source links are pinned to the
revisions reviewed on October 10 (iOS `f42e2ad`, Android `235be7c`). A string in public source
shows what the client can display; it does not prove that a given installed release shows it.

| Page | Statement | Evidence |
|---|---|---|
| help/groups-and-channels.md | Writing restricted by admins, sometimes until a date | iOS strings:2812-2813 · Android strings:1531 · Android strings:1543 |
|  | Writing closed for everyone in the group | iOS strings:2814 |
|  | Slow mode: one message per interval, next-send time shown | iOS strings:4706-4707 · iOS strings:4713-4721 · Android strings:877 |
|  | Banned by an admin | iOS strings:1631 |
|  | Account limited: only mutual contacts / restricted from public groups; @SpamBot | iOS strings:1750 · iOS strings:3867 · [Telegram spam FAQ](https://telegram.org/faq_spam) · [Telegram FAQ: non-contacts](https://telegram.org/faq#can-39t-send-messages-to-non-contacts) |
|  | Telegram rules: another Telegram app shows the same restriction (restrictions kept per member) | [Telegram API: banned rights](https://core.telegram.org/api/rights) |
|  | Join limit per account; higher for Telegram Premium | [Telegram API: client configuration](https://core.telegram.org/api/config#channels-limit-default) (`channels_limit_default`, `channels_limit_premium`) · [channels.joinChannel `CHANNELS_TOO_MUCH`](https://core.telegram.org/method/channels.joinChannel) |
|  | Luckgram Premium is separate from Telegram Premium | [features/plans-and-rewards.md](../../features/plans-and-rewards.md) (“Luckgram Premium is separate from Telegram Premium”) |
|  | App asks to leave some before joining; iOS lists the most inactive chats | iOS strings:5179-5186 · Android strings:670 · Android strings:3941-3942 |
|  | Private group / expired invite link | iOS strings:1630 · iOS strings:6308 |
|  | Approval-only groups: added once an admin approves | iOS strings:7086-7094 · Android strings:5303 |
|  | Connecting… / Waiting for network status (also used on App problems) | iOS strings:315-320 · Android strings:181-182 |
| help/app-problems.md | Report with platform, versions, steps | [help/support-and-source.md § Reporting a problem](../../help/support-and-source.md) |
|  | Reinstall: login code via Telegram on another device or SMS; two-step password | [Telegram FAQ: getting a code via Telegram](https://telegram.org/faq#getting-a-code-via-telegram) · [Telegram FAQ: two-step verification](https://telegram.org/faq#q-how-does-2-step-verification-work) · iOS strings:426 |
|  | Cloud chats kept, secret chats lost on log-out; local data may not return | [Telegram FAQ: logging out](https://telegram.org/faq#q-how-do-i-log-out) · feature-not-visible.md at 4345c3b, lines 31-33 (now a link to this checklist) |
|  | Unsupported message/story prompts refer to one item | iOS strings:535 · iOS strings:3998-3999 · iOS strings:9595-9596 · Android strings:3901 · Android strings:6691 |
|  | Login “update to log in” comes from Telegram’s servers | iOS strings:9426 · Authorization.swift:254 (`UPDATE_APP_TO_LOGIN`) |
|  | iOS asks Telegram’s servers for an app update (every 12 hours) and shows the Luckgram Update screen | AppUpdate.swift:37-48 · ApplicationContext.swift:588-598 · iOS strings:3591-3594 · [help.getAppUpdate](https://core.telegram.org/method/help.getAppUpdate) |
|  | Update button opens App Store page; Skip unless required | UpdateInfoController.swift:117-118 · UpdateInfoController.swift:134 |
|  | Official download page and latest APK | [getting-started/install.md § Android](../../getting-started/install.md) |
|  | Notification checks: settings on, muted chats, system settings | [Telegram FAQ: notification problems](https://telegram.org/faq#notification-problems) |
|  | All Accounts: notifications from every account or only the active one | iOS strings:4258-4260 · NotificationsAndSoundsController.swift:534 · Android strings:2713-2715 |
|  | Power Saving: automatic below a battery level; autoplay, animations, effects | [Telegram: Power Saving](https://telegram.org/blog/power-saving) · iOS strings:9082-9092 · Android strings:6156 · Android strings:6256-6268 |
|  | Android Keep-Alive Service and Background Connection | Android strings:2497-2500 · NotificationsSettingsActivity.java:1021-1023 |
|  | Passcode Lock under Settings → Privacy and Security; Face ID/Touch ID/fingerprint unlock is an option of it | iOS strings:1227-1233 · iOS strings:3123 · iOS strings:3136-3137 · Android strings:3124 · Android strings:3147 · [Telegram FAQ: logging out](https://telegram.org/faq#q-how-do-i-log-out) |
|  | Forgot passcode: delete (uninstall) and reinstall; secret chats lost | iOS strings:3141-3142 · Android strings:3126 · Android strings:5525 |
|  | Wrong attempts make the app wait | iOS strings:1257-1263 |
|  | Two-step password is asked at sign-in | [Telegram FAQ: two-step verification](https://telegram.org/faq#q-how-does-2-step-verification-work) |
| getting-started/accounts.md | One account on many devices at once; cloud chats sync | [Telegram FAQ: devices](https://telegram.org/faq#q-which-devices-can-i-use) |
|  | Code may arrive in Telegram on another device | [Telegram FAQ: getting a code via Telegram](https://telegram.org/faq#getting-a-code-via-telegram) · iOS strings:426 |
|  | Devices / Active Sessions list | iOS strings:1469 · iOS strings:5122 · Android strings:2351 · Android strings:3020 |
|  | Sign-up: number with no account → after confirming, name, photo, terms, new account | [Telegram API: sign in / sign up](https://core.telegram.org/api/auth#sign-in-sign-up) · iOS strings:15064-15070 · iOS strings:3332 |
|  | Mobile numbers only, no landlines; registration problems → Telegram form | [Telegram FAQ: login and SMS](https://telegram.org/faq#login-and-sms) |
|  | Re-created too many times: wait a few days | iOS strings:2405 |

Fetched on 2026-10-12: telegram.org FAQ and spam FAQ, telegram.org/blog/power-saving,
core.telegram.org/api/config, /api/rights, /api/auth, /method/channels.joinChannel and
/method/help.getAppUpdate.

## Fix round (product tier review, 2026-10-12)

| Page | Statement | Evidence |
|---|---|---|
| help/app-problems.md | A reinstall means signing in to each account again, including Double Bottom accounts | [features/privacy.md § Double Bottom](../../features/privacy.md) (hidden accounts are signed-in Telegram accounts) · iOS strings:3141-3142 |
|  | Back up or export accounts first; menu Luckgram Settings → Accounts (iCloud Backup, Import from iCloud, Import from File, Export as File), all gated to iOS 15+ (NiceLocalizable.strings:237-242, LuckgramSettingsController.swift:616-618); Android import/export (label in a private module); a locked app cannot export; Import from iCloud only if iCloud Backup was on before | LuckgramSettingsController.swift:474-532 · AccountsExportHelper.kt · dataroom feature record `sessions-backup` (how_to) · [accounts.md § Back up, import, or export accounts](../../getting-started/accounts.md) |
|  | Bought or imported accounts may use a number you do not control; contact support before deleting; no sign-out as generic repair | [accounts.md § Telegram Sessions and Account Shop](../../getting-started/accounts.md) (“Do not delete sessions or sign out as a generic repair”) · scenario SCR-011 · [Account-shop announcement](https://t.me/luckgramapp/1015) |
|  | Didn’t get the code? → Get the code via SMS | iOS strings:427 · iOS strings:3874 |
|  | Forgotten two-step password: recovery email | [Telegram FAQ: two-step verification](https://telegram.org/faq#q-how-does-2-step-verification-work) |
|  | APK only for devices without Google Play | [getting-started/install.md:18-20](../../getting-started/install.md) (“When Google Play is unavailable …”) |
|  | The APK has the same package as the Play app, so Android may refuse to install it over the store version | Release 1.61.0 `app.apk`: `aapt2 dump badging` → `package: name='app.luckgram' versionCode='2259' versionName='1.61.0'` (checked 2026-10-12); Play listing id `app.luckgram`; [Android: app signing, App upgrade](https://developer.android.com/studio/publish/app-signing#considerations) |
|  | Same account in Telegram and Luckgram on one phone: two signed-in devices, both can notify | [Telegram FAQ: devices](https://telegram.org/faq#q-which-devices-can-i-use) · [Telegram FAQ: getting a code via Telegram](https://telegram.org/faq#getting-a-code-via-telegram) (“a different app on the same device”) |
|  | Power Usage is the Android label | Android strings:6156 · ProfileActivity.java:14033 |
| help/groups-and-channels.md | Not joined: the message field shows Join / Join Group | iOS strings:1626 · iOS strings:7648 · Android strings:522 |
| getting-started/accounts.md | Telegram may ask for an email address at sign-up | iOS strings:8117-8121 · [Telegram API: email verification](https://core.telegram.org/api/auth#email-verification) |
|  | On an account bought through Account Shop, contact support first if unsure before ending sessions (the shop owner confirms current client behaviour) | [accounts.md § Telegram Sessions and Account Shop](../../getting-started/accounts.md) · scenario SCR-011 |
| getting-started/availability.md | Former wallet and dApps: no longer offered on any platform | [features/wallet.md](../../features/wallet.md) · [docs/brand/facts.md](../brand/facts.md) (wallet financial functions retired) · [Wallet update](https://t.me/luckgramapp/1017) |

## Lost phone or SIM card (W4-P2, 2026-10-12)

Backs [I lost my phone or SIM card](../../getting-started/accounts.md#i-lost-my-phone-or-sim-card)
(dataroom gap GAP-03). Telegram FAQ fetched on 2026-10-12.

| Page | Statement | Evidence |
|---|---|---|
| getting-started/accounts.md | The phone number identifies the account; without the number or another signed-in device no one can restore it | [Telegram FAQ: my phone was stolen](https://telegram.org/faq#q-my-phone-was-stolen-what-do-i-do) (“the phone number is the only way for us to identify a Telegram user … we can't help you unless you have access either to the phone number or to Telegram itself on any of your devices”) · [support-and-source.md](../../help/support-and-source.md) (never share login codes or recovery material) |
|  | From another device: turn on Two-Step Verification in Settings → Privacy and Security, end the lost phone's session under Settings → Devices (or Active Sessions), have the operator block the SIM and reissue the number | [Telegram FAQ: I have access to Telegram on another device](https://telegram.org/faq#i-have-access-to-telegram-on-another-device) · iOS strings:953 · iOS strings:1367 · iOS strings:1469 · iOS strings:5122 · Android strings:3593 · Android strings:3425 · Android strings:2351 · Android strings:3020 |
|  | No other device: new SIM with the same number first, then sign in and end the old session | [Telegram FAQ: I don't have access to Telegram on any other devices](https://telegram.org/faq#i-don-39t-have-access-to-telegram-on-any-other-devices) |
|  | Code via Telegram on other devices; otherwise Didn't get the code? → SMS | [Telegram FAQ: getting a code via Telegram](https://telegram.org/faq#getting-a-code-via-telegram) · iOS strings:426-427 · iOS strings:3874 · Android strings:52-53 |
|  | Forgotten two-step password: the recovery email resets it | [Telegram FAQ: two-step verification](https://telegram.org/faq#q-how-does-2-step-verification-work) · iOS strings:3849 · iOS strings:6759 |
|  | Bought or imported accounts may use a number you do not control; support first | [accounts.md § Telegram Sessions and Account Shop](../../getting-started/accounts.md#telegram-sessions-and-account-shop) · scenario SCR-011 |
|  | Inactive accounts are deleted after the "If Away For" period in Privacy and Security | [Telegram FAQ: account self-destruction](https://telegram.org/faq#q-how-does-account-self-destruction-work) · iOS strings:981-983 · Android strings:3673 · Android strings:3679 |
|  | Change Number: Settings → tap your phone number → Change Number; keep a number you control | [Telegram FAQ: how do I change my phone number](https://telegram.org/faq#q-how-do-i-change-my-phone-number) · [Telegram FAQ: getting a code via Telegram](https://telegram.org/faq#getting-a-code-via-telegram) (warning) · iOS strings:1041-1045 · Android strings:2736 |
