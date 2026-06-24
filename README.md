# 自动编译视频壳子

![Build](https://img.shields.io/github/actions/workflow/status/IsayIsee/TVBoxOS-Build/build.yml?branch=master&logo=github&label=Build&style=flat-square)
[![Release](https://img.shields.io/github/v/release/IsayIsee/TVBoxOS-Build?style=flat-square&logo=android&logoColor=white&label=Release&color=green)](https://github.com/IsayIsee/TVBoxOS-Build/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/IsayIsee/TVBoxOS-Build/total?style=flat-square&logo=download&label=Downloads&color=blue)](https://github.com/IsayIsee/TVBoxOS-Build/releases)
[![Last Commit](https://img.shields.io/github/last-commit/IsayIsee/TVBoxOS-Build/master?style=flat-square&logo=git&logoColor=white&label=Updated&color=lightgrey)](https://github.com/IsayIsee/TVBoxOS-Build/commits/master)

# **本项目目的**
  - **本仓库主要目的是方便自用**
  - **原始仓库可能不会每个版本都发布 apk。本项目可根据情况自动或手工执行编译，方便使用验证新版本功能**
  - **项目编译的视频壳子 Repo 都为原项目的 Fork，fongmi 和 webhtv 项目针对本人使用习惯进行了简单修改**

# 推荐
## **根据自己使用的感受强烈推荐 [webhtv](https://github.com/fish2018/webhtv) (以下内容来自源仓库描述)**
  - 开发相当活跃，更新非常频繁
  - 增强的同步工具能更方便的的同步多设备的环境和配置
  - 支持壳代理，选择站点自动生成建议配置
  - WebHome 扩展
  - 观影记录同步
  - 内置网盘搜索(盘搜)和网盘链接有效性检测
  - 站点注入，方便在线接口随时添加 webhome、自定义CSP、直播
  - 站点健康度学习，搜索和自动换源会优先使用健康度更高的站点
  - 支持网页管理，浏览器打开操作更便捷
  - 集成调试日志功能，方便快速定位问题
  - 远程托管

## **提示**
  ~~目前默认的 Nostr 推荐页面未进行分级过滤,会导致推荐热榜里有很多不合适的内容,如果你介意可以使用我提供的具有分级过滤的 [Nostr.html](https://github.com/IsayIsee/TVBoxOS-Build/tree/master/apk/webhtv_dev/Nostr.html), 可以放入本地然后使用注入功能注入。~~  
  源 Nostr 已提供分级选项  
  **注入的具体使用方法请参考仓库相关文档**
   

# 注意
- **本仓库使用的证书与原始仓库不相同，因此不能直接更新，如无特殊需求请尽量使用原始仓库版本**
- **为避免与原版本混淆，版本号会根据源代码更新时间生成，防止向开发者反馈问题时搞错**
- **FongMi 分支自动升级**
  - **本项目编译的 FongMi 版升级检查在编译时会被替换为为本仓库内 ~~apk 目录~~ Release 下对应的版本**
  - **本项目编译的 WebHomeTV 版升级检查在编译时会被替换为为本仓库内 ~~apk 目录~~ Release 下对应的版本**
  - apk 目录下的应用仅为旧版升级兜底，将在一段时间后彻底删除仅保留 json 文件

# 编译代码来自以下仓库
- [TVBoxOS/main](https://github.com/IsayIsee/TVBoxOS/tree/main) (Updated: 704cd2658fbcaf38551228cb90bd9f766a0c9e72)
- [Takagen-Box/main](https://github.com/IsayIsee/Takagen-Box/tree/main) (Updated: 258a5fef61578869ae905ca230bdde9e99fc19a8)
- [FongMI/my_dev](https://github.com/IsayIsee/FongMI/tree/my_dev) (Updated: 415d5e296589f044e5ea7643d099a80c5e08deb7)
- [webhtv/webhtv_dev](https://github.com/IsayIsee/webhtv/tree/webhtv_dev) (Updated: 4b1687b63c7390d07d40fce36d31d96a217eb166)


# 感谢
- [j4Uq/TVBoxOSC-Build](https://github.com/j4Uq/TVBoxOSC) 
- [tdlib/telegram-bot-api](https://github.com/tdlib/telegram-bot-api)
- [q215613905/TVBoxOS](https://github.com/q215613905/TVBoxOS)
- [takagen99/Box](https://github.com/takagen99/Box)
- [FongMi/TV](https://github.com/FongMi/TV)
- [fish2018/webhtv](https://github.com/fish2018/webhtv)