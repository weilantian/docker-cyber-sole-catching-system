# cybercoleCatchingSystem
这是一个docker封装的python小程序，用了docker是因为部分的截图功能需要用到带chromedriver的linux服务器，配置起来少许会有一点麻烦，所以就封装在docker中了。

## 需要实现的功能
- 实时对cybersole进行**良心监控**，指在对方网站的接受范围内，对网站的变化进行抓取
- 使用验证码提示用户付款时间，并提供进入cybercoleCatchingSystem管理网站的入口
- 一个网站用于管理系统的运行状态
- 对网站进行截图并提供预览