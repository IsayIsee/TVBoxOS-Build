# 自动编译视频壳子

![Build](https://img.shields.io/github/actions/workflow/status/IsayIsee/TVBoxOS-Build/build.yml?branch=master&logo=github&label=Build&style=flat-square)
[![Release](https://img.shields.io/github/v/release/IsayIsee/TVBoxOS-Build?style=flat-square&logo=android&logoColor=white&label=Release&color=green)](https://github.com/IsayIsee/TVBoxOS-Build/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/IsayIsee/TVBoxOS-Build/total?style=flat-square&logo=download&label=Downloads&color=blue)](https://github.com/IsayIsee/TVBoxOS-Build/releases)
[![Last Commit](https://img.shields.io/github/last-commit/IsayIsee/TVBoxOS-Build/master?style=flat-square&logo=git&logoColor=white&label=Updated&color=lightgrey)](https://github.com/IsayIsee/TVBoxOS-Build/commits/master)

# **本项目目的**
  - **本项目主要目的为测试 Action 的 APK 的自动构建能力和在构建前对被编译代码进行简单定制的功能**
  - **原始仓库可能不会每个版本都发布 APK。本项目可根据情况自动或手工执行编译，方便使用验证新版本功能**

# 注意
- 
- **本仓库使用的证书与原始仓库不相同，因此不能直接更新，如无特殊需求请尽量使用原始仓库版本**
- **为避免与原版本混淆，版本号会根据源代码更新时间生成，防止向开发者反馈问题时搞错**
- **FongMi 分支自动升级**
  - **本项目编译的 FongMi 版升级检查在编译时会被替换为为本仓库内 ~~apk 目录~~ Release 下对应的版本**
  - **本项目编译的 WebHomeTV 版升级检查在编译时会被替换为为本仓库内 ~~apk 目录~~ Release 下对应的版本**
  - apk 目录下的应用仅为旧版升级兜底，将在一段时间后彻底删除仅保留 json 文件

# 编译代码来自以下仓库
- [TVBoxOS/main](https://github.com/IsayIsee/TVBoxOS/tree/main) (Updated: 704cd2658fbcaf38551228cb90bd9f766a0c9e72)
- [Takagen-Box/main](https://github.com/IsayIsee/Takagen-Box/tree/main) (Updated: 258a5fef61578869ae905ca230bdde9e99fc19a8)
- [FongMI/my_dev](https://github.com/IsayIsee/FongMI/tree/my_dev) (Updated: e758f5fc9efd5ec398cb2743ec6441a93457f26f)
- [webhtv/webhtv_dev](https://github.com/IsayIsee/webhtv/tree/webhtv_dev) (Updated: c12a0503c3923a253824dd245f3e1b3abf7bd666)


# 感谢
- [j4Uq/TVBoxOSC-Build](https://github.com/j4Uq/TVBoxOSC) 
- [tdlib/telegram-bot-api](https://github.com/tdlib/telegram-bot-api)
- [q215613905/TVBoxOS](https://github.com/q215613905/TVBoxOS)
- [takagen99/Box](https://github.com/takagen99/Box)
- [FongMi/TV](https://github.com/FongMi/TV)
- [fish2018/webhtv](https://github.com/fish2018/webhtv)