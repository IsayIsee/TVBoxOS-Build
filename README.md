# 自动编译视频壳子

![Build](https://img.shields.io/github/actions/workflow/status/IsayIsee/TVBoxOS-Build/build.yml?branch=master&logo=github&label=Build&style=flat-square)
[![Release](https://img.shields.io/github/v/release/IsayIsee/TVBoxOS-Build?style=flat-square&logo=android&logoColor=white&label=Release&color=green)](https://github.com/IsayIsee/TVBoxOS-Build/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/IsayIsee/TVBoxOS-Build/total?style=flat-square&logo=download&label=Downloads&color=blue)](https://github.com/IsayIsee/TVBoxOS-Build/releases)
[![Last Commit](https://img.shields.io/github/last-commit/IsayIsee/TVBoxOS-Build/master?style=flat-square&logo=git&logoColor=white&label=Updated&color=lightgrey)](https://github.com/IsayIsee/TVBoxOS-Build/commits/master)

# 推荐
## **根据自己使用的感受强烈推荐 webhtv(以下内容来自源仓库描述)**
  - 增强的同步工具能更方便的的同步多设备的环境和配置
  - 支持壳代理，选择站点自动生成建议配置
  - 新增的 WebHome 自定义首页能力
    - 可以调用 app 原生开放能力
    - Nostr推荐榜单，基于去中心化技术实现，根据真实用户观影数据自动发布榜单*
    - 集成 WebHome 扩展脚本注入功能，可自由改变网站界面/能力
  - 观影记录同步
  - 内置网盘搜索(盘搜)和网盘链接有效性检测
  - 站点注入，方便在线接口随时添加 webhome、自定义CSP、直播
  - 站点健康度学习，搜索和自动换源会优先使用健康度更高的站点
  - 支持网页管理，浏览器打开操作更便捷
  - 集成调试日志功能，方便快速定位问题
## **提示**
  ~~目前默认的 Nostr 推荐页面未进行分级过滤,会导致推荐热榜里有很多不合适的内容,如果你介意可以使用我提供的具有分级过滤的 [Nostr.html](https://github.com/IsayIsee/TVBoxOS-Build/tree/master/apk/webhtv_dev/Nostr.html), 可以放入本地然后使用注入功能注入。~~  
  **注入的具体使用方法请参考源仓库**
   

# 注意
- **为避免与原版本混淆，本仓库编译的 APK 证书使用的证书与原始仓库不相同**
- **版本号会根据源代码更新时间生成，避免和原版本混淆**
- **FongMi 分支自动升级**
  - **本项目编译的 FongMi 版升级检查在编译时会被替换为为本仓库内 apk 目录下对应的版本**
  - **本项目编译的 WebHomeTV 版升级检查在编译时会被替换为为本仓库内 apk 目录下对应的版本**

# 编译代码来自以下仓库
- [TVBoxOS/main](https://github.com/IsayIsee/TVBoxOS/tree/main) (Updated: 704cd2658fbcaf38551228cb90bd9f766a0c9e72)
- [Takagen-Box/main](https://github.com/IsayIsee/Takagen-Box/tree/main) (Updated: 258a5fef61578869ae905ca230bdde9e99fc19a8)
- [FongMI/my_release](https://github.com/IsayIsee/FongMI/tree/my_release) (Updated: 809725308faebb6c9d99644a79a181bc279a8326)
- [FongMI/my_dev](https://github.com/IsayIsee/FongMI/tree/my_dev) (Updated: bc5f3a9ccee3bf8a5443db1ec8bd78a783e4f5e0)
- [webhtv/webhtv_dev](https://github.com/IsayIsee/webhtv/tree/webhtv_dev) (Updated: a56a589d0453a3aeecf670b1151ff78621eedd5d)


# 感谢
- [j4Uq/TVBoxOSC-Build](https://github.com/j4Uq/TVBoxOSC) 
- [tdlib/telegram-bot-api](https://github.com/tdlib/telegram-bot-api)
- [q215613905/TVBoxOS](https://github.com/q215613905/TVBoxOS)
- [takagen99/Box](https://github.com/takagen99/Box)
- [FongMi/TV](https://github.com/FongMi/TV)
- [fish2018/webhtv](https://github.com/fish2018/webhtv)