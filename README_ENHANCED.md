# OK-WW Enhanced - 鸣潮自动化增强版

基于 ok-wuthering-waves 的增强版本，增加了多账号管理、自定义任务配置、截图保存等功能。

## 新增功能

### 1. 多账号每日任务（CustomDailyTask）
- 每个账号可配置不同的副本组合
- 配置文件格式：`账号 - 体力副本 - 梦魇 - 截图编号`
- 自动切换账号，自动恢复键位

### 2. 周常自动乐园（WeeklyParadiseTask）
- 自动完成周常乐园任务
- 支持自动领取奖励

### 3. 活动框架（ActivityFramework）
- 支持限时活动和周期活动
- 预留扩展接口，方便后续添加新活动

### 4. 截图保存（ScreenshotTask）
- 满活跃界面自动截图
- 按账号分目录保存
- 可选同步到 NAS

### 5. 纯战斗模式（CombatModeTask）
- 检测到怪物后自动战斗
- 支持自定义战斗配置
- 滚轮锁定视角

### 6. 连接模式（ConnectionModeTask）
- 手动启动游戏后连接
- 适合临时刷活动

## 副本类型

| 类型 | 体力消耗 | 领奖方式 | 限制 |
|------|---------|---------|------|
| 世界 boss | 60 | 单倍领取 | 无 |
| 周本 | 60 | 单倍领取 | 每周限 3 次 |
| 副本 | 40 | 双倍领取 | 刷到 240 体力 |
| 声骸 | 60 | 双倍领取 | 刷到 240 体力 |
| 梦魇 | 0（免费） | - | 读界面 X/Y 判断 |

## 配置文件格式

```
账号 - 体力副本 1|体力副本 2-梦魇 1|梦魇 2-截图编号

示例：
13812345678-世界 boss|周本 | 副本 - 梦 A|梦 B-003
lisi-副本--001
wangwu--梦 A|梦 B|梦 C-005
```

## 安装和使用

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行
```bash
python main.py
```

### 3. 打包成 exe
```bash
pyappify pack
```

打包完成后在 `dist/` 目录找到 `ok-ww.exe`

## 目录结构

```
├── configs/
│   ├── daily/          # 每日任务配置
│   ── event/          # 活动配置
├── combat_config/
│   ├── default.json    # 默认战斗配置
│   └── custom/         # 自定义角色战斗配置
── screenshots/        # 截图保存目录
── logs/               # 日志目录
└── src/
    ├── task/           # 任务模块
    └── gui/            # GUI 界面
```

## 注意事项

1. 首次使用需要先手动登录游戏，保存登录状态
2. 配置文件放在 `configs/daily/` 目录，文件名就是配置
3. 截图默认保存到 `screenshots/账号名/` 目录
4. 日志按日期保存在 `logs/` 目录

## 致谢

基于 [ok-wuthering-waves](https://github.com/ok-oldking/ok-wuthering-waves) 开发
