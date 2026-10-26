---
description: Hide selected Luckgram accounts or chats and understand what these controls do not protect.
---

# How do Luckgram privacy controls work?

> **In development.** The features on this page are not in Luckgram yet. They are on the roadmap; this page describes the planned behavior.

Luckgram adds controls that reduce what appears in the normal app interface. They
are useful when several people can see or temporarily handle your device, but they
do not replace device security or Telegram’s account protections.

## Double Bottom

Double Bottom creates an alternate hidden account surface. After setup, the normal
entry path shows your regular accounts; the configured alternate action or code
reveals the hidden set.

1. Open Luckgram settings and find **Double Bottom** or hidden-account settings.
2. Configure the alternate access method offered by your build.
3. Add only the intended accounts to the hidden surface.
4. Lock the app and test both the normal and alternate paths before relying on it.

If you forget the Double Bottom credential, recovery can be limited. Do not set it
until you know which recovery option the current screen provides.

## Hidden chats

Hidden chats remove selected conversations from the normal chat list and expose
them through Luckgram’s hidden-chat entry point. Hiding a chat does not delete it,
change Telegram retention, or make messages invisible on another signed-in device.

## Immediate auto-lock

Supported builds offer shorter auto-lock intervals than the normal client flow.
Use a device passcode and biometric lock as the first layer; use Luckgram’s lock as
an additional client layer.

## Phone-number controls

Some builds expose an extra phone-number visibility control or guidance. Telegram
still owns the account’s underlying privacy rules, so confirm the result under
**Settings → Privacy and Security → Phone Number**.

## Restricted channels {#restricted-channels}

> **In development.** Luckgram does not include this yet. It is on the roadmap; this section describes the planned behavior.

Some channels and groups are hidden only in the App Store and Google Play builds of
Telegram, which show "Channel unavailable" when you open them. In Luckgram:

1. Tap **Change settings** on such a channel, or open **Content Settings** in Luckgram settings.
2. Turn on **Show restricted channels**.
3. Go back to the channel; its content now shows.

The switch is free and stays on; no website sign-in is needed. It only lifts the
hiding done by the store builds: channels Telegram blocks for everyone, channels
blocked by law where you live, and deleted or private content still do not open.
What you choose to view is up to you; follow the law where you live.

See also: [Why can't I see sensitive (18+) or restricted content?](../help/sensitive-content.md)

## Hidden chats are not Secret Chats

Hidden chats change the local Luckgram interface. Telegram Secret Chats are a
separate Telegram conversation type with their own encryption and device behavior.

**Availability:** iOS and Android; exact labels and recovery behavior vary.

**Sources:** [Official feature list](https://luckgram.cc/en/features) ·
[Official status labels](https://wiki.luckgram.cc/en/getting-started/install.html) ·
[Telegram privacy FAQ](https://telegram.org/faq#privacy)
