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
file transfers work the same way. Of the features Luckgram adds, the web app has one so far:

| Feature | Web app | iOS and Android apps |
|---|---|---|
| [More accounts](../features/privacy.md#accounts) | Up to 20, no Luckgram Pro needed | 10 free, unlimited with Luckgram Pro |
| The other features in the [feature catalog](../features/README.md) | Not yet | Yes |
| Secret chats (end-to-end encrypted) | No; Telegram's web app does not have them | Yes |

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

**Last verified:** 13 November 2026.
