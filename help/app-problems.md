---
description: Luckgram 打不开或一直加载、要求更新却找不到更新、通知重复或收不到、更新后聊天不见了、耗电快、忘记应用密码时怎么办，以及如何使用代理。
---

# Luckgram 用不了时怎么办？

先从不会丢数据的步骤开始。删除应用之前，请先阅读[重装 Luckgram 之前](#before-you-reinstall-luckgram)。

## Luckgram 打不开、闪退或一直加载 {#luckgram-wont-open-crashes-or-keeps-loading}

1. 彻底关闭 Luckgram 后重新打开，然后重启设备。
2. 如果聊天列表显示 **连接中…** 或 **等待网络**，说明应用还没有连上 Telegram。请检查 Wi-Fi 或移动数据。
3. 从应用商店或[官方下载页面](https://wiki.luckgram.cc/getting-started/install.html)安装最新版本。
4. 如果设备存储空间快满了，清理出一些空间。
5. 还是不行？请通过[客服与源码](support-and-source.md#reporting-a-problem)报告问题，写明设备、系统版本、Luckgram 版本和你看到的情况。

## 重装 Luckgram 之前 {#before-you-reinstall-luckgram}

卸载应用会让这台设备退出登录。之后你需要重新登录每个账号，包括用双重空间隐藏的账号。有些登录可能再也回不来，所以请先检查：

- **先保存你的账号**（如果你的版本提供）：保存到文件，或开启 iCloud 备份（iOS 15 及以上）。见[账号迁移工具](../getting-started/accounts.md#back-up-import-or-export-accounts)。
- **通过 Telegram 会话购买或以会话方式导入的账号**，用的可能是不在你手里的手机号，你可能无法重新登录。请先[联系客服](support-and-source.md)，不要把退出登录当作通用修复办法。
- **登录验证码** 通常会发到另一台已登录设备上的 Telegram 里。如果验证码会发到这个应用里，点 **没有收到验证码？**，有短信选项时选择短信。
- **两步验证密码：** 如果设置过就需要输入（忘了？见[两步验证密码帮助](../getting-started/accounts.md#i-forgot-my-two-step-verification-password)）。

Telegram 会保留你的云端聊天。私密聊天会丢失，快捷回复和下载内容等 Luckgram 本地数据也可能无法恢复。

## Luckgram 提示更新，但商店里没有更新 {#luckgram-asks-me-to-update-but-the-store-has-no-update}

- **“你的版本不支持此消息”**（或快拍）只针对那一条内容；应用的其他部分正常。
- **“请将 Telegram 更新到最新版本后登录”** 是登录时 Telegram 服务器返回的提示。
- **Luckgram 更新页面**（iPhone、iPad）会在 Telegram 服务器通知有更新时出现。**更新 Luckgram** 会打开 App Store；除非是必须的更新，否则会提供 **跳过**。

如果商店里没有更新的版本，请查看[官方下载页面](https://wiki.luckgram.cc/getting-started/install.html)。那里的 APK 适用于没有 Google Play 的 Android 设备。如果 Android 无法用它覆盖安装商店版本，不要卸载 Luckgram；请看上面的“重装 Luckgram 之前”。

## 更新后聊天不见了 {#my-chats-are-gone-after-an-update}

Telegram 把你的云端聊天保存在服务器上，而不只在手机上，所以只要登录同一个账号，聊天就会回来。先检查这些：

1. **账号。** 打开账号切换器，确认当前账号就是你之前用的那个：每个账号有自己的聊天（见[切换账号](../getting-started/accounts.md#switch-accounts)）。用另一个手机号登录，打开的是另一个账号。
2. **归档。** 在聊天列表上向下滑，查看 **已归档的聊天**。默认情况下，未静音的归档聊天收到新消息后会回到列表；已静音的会留在归档里。
3. **文件夹。** 如果打开的是某个文件夹标签，请切换到 **全部聊天**（或 **全部**）。文件夹只显示符合条件的聊天。
4. **隐藏聊天。** 你在 Luckgram 里隐藏的聊天并没有被删除（见[隐藏聊天](../features/privacy.md#hidden-chats)）；在 iPhone 和 iPad 上，聊天菜单里有 **取消隐藏**。
5. **网络连接。** 聊天列表显示 **连接中…** 或 **等待网络** 时，应用还没有连上 Telegram（见[Luckgram 打不开、闪退或一直加载](#luckgram-wont-open-crashes-or-keeps-loading)）。

私密聊天是例外：它们只保存在发起聊天的那台设备上，退出登录或卸载应用后就会丢失，无法找回。Telegram 会保存什么、怎样保存自己的副本，见[怎样备份所有聊天和媒体？](../getting-started/accounts.md#how-do-i-back-up-all-my-chats-and-media)

如果更新后应用出了问题、你正打算重装，请先阅读[重装 Luckgram 之前](#before-you-reinstall-luckgram)。

**来源：** [依据记录](../docs/evidence/help-w6a-2026-10-16.md)

## 通知重复或反复出现 {#notifications-repeat-or-keep-coming-back}

1. 在 **设置 → 通知与声音** 中检查设置，把不需要的聊天静音。
2. 有多个账号时，**所有账号** 决定是所有已登录账号都给你发通知，还是只有当前账号发。
3. 如果同一个账号在这台手机上同时登录了 Telegram 和 Luckgram，两个应用都可能发通知。请在其中一个里关闭通知。
4. 检查系统通知设置，更新 Luckgram 后重新打开。

如果问题仍然存在，请报告平台、Luckgram 版本以及发生的频率。

## 完全收不到通知 {#i-get-no-notifications-at-all}

- **手机设置。** 在 iPhone 和 iPad 上，**设置** 里 **通知与声音** 旁边出现红色 **!**，说明通知已关闭或受限；该页面会提供开启按钮（**在设置中开启**、**打开设置** 或 **开启通知**）。在 Android 上，如果 Luckgram 请求你 **开启通知**，请允许。
- **Luckgram 的设置。** 在 **设置 → 通知与声音** 中，保持 **私人聊天**、**群聊**（Android 上为 **群组**）和 **频道** 开启。在 Android 上，逐个打开它们，点 **更多选项**，把 **重要性** 设为 **高** 或 **紧急**。
- **静音的聊天、专注模式和勿扰模式。** 静音的聊天不会发出提醒：打开聊天并选择 **取消静音**（iPhone 和 iPad：点聊天名称；Android：点 **⋮** 菜单）。iPhone 和 iPad 上的专注模式（如勿扰模式）或 Android 上的勿扰模式，会让你没有允许的应用保持安静。
- **Android 省电设置。** 保留 Google Play 服务，并在所有省电应用中允许 Luckgram；在华为和小米手机上，还要在 **受保护应用** 或 **自启动** 中允许。**通知与声音** 里的 **保活服务** 和 **后台连接** 会有帮助，但会多耗一些电。
- **iPhone 或 iPad 上仍然没有通知：** 关闭 Luckgram，在设备设置中把它的提醒样式设为“无”，打开 Luckgram，再改回“横幅”。

**来源：** [依据记录](../docs/evidence/help-w6b-2026-10-16.md)

## Luckgram 耗电快 {#luckgram-drains-the-battery}

- **设置 → 省电模式**（Android 上叫 **电量使用**）可以在电量低于你设定的值时自动开启，并关闭自动播放、动画和特效。
- 在 Android 上，**通知与声音** 里的 **保活服务** 和 **后台连接** 会让应用在后台保持运行，以便可靠地接收通知。请根据需要决定是否开启。

如果耗电仍然很高，请报告设备型号、系统版本和 Luckgram 版本。

## Luckgram 能用代理吗？ {#can-i-use-a-proxy-in-luckgram}

能。Luckgram 的代理设置与 Telegram 官方应用相同：

- **iPhone 和 iPad：** **设置 → 数据与存储 → 代理**。添加代理后，**代理** 也会出现在设置主列表中。
- **Android：** **设置 → 数据与存储 → 代理设置**。

点 **添加代理**，选择代理使用的类型：

- **SOCKS5** 需要服务器和端口。用户名和密码可选。
- **MTProto** 需要服务器、端口和密钥（secret）。

应用通过代理连接时，主界面顶部会显示 **正在连接代理…**。如果一直停在这里，代理可能不可用：打开代理设置换一个已保存的代理，或关闭 **使用代理** 直接连接。

只使用来源可信的代理。代理运营者无法读取你的消息，但能看到你的 IP 地址以及你在使用 Telegram。MTProto 代理还可能在你的列表中添加一个赞助频道。

在 Telegram 本身不需要代理就能使用的地方，Luckgram 也不需要代理或 VPN：Luckgram 连接的是 Telegram 官方服务器。在 Telegram 受限的地方，Luckgram 也同样受限。

## 忘记应用密码，无法解锁 Luckgram {#i-forgot-my-app-passcode-and-cant-unlock-luckgram}

应用密码是 **设置 → 隐私与安全** 里的 **密码锁**。用面容或指纹解锁只是其中的一个选项，密码依然存在。它不是登录时使用的两步验证密码（忘了那个？见[两步验证密码帮助](../getting-started/accounts.md#i-forgot-my-two-step-verification-password)）。

应用密码无法重置。密码页面上写着：如果忘记密码，必须卸载并重新安装应用，私密聊天会丢失。这可能导致某些账号永久无法登录。锁定状态下的应用无法保存账号；只有之前开启过 iCloud 备份（iOS 15 及以上），**从 iCloud 导入** 才有效。否则，每个账号都需要登录验证码和两步验证密码；对于购买或以会话方式导入的账号，请在卸载之前先[联系客服](support-and-source.md)。

**来源：** [依据记录](../docs/evidence/help-troubleshooting-2026-10-12.md) ·
[依据记录（10 月 13 日）](../docs/evidence/help-troubleshooting-2026-10-13.md)
