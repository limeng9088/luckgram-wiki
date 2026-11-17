---
description: Open the Luckgram web app in a browser, install it as a desktop app, see how it differs from the mobile apps, and choose how it connects.
---

# How do I use the Luckgram web app?

The Luckgram web app runs in the browser, with nothing to download. It uses the same Telegram
account: once you sign in, your chats, channels, groups and files are there.

## Open the web app {#open}

1. Open [web.luckgram.cc](https://web.luckgram.cc) in a browser on a computer or phone. A recent
   Chrome, Edge or Safari is recommended.
2. Sign in one of two ways:
   - **QR code:** in Telegram or Luckgram on a phone that is already signed in, open
     **Settings → Devices → Link Desktop Device** and scan the code on the page.
   - **Phone number:** choose **Log in by phone number**, then enter your number and the code.
3. If the account has two-step verification, enter that password too.

**Where does the code arrive?** When the number is already signed in on another device, Telegram
does not send an SMS. It sends the code to the Telegram app that is signed in, in the official chat
named **Telegram**. An SMS is sent only when the number is not signed in anywhere.

## Install it as a desktop app {#install}

The web app can be installed as an app with its own window and icon, without the browser's
address bar.

| Browser | How |
|---|---|
| Chrome, Edge (computer) | The **Install** icon at the right of the address bar, or **Install Luckgram** in the menu |
| Safari (Mac) | **File → Add to Dock** in the menu bar |
| Chrome (Android) | Menu **⋮ → Add to Home screen** |
| Safari (iPhone, iPad) | **Share → Add to Home Screen** |

The installed app and the web app in the browser share one sign-in. Uninstalling the app does not
sign you out; to sign out, use **Settings**.

## How it differs from the mobile apps {#differences}

The web app is based on Telegram's web app, so Telegram's own chats, channels, groups, calls and
file transfers work the same way. Of the features Luckgram adds, the web app has the ones below.
They are used a little differently: mostly, where the phone has a long press, the web app has a
**right-click**.

| Feature | How it is used in the web app, and what differs |
|---|---|
| [More accounts](../features/privacy.md#accounts) | Up to 20, no Luckgram Pro needed (the mobile apps: 10 free, unlimited with Luckgram Pro) |
| [Translate messages](../features/translation-and-voice.md#translate-in) | Right-click a message and choose Translate, or click the translate icon beside a message in another language. The target language is set in Settings → Luckgram Features. |
| [Voice to text, dictation](../features/translation-and-voice.md#voice-text) | Click the transcribe button on a voice message or a round video. Accounts without Telegram Premium are transcribed by Luckgram for free; Premium accounts use Telegram’s own transcription. A voice message over 3 minutes is transcribed in parts and takes longer. To dictate, click Dictation beside the emoji button and click it again when you are done: the text is put into the message field once you finish, not as you speak. Chrome or Edge on a computer is recommended; Safari and mobile browsers have not been tested yet. |
| [Translate before sending](../features/translation-and-voice.md#translate-out) | Click the translate button beside the message field, or right-click the send button and choose Translate or Translate to…; in a narrow window it is in the ✦ menu. |
| [AI writing](../features/ai.md#ai-writing) | Click the ✦ button beside the message field and pick an effect. Up to 4,000 characters at a time; Undo brings your own text back. |
| [Reply drafts](../features/ai.md#ai-reply) | Click the ✦ button beside the message field and choose Help me reply. The suggestions appear above the field; click one to put it in, then send. |
| [AI assistant](../features/ai.md#ai-chat) | Open Luckgram AI at the top of the chat list, or the AI button beside the search field; right-click any message and choose Ask AI. Conversations are kept in this browser only. |
| [Chat summary](../features/ai.md#ai-summary) | ⋮ → Summarize chat at the top of a chat, for the last 100, 300 or 500 messages; with 30 or more unread messages a Summarize chat bar appears at the top. |
| [Private notes](../features/profiles-and-folders.md#user-notes) | Notes are kept in this browser only and do not sync with your phone; export and import them in Settings → Luckgram Features → All notes. |
| [Profile details](../features/profiles-and-folders.md#profile-info) | The profile panel shows the ID (click to copy) and the approximate registration date; very new accounts show as “about a given month or later”. |
| [Select all](../features/messaging.md#select-all) | Right-click a message and choose Select all messages from …; forwarding or deleting many messages is done in batches, with a progress line. |
| [Save in one tap](../features/messaging.md#save-direct) | Right-click a message and choose Save. |
| [Quick replies](../features/messaging.md#quick-replies) | Click the quick replies button beside the emoji button, or type “/” in the message field; Shift+click sends at once. The templates are kept in this browser only. |
| [Keyword folders](../features/profiles-and-folders.md#keyword-folders) | Create one in Settings → Chat Folders. Keyword folders are kept in this browser only, do not sync with your phone or Telegram, and always come after Telegram’s own folders; chats are matched by their recent messages, and archived chats are left out. |

Not there yet:

| Feature | Web app | iOS and Android apps |
|---|---|---|
| The other features in the [feature catalog](../features/README.md) | Not yet | Yes |
| Secret chats (end-to-end encrypted) | No; Telegram's web app does not have them | Yes |

**What is kept in this browser only?** Private notes, quick reply templates, keyword folders and
the AI assistant's conversations are stored in the current browser: they do not sync to the mobile
apps, nor to the web app opened on another computer, and they are cleared when you log out of the
account. Private notes can be exported to a file first.

**Where do the AI features send things?** AI writing, reply drafts, the AI assistant and chat
summaries send the text you give them to Luckgram's AI service. Translation uses Telegram's own
translation first; only when that is not available, or gives no result within 8 seconds, is the
text sent to Luckgram's AI service. Voice to text and dictation: for an account without Telegram Premium, the audio of a voice
message is sent to Luckgram's AI service to be transcribed (a Premium account's voice messages
are transcribed by Telegram); what you dictate is sent to Luckgram's AI service too, and with
**Tidy dictation with AI** on, the resulting text is sent once more to be tidied. You are asked
to agree the first time Luckgram's AI service is used.

Each feature has its own switch in **Settings → Luckgram Features**.

To add an account, open the menu at the top left and choose **Add Account**. With many accounts
the list of accounts in the menu scrolls. With 20 signed in, the app tells you that 20 is the limit.

For a feature the web app does not have yet, use the [iOS or Android app](install.md). The same
account can be signed in on both.

## Connection {#connection}

Some networks cannot reach Telegram's servers. The web app can connect through a Luckgram relay.
Choose under **Settings → Luckgram Features → Connection**:

| Option | Meaning | When to use it |
|---|---|---|
| **Automatic** (default) | Telegram's address or the relay, whichever connects first | Normally leave it here |
| **Telegram only** | Connects to Telegram's address only | You do not want traffic to pass through the relay |
| **Relay only** | Connects through the Luckgram relay only | Telegram's address keeps dropping |

The same page shows which route is in use. When no route connects, a bar at the top says
“Can't connect. Please check your network.” with a **Retry** button.

**What can the relay see?** The relay only forwards encrypted data. Message contents are encrypted
by Telegram's protocol between your browser and Telegram's servers; the relay cannot read them and
does not store them. It does not log IP addresses and keeps only counts of connections and traffic.

## Common problems {#faq}

- **The page stays blank or keeps loading:** keep the window in front. Browsers pause a page's
  start-up in a background or covered tab.
- **The sign-in page shows but the QR code is slow:** the connection to Telegram is probably slow.
  Wait a little, or set the connection to **Relay only** and try again.
- **No code arrives:** see “Where does the code arrive?” above, or sign in with the QR code.

**Last verified:** 17 November 2026.
