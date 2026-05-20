# Bigmi PoC 与 Proposal 对齐说明

这份文档的目的不是解释 Home Assistant，而是解释当前 PoC 如何服务于 Bigmi 的商业计划书主线。

## 核心定位

Bigmi 不是另一个智能家居控制 App。  
Bigmi 是智能家居和小型智能空间的 **programmable automation layer**。

一句话可以直接沿用到讲演里：

> Bigmi is a high-privilege programmable smart home customization platform that allows developers and advanced users to create, deploy, and share complex smart home automations across different devices and ecosystems.

## 六个核心关键词

### 1. 高权限

Bigmi 控制的不是单个设备开关，而是“整套空间行为”。

在当前 PoC 中，高权限体现在：

- 一个按钮可以联动多个房间和多台设备
- `Owner Arrives Home` 会停止扫地机、开空调、预热热水器、开灯、开窗帘
- `Safety Lab` 展示敏感操作的二次确认和运行留痕

### 2. 可编程

Bigmi 的差异化不在“能做自动化”，而在“可以像写程序一样编排空间”。

在当前 PoC 中，可编程体现在三层：

- Python Runtime
  - [bigmi_runtime.py](/Users/jarason/Documents/code/bigme-demo/appdaemon/conf/apps/bigmi_runtime.py)
  - [house_program_demo.py](/Users/jarason/Documents/code/bigme-demo/appdaemon/conf/apps/house_program_demo.py)
- Blueprint 模板
  - [programmable_scene_trigger.yaml](/Users/jarason/Documents/code/bigme-demo/ha/blueprints/automation/bigmi/programmable_scene_trigger.yaml)
- Webhook / API
  - `POST /api/webhook/bigmi_demo_scene`

### 3. 跨生态

Proposal 里强调 Bigmi 不是绑定某一家设备生态，而是站在生态上层。

当前 PoC 用虚拟桥接状态来表达：

- Xiaomi Bridge
- Tuya Bridge
- Matter Fabric

这些状态在 [bigmi_demo.yaml](/Users/jarason/Documents/code/bigme-demo/ha/packages/bigmi_demo.yaml) 和 `Bigmi Console` 中都能看到，适合在 PPT 里先讲“统一控制面”，后续再替换成真实设备。

### 4. 开发者友好

Bigmi 不是只给普通用户点按钮，而是给开发者一个真正可扩展的工作台。

当前 PoC 的开发者入口包括：

- AppDaemon Python 应用
- Blueprint 参数化模板
- Webhook/API 接口
- Trace 和日志
- Lovelace 中的 `Studio` 与 `Apartment` 演示面板

最关键的是，用户可以直接修改一个结构化脚本，而不是到处改零碎 YAML。

### 5. 安全可控

Proposal 里强调 Bigmi 是 high-privilege platform，因此安全不是附加项，而是产品核心。

当前 PoC 已经展示了：

- 敏感设备二次确认
- 运行日志
- Automation Trace
- 本地优先运行

这让你在讲演时可以明确区分：

- `低风险自动化`
  - 比如回家开灯、开窗帘、开空调
- `高风险自动化`
  - 比如门锁、摄像头、插座、安防权限

### 6. 模板市场

Proposal 里提到普通用户不写代码，而是安装开发者写好的模板。

当前 PoC 中，模板市场的最小可见形态就是：

- Blueprint
- 预装的 Blueprint automation
- `Run Blueprint Demo`

讲法可以是：

> 开发者不是直接把一个硬编码规则交给用户，而是把一个参数化、可复用的自动化接口发布到 Marketplace。

## 当前 PoC 对四个核心模块的映射

### 1. Runtime / Hub

- Home Assistant Container
- 统一设备状态
- 本地事件总线
- 多房间设备编排

### 2. Studio

- AppDaemon Python Runtime
- `Studio` 演示页
- 程序化事件入口
- 可读、可改、可扩展的脚本结构

### 3. Marketplace

- Blueprint
- 可复用 automation 模板
- 未来可扩展到 HACS 与真实分发

### 4. Safety & Permission Layer

- Safety Lab
- 二次确认
- Persistent notification
- Automation Trace

## 最适合 PPT 的表达方式

### 不要这样讲

- 这是一个 Home Assistant demo
- 这里有几个虚拟设备
- 这里可以写点自动化

### 更好的讲法

- Bigmi 把分散的设备控制上升为“空间级程序”
- Bigmi 的核心不是按钮，而是可编排的运行时
- Bigmi 让开发者写一次，把复杂自动化交付给普通用户和空间运营者使用
- Bigmi 在开放性和安全性之间做了产品化平衡

## 一句话总结

当前这个 PoC 证明的不是“我们能控制灯和空调”，而是：

**Bigmi 可以把一个房子抽象成可编程对象，把一个空间场景抽象成可复用程序。**
