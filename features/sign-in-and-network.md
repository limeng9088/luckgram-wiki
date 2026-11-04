---
description: 连不上 Telegram 时在登录页配置代理，登录后在哪里切换代理，以及验证码发到 Telegram 应用里时怎么找到它。
---

# 登录与网络

<!-- features:top -->
> 本页各功能的状态与 [Luckgram 功能介绍](https://luckgram.cc/features/) 一致。 [← 返回功能介绍](https://luckgram.cc/features/)
<!-- features:top:end -->

## 代理配置 {#proxy}

> **已上线** · [在功能介绍中查看](https://luckgram.cc/features/#proxy) <!-- status:proxy -->

很多网络环境下，第一次打开就连不上 Telegram，收不到验证码。Luckgram 把代理入口放在了随手能点到的地方：

- **登录时：** 登录流程的每一页（输入手机号、验证码、两步验证密码、注册姓名）右上角都有代理图标。灰色线框表示没开代理，转圈表示正在连接，实心表示已连接。点它打开 Telegram 的代理设置，添加 SOCKS5 或 MTProto 代理后返回，图标状态会立即更新。
- **登录后：** 点聊天列表右上角的 **⋮**，菜单最上面是 **代理配置**，右侧显示当前状态（未开启、连接中、已连接）。

也可以直接打开别人分享的 `t.me/proxy` 或 `tg://proxy` 链接添加代理，登录前后都可以。代理由你自己选择和提供，Luckgram 不提供代理服务；请只使用你信任的代理。

## 收码说明 {#login-code}

> **已上线** · [在功能介绍中查看](https://luckgram.cc/features/#login-code) <!-- status:login-code -->

如果你的账号已经在别的设备上登录，Telegram 通常会把登录验证码发到那台设备上的 Telegram 应用里，而不是发短信。这时验证码页会多出一张说明卡片：

1. 在另一台已登录的设备上打开 Telegram（或 Luckgram）。
2. 在聊天列表里找到官方账号 **Telegram**（带蓝色认证标）发来的消息。
3. 把消息里的 5–6 位验证码填进来。

点 **知道了** 收起卡片。点 **收不到验证码？** 可以看到更多说明：

- 所有设备都已退出时，点 Telegram 原有的 **没有收到验证码？**，可以改用短信（如果 Telegram 允许）；
- 网络连不上时，先点右上角的代理图标配置[代理](#proxy)。

验证码只在登录时用。任何人（包括自称客服的人）向你索要验证码都是诈骗。

**可用平台：** iOS 和 Android。
