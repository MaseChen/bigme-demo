# Bigmi 技术与商业报告参考文档

本文档面向最终报告撰写者，目标是把当前 Bigmi PoC 的产品结构、技术实现、演示价值和商业含义统一说明清楚。它不是操作手册，而是一份可直接抽取内容进入商业计划书、技术章节、PPT 讲稿和答辩材料的参考资料。

当前项目使用 Home Assistant 生态作为本地沙箱，但它的展示目标不是证明 Home Assistant 本身，而是证明 Bigmi 可以作为智能家居和小型智能空间的可编程自动化中间层。

## 1. 项目定位

Bigmi 的核心定位是：

> Bigmi is a high-privilege programmable smart home customization platform that allows developers and advanced users to create, deploy, and share complex smart home automations across different devices and ecosystems.

中文表达可以写成：

> Bigmi 不是另一个智能家居控制 App，而是智能家居和小型智能空间的可编程自动化中间层。

当前 PoC 的核心任务是把这句话可视化。它通过一个本地运行的 Bigmi Console，展示如下能力：

- 用户可以一键启动复杂空间场景。
- 高阶用户可以通过 Python 脚本修改空间程序。
- 开发者可以通过 Blueprint、Webhook、Node-RED 等多种入口接入运行时。
- 普通用户可以从 Marketplace 风格界面安装场景包。
- 高权限动作有单独的安全中心和审批链路。

## 2. 总体架构

当前项目采用容器化架构：

- Home Assistant Container 作为本地状态层、事件总线、dashboard 宿主和自动化引擎。
- AppDaemon 作为 Python Runtime，用来承载 Bigmi 的可编程自动化逻辑。
- Node-RED 作为可视化规则编辑器，用 webhook 调用 Bigmi Runtime。
- Lovelace YAML dashboard 作为 Bigmi Console 的产品前台。
- Home Assistant Blueprint 和 HACS 路径作为 Marketplace 的底层证明。

核心文件映射如下：

- `docker-compose.yml`：定义 Home Assistant、AppDaemon、Node-RED 三个容器。
- `ha/configuration.yaml`：挂载 dashboard、REST command、manual alarm panel 和 HA 主配置。
- `ha/packages/bigmi_demo.yaml`：定义虚拟设备、状态 helper、指标 sensor、group。
- `ha/dashboards/bigmi-console.yaml`：Bigmi Console 的五个主要视图。
- `ha/scripts.yaml`：场景触发、Marketplace 安装模拟、安全控制动作。
- `ha/automations.yaml`：Blueprint demo、Webhook 接入、安全审批和 trace 自动化。
- `appdaemon/conf/apps/bigmi_runtime.py`：模式级 Python runtime。
- `appdaemon/conf/apps/house_program_demo.py`：空间程序库。
- `nodered/data/flows.json`：Node-RED 可视化规则 demo。

从事件流看，系统的核心链路是：

```text
Bigmi Console / Blueprint / Webhook / Node-RED
  -> Home Assistant event or webhook
  -> AppDaemon Python Runtime
  -> input_boolean / input_text / persistent notification / trace
  -> Bigmi Console 状态变化
```

这条链路是整套 PoC 的关键。它说明 Bigmi 的核心不是某一个 UI 按钮，而是多个入口共享同一个可编程执行层。

## 3. Bigmi Console 总览

Bigmi Console 目前分为五个视图：

- `Home`
- `Spaces`
- `Marketplace`
- `Security`
- `Developer`

这五个页面分成两层叙事：

- User Console：`Home`、`Spaces`、`Marketplace`、`Security`
- Developer Console：`Developer`

这样设计的原因是：普通用户和投资人更需要看到清晰的产品前台，而开发者和答辩评委可能会追问底层如何实现。前台负责产品感，后台负责技术可信度。

## 4. Bigmi Console -> Home

### 4.1 页面定位

`Home` 是 Bigmi Console 的首页，也是最适合开场展示的页面。它承担三个任务：

- 给观众一个 Bigmi 产品前台的第一印象。
- 快速说明 Bigmi 连接了生态、模板、安全和空间程序。
- 提供少量高价值快捷入口，而不暴露过多底层 helper。

页面文件位置：

- `ha/dashboards/bigmi-console.yaml`

### 4.2 页面组成

`Home` 页面包含：

- 顶部品牌视觉图：`/local/bigmi-stage.svg`
- 三个关键指标：
  - `Ecosystems`
  - `Installed Packs`
  - `Safety Queue`
- 快捷启动按钮：
  - `Arrive Home`
  - `Rental Check-in`
  - `Quiet Night`
  - `Open Marketplace`
- 平台快照：
  - runtime 状态
  - 当前主生态
  - Space Guard 状态
  - 已安装模板包数量
  - 当前空间程序状态
- 三个旗舰体验：
  - Esports Arena
  - Rental Host
  - Cinema Room

### 4.3 技术实现

`Home` 页面主要消费以下实体：

- `sensor.bigmi_connected_ecosystems`
- `sensor.bigmi_installed_pack_count`
- `sensor.bigmi_approval_queue`
- `sensor.bigmi_runtime_status`
- `input_select.bigmi_primary_ecosystem`
- `alarm_control_panel.bigmi_space_guard`
- `input_text.bigmi_house_program_status`
- `input_boolean.bigmi_esports_mode`
- `input_boolean.bigmi_rental_mode`
- `input_boolean.bigmi_cinema_mode`

其中 `sensor.bigmi_connected_ecosystems`、`sensor.bigmi_installed_pack_count`、`sensor.bigmi_approval_queue` 等都是 template sensor，定义在：

- `ha/packages/bigmi_demo.yaml`

快捷按钮调用的脚本定义在：

- `ha/scripts.yaml`

例如 `Arrive Home` 最终触发：

```text
script.bigmi_run_owner_arrives_home_program
  -> event: bigmi_run_house_program
  -> AppDaemon BigmiHouseProgramDemo
  -> 执行 owner_arrives_home steps
```

### 4.4 商业含义

`Home` 页面支撑的商业叙事是：

- Bigmi 不是设备遥控器，而是空间控制入口。
- 用户打开 Bigmi 看到的是场景、模板和安全状态，而不是零散设备。
- Bigmi 可以把多生态、多场景、多用户角色收束到一个统一前台。

这部分适合写进报告中的产品概述、用户价值和差异化章节。

## 5. Bigmi Console -> Space Program

### 5.1 页面定位

`Spaces` 页面是当前项目最能体现“可编程空间”的页面。报告中也可以称它为 `Space Program` 模块。

它展示的核心思想是：

> 房子不是设备列表，而是一个可编程对象。场景不是单个开关，而是一段可维护、可扩展的空间程序。

页面文件位置：

- `ha/dashboards/bigmi-console.yaml`

核心运行时文件：

- `appdaemon/conf/apps/house_program_demo.py`

### 5.2 空间模型

当前空间模型包含六个房间和一个支持系统层：

- Entryway
- Living Room
- Kitchen
- Bedroom
- Bathroom
- Study
- Support Systems

这些空间定义在 `house_program_demo.py` 的 `ROOMS` 字典中。每个空间都有：

- 内部 room key
- 展示 label
- 关联设备实体列表

这种结构对最终报告很重要，因为它说明 Bigmi 可以把空间建模成结构化对象，而不是把自动化写成零散规则。

### 5.3 场景库

当前 `Spaces` 页面提供九个空间程序：

- `Owner Arrives Home`
- `Elder Care`
- `Energy Saver`
- `Pet Mode`
- `Rental Check-in`
- `Esports Room`
- `Cinema Room`
- `Quiet Night`
- `Work From Home`

这些程序定义在 `house_program_demo.py` 的 `PROGRAMS` 字典中。每个 program 包含：

- `title`
- `status`
- `steps`
- `final_status`

每个 step 包含：

- `room`
- `entity_id`
- `state`
- `note`

这是一种非常适合讲演的“低代码结构”。它对普通观众可解释，对开发者也可修改。

### 5.4 程序执行方式

以 `Owner Arrives Home` 为例：

```text
Bigmi Console -> Spaces -> Owner Arrives Home
  -> script.bigmi_run_owner_arrives_home_program
  -> event bigmi_run_house_program
  -> BigmiHouseProgramDemo._handle_program_event
  -> run_in 分步执行每个 step
  -> 更新设备状态、房间状态、runtime audit
```

`run_in` 让程序以分步方式执行，演示时可以看到设备状态逐个变化。这比瞬间全部切换更有可视化效果，也更容易讲“程序正在运行”。

### 5.5 场景商业映射

每个场景都可以对应 proposal 中的市场场景：

- `Elder Care`：老人照护，展示安全、提醒和低风险行动辅助。
- `Energy Saver`：节能模式，展示空间级能耗优化。
- `Pet Mode`：宠物场景，展示无人状态下的照护自动化。
- `Rental Check-in`：民宿入住，展示小型空间运营价值。
- `Esports Room`：电竞房，展示高价值垂直空间定制。
- `Cinema Room`：影音房，展示氛围型空间编排。
- `Quiet Night`：夜间安静，展示家庭 policy automation。
- `Work From Home`：居家办公，展示生产力环境编排。

### 5.6 技术价值

`Spaces` 页面证明了三件事：

- Bigmi 能做多设备、多房间、多步骤编排。
- 高阶用户可以通过修改 Python 字典扩展场景。
- 同一套空间模型可以适配家庭、民宿、公寓、办公室、影音房、电竞房等场景。

报告中可以把这部分称为 Bigmi 的 `Programmable Space Model`。

## 6. Bigmi Console -> Marketplace

### 6.1 页面定位

`Marketplace` 是一个 Bigmi 风格的模板市场前台壳。它的目的不是实现完整交易系统，而是在讲演中证明：

- 开发者可以交付模板包。
- 普通用户可以安装模板包。
- 模板安装后可以直接启动场景。

页面文件位置：

- `ha/dashboards/bigmi-console.yaml`

相关 helper 和脚本位置：

- `ha/packages/bigmi_demo.yaml`
- `ha/scripts.yaml`

### 6.2 页面组成

`Marketplace` 页面包含：

- 顶部品牌视觉图：`/local/bigmi-marketplace-stage.svg`
- 指标：
  - `Installed Packs`
  - `Template Catalog`
- Marketplace 状态：
  - 最近一次安装事件
  - 已安装代表性 pack
- Featured Packs：
  - Elder Care Pack
  - Rental Ops Pack
  - Quiet Night Pack
  - Workday Pack
  - Esports Pack
  - Cinema Pack
- Install Featured Packs：
  - 安装按钮
- Launch Installed Pack Demos：
  - 安装后启动对应场景

### 6.3 技术实现

Marketplace 的安装状态由一组 `input_boolean` 表示：

- `input_boolean.bigmi_pack_elder_care_installed`
- `input_boolean.bigmi_pack_rental_host_installed`
- `input_boolean.bigmi_pack_quiet_night_installed`
- `input_boolean.bigmi_pack_workday_installed`
- `input_boolean.bigmi_pack_esports_installed`
- `input_boolean.bigmi_pack_cinema_installed`

安装数量由 `sensor.bigmi_installed_pack_count` 计算。

每个安装按钮调用一个 script，例如：

```text
script.bigmi_install_elder_care_pack
  -> input_boolean.bigmi_pack_elder_care_installed = on
  -> input_text.bigmi_marketplace_last_install 更新
  -> input_text.bigmi_last_runtime_action 更新
```

模板市场的底层证明来自两个方向：

- Home Assistant Blueprint：证明自动化模板可参数化、可复用。
- HACS 路径：证明第三方分发与社区插件生态存在现实基础。

当前项目中的 Blueprint 文件包括：

- `ha/blueprints/automation/bigmi/experience_mode.yaml`
- `ha/blueprints/automation/bigmi/programmable_scene_trigger.yaml`

### 6.4 商业价值

Marketplace 对 Bigmi 的商业意义很强：

- 对普通用户：不用写代码，安装模板即可获得复杂自动化。
- 对高阶用户：可以复用和调整模板，降低配置成本。
- 对开发者：可以发布自动化方案，未来形成模板销售或订阅收入。
- 对平台：Marketplace 带来网络效应和生态资产。

报告中可以把 Marketplace 写成 Bigmi 后期商业化的关键模块，包括：

- 模板销售抽成
- 开发者生态
- 垂直场景包
- B2B 场景交付

### 6.5 当前 PoC 边界

当前 Marketplace 是演示前台，不是真实商店系统。它没有实现：

- 用户账户
- 支付
- 评分
- 评论
- 版本更新
- 插件审核
- 真实远程下载

但它已经足够支撑商业计划书里的核心论点：Bigmi 可以把复杂自动化包装成可安装、可复用、可传播的场景包。

## 7. Bigmi Console -> Security

### 7.1 页面定位

`Security` 页面把安全从“隐藏在自动化里的技术细节”提升成一个产品模块。它对应 proposal 中的 `Safety & Permission Layer`。

页面文件位置：

- `ha/dashboards/bigmi-console.yaml`

核心配置位置：

- `ha/configuration.yaml`
- `ha/automations.yaml`
- `ha/scripts.yaml`
- `ha/packages/bigmi_demo.yaml`

### 7.2 页面组成

`Security` 页面包含：

- 顶部品牌视觉图：`/local/bigmi-security-stage.svg`
- `Bigmi Space Guard` alarm panel
- Guard Status：
  - High Privilege Guard
  - Unlock Pending
  - Manual Approval
  - Smart Lock Override
  - Latest Safety Action
- Safety Demo Controls：
  - Request Unlock
  - Approve Unlock
  - Trigger Breach
  - Arm Stay
  - Arm Away
  - Disarm

### 7.3 Space Guard

当前项目使用 Home Assistant manual alarm control panel 模拟 Bigmi 的空间安防状态：

```yaml
alarm_control_panel:
  - platform: manual
    name: Bigmi Space Guard
```

这使系统具备：

- disarmed
- armed_home
- armed_away
- armed_night
- triggered

这些状态足以在讲演里展示“安全态势”概念。

后续如果要接入 Alarmo，`Security` 页面可以继续沿用，只替换底层 alarm entity 和规则来源。

### 7.4 敏感操作审批流

当前已有二次确认链路：

```text
Request Unlock
  -> input_button.bigmi_request_sensitive_unlock
  -> automation bigmi_sensitive_unlock_request
  -> input_boolean.bigmi_sensitive_unlock_pending = on
  -> persistent notification
  -> Approve Unlock
  -> input_boolean.bigmi_admin_approval = on
  -> automation bigmi_sensitive_unlock_approval
  -> input_boolean.bigmi_smart_lock = on
```

这个流程展示了 high-privilege platform 的关键逻辑：

- 高风险动作不应被自动直接执行。
- 系统应将高风险动作排队。
- 管理员审批后才释放动作。
- 审批过程应有 trace 和审计字段。

### 7.5 Trace 与审计

相关 automations 都配置了：

```yaml
trace:
  stored_traces: 20
```

这意味着演示时可以打开 Home Assistant 的 trace 页面，展示彩色执行链路。报告中可以把它解释成 Bigmi 的“审计与可解释性能力”。

同时，系统会更新：

- `input_text.bigmi_last_runtime_action`
- `input_text.bigmi_last_program_payload`
- `sensor.bigmi_approval_queue`

这些字段构成演示级 audit feed。

### 7.6 商业价值

Security 模块支撑以下商业论点：

- Bigmi 是高权限平台，因此安全必须产品化。
- 控制门锁、摄像头、插座、安防设备需要比灯光更严格的权限。
- 对民宿、公寓、小办公室等小型空间运营者，安全审计和权限管理是购买理由。
- 对家庭用户，安全中心能降低“自动化失控”的心理门槛。

## 8. Bigmi Console -> Developer

### 8.1 页面定位

`Developer` 是后台技术证明页。它的目标不是给普通用户日常使用，而是给开发者、评委和投资人展示 Bigmi 的可编程深度。

页面文件位置：

- `ha/dashboards/bigmi-console.yaml`

### 8.2 页面组成

`Developer` 页面包含：

- 顶部品牌视觉图：`/local/bigmi-flow-stage.svg`
- 三个指标：
  - Entry Points
  - Template Packs
  - Active Modes
- Runtime Audit Feed：
  - Last Runtime Action
  - Last Runtime Channel
  - Last Program Payload
  - Runtime Status
  - Last Marketplace Install
- Trigger Matrix：
  - Fire Runtime Event
  - Run Blueprint Demo
  - Run Mode Webhook
  - Run House Webhook
- Visual Flow Studio：
  - Node-RED editor
  - AppDaemon admin
- Developer Timeline

### 8.3 编程入口

当前 Bigmi 提供五类编程入口：

- Dashboard action
- Python Runtime
- Blueprint
- Webhook / REST command
- Node-RED visual flow

`sensor.bigmi_programmable_entry_points` 当前设置为 5，用来在页面中直观表示 Bigmi 的可编程入口数量。

### 8.4 Python Runtime

`bigmi_runtime.py` 负责三种 experience mode：

- esports
- rental
- cinema

它监听：

- input_boolean 状态变化
- `bigmi_activate_scene` 自定义事件

它执行：

- 模式互斥
- 激活对应 script
- 更新 audit feed
- 发送 persistent notification

这部分说明 Bigmi 可以做常驻本地 runtime，而不仅是一次性自动化规则。

### 8.5 House Program Engine

`house_program_demo.py` 负责空间级 program：

- 使用 `ROOMS` 建模房间。
- 使用 `PROGRAMS` 定义场景。
- 使用事件 `bigmi_run_house_program` 触发程序。
- 使用 `run_in` 分步执行动作。
- 每一步写入 runtime audit。

这部分是 Bigmi “可编程空间对象”概念的技术核心。

### 8.6 Webhook

当前有两个 webhook surface：

- `bigmi_demo_scene`
- `bigmi_demo_house_program`

`bigmi_demo_scene` 用于触发 experience mode：

```text
POST /api/webhook/bigmi_demo_scene
```

`bigmi_demo_house_program` 用于触发 apartment program：

```text
POST /api/webhook/bigmi_demo_house_program
```

这说明 Bigmi 未来可以被外部系统调用，例如：

- 小程序
- 自研 App
- 物业系统
- 民宿 PMS
- 日历系统
- AI agent

### 8.7 Blueprint

Blueprint 的价值是模板化。当前 demo 中：

- `Bigmi Blueprint Programmable Rental Demo` 通过 Blueprint 发出标准事件。
- 事件进入 Python runtime。
- runtime 再决定如何切换场景。

这说明 Bigmi 的模板不是简单地复制 YAML，而是可以统一调用平台 runtime。

### 8.8 商业价值

Developer 页面支撑 Bigmi 对开发者的价值主张：

- 提供可编程入口。
- 提供可调试运行时。
- 支持模板化交付。
- 支持可视化流程。
- 支持外部系统集成。

在报告中，这部分适合放在：

- 技术架构章节
- 开发者生态章节
- 产品差异化章节
- 未来 SDK / API 扩展章节

## 9. Node-RED

### 9.1 定位

Node-RED 在当前项目中代表 Bigmi 的可视化规则编辑器。它补足了纯 Python Runtime 对非程序员不够直观的问题。

容器定义位置：

- `docker-compose.yml`

flow 文件位置：

- `nodered/data/flows.json`

访问地址：

```text
http://localhost:1880
```

### 9.2 当前 flow 内容

预置 tab 名为：

- `Bigmi Visual Rules`

包含四个主要 inject 节点：

- `Launch Rental Host Experience`
- `Launch Cinema Experience`
- `Owner Arrives Home Program`
- `Quiet Night Program`

它们分别调用两个 webhook：

- `http://homeassistant:8123/api/webhook/bigmi_demo_scene`
- `http://homeassistant:8123/api/webhook/bigmi_demo_house_program`

### 9.3 技术链路

Node-RED 到 Bigmi 的链路如下：

```text
Node-RED inject node
  -> HTTP request node
  -> Home Assistant webhook automation
  -> event bigmi_activate_scene or bigmi_run_house_program
  -> AppDaemon runtime
  -> Bigmi Console 状态更新
```

这条链路说明 Node-RED 不是孤立编辑器，而是 Bigmi 的又一个入口。

### 9.4 演示价值

Node-RED 最适合展示：

- 可视化流程编排
- 低代码自动化
- 复杂逻辑的图形化表达
- 开发者友好和高阶用户友好

对于最终报告，可以把它写成 Bigmi Studio 的一个模式：

- Code Mode：Python / future typed languages
- Visual Mode：Node-RED style flow editor
- Template Mode：Marketplace packs and Blueprints
- API Mode：Webhook / future SDK

### 9.5 商业价值

Node-RED 能帮助 Bigmi 讲清楚一个重要问题：

> Bigmi 面向程序员，但不只属于程序员。

它让平台同时覆盖：

- 专业开发者
- 智能家居发烧友
- 安装商
- 小型空间运营者
- 会配置但不想写完整代码的高阶用户

## 10. 与 Proposal 四模块的映射

### 10.1 Runtime / Hub

当前对应能力：

- Home Assistant 本地状态层
- AppDaemon runtime
- input_boolean / input_text 虚拟设备
- 自定义事件
- webhook
- 本地执行

证明点：

- Bigmi 可以做统一运行时。
- 多生态设备未来可以被收束到同一层。
- 场景执行不依赖云端。

### 10.2 Studio

当前对应能力：

- Python AppDaemon
- Developer Console
- Node-RED
- Webhook
- Blueprint
- runtime audit

证明点：

- Bigmi 可以给开发者提供多种编程入口。
- 同一套 runtime 可以被 UI、模板、API 和 flow 调用。

### 10.3 Marketplace

当前对应能力：

- Marketplace 页面
- Featured Packs
- 安装状态
- 安装脚本
- Blueprint
- HACS 路径

证明点：

- 普通用户可以消费开发者模板。
- 开发者模板可以被包装成场景包。
- 平台未来具备生态和抽成空间。

### 10.4 Safety & Permission

当前对应能力：

- Security Center
- Space Guard
- 二次审批
- Smart Lock Override
- Approval Queue
- trace
- audit feed

证明点：

- Bigmi 的高权限能力需要被安全产品化。
- 敏感设备需要独立授权和审计。
- 安全机制可以成为产品可信度的一部分。

## 11. 与六个关键词的映射

### 高权限

一个场景可以同时控制灯光、窗帘、空调、扫地机、热水器、门锁等设备状态。PoC 中通过 `Spaces` 和 `Security` 两个页面展示高权限编排和高风险审批。

### 可编程

核心可编程能力来自：

- `PROGRAMS` 结构化场景库
- `bigmi_activate_scene` 事件
- `bigmi_run_house_program` 事件
- Webhook
- Node-RED flow
- Blueprint

### 跨生态

当前通过 Xiaomi / Tuya / Matter 三个 bridge 状态模拟跨生态接入。虽然还没有真实设备，但已经能展示统一控制面的产品形态。

### 开发者友好

开发者可以修改 Python 脚本、触发 webhook、查看 runtime audit、使用 Node-RED 视觉 flow、复用 Blueprint 模板。

### 安全可控

Security Center 展示审批、alarm posture、Smart Lock Override、trace 和 audit feed。

### 模板市场

Marketplace 页面展示模板包安装、安装状态、场景启动和模板数量，支撑平台生态和商业化叙事。

## 12. 当前 PoC 的技术边界

为了避免最终报告过度承诺，建议明确以下边界：

- 当前设备是虚拟 helper，不是真实硬件。
- 当前 Marketplace 是前台壳，不是真实交易系统。
- 当前 Security Center 用 manual alarm panel 模拟安全态势，尚未完整接入 Alarmo。
- 当前跨生态是抽象展示，尚未接入真实 Xiaomi / Tuya / Matter 设备。
- 当前 Node-RED 通过 webhook 调用系统，尚未安装 Home Assistant websocket companion 节点。
- 当前开发者体验以 Python 为主，Java / TypeScript 仍是未来方向。

这些边界不削弱 PoC 价值，因为当前项目的目标是讲演和概念证明，而不是最终交付。

## 13. 最适合写进最终报告的论点

最终报告可以围绕以下论点组织：

- Bigmi 的核心不是控制设备，而是编排空间。
- Bigmi 把房子建模成可编程对象，把场景建模成可复用程序。
- Bigmi 通过 Marketplace 把开发者能力交付给普通用户。
- Bigmi 通过 Developer Console 证明它不是封闭 App，而是开放平台。
- Bigmi 通过 Security Center 处理高权限平台最关键的信任问题。
- Bigmi 可以先做软件平台，后续再扩展到真实设备、硬件 Hub、多空间管理和商业化 Marketplace。

## 14. 建议报告章节结构

最终报告可以按以下结构引用本项目：

1. 项目定位：Bigmi 是 programmable automation layer。
2. 用户痛点：生态割裂、自动化弱、开发者体验差、安全不透明。
3. 产品方案：Runtime / Studio / Marketplace / Safety。
4. PoC 实现：Bigmi Console 五个页面和 Node-RED。
5. 技术架构：本地事件总线、AppDaemon runtime、Webhook、Blueprint、Node-RED。
6. 场景展示：老人照护、节能、宠物、民宿、电竞、影音、夜间安静、居家办公。
7. 商业价值：开发者生态、模板市场、小型空间运营、订阅和 B2B。
8. 风险与边界：设备兼容、安全、用户门槛、生态依赖。
9. 未来路线：真实设备接入、强类型语言、真正 Marketplace、多空间管理。

## 15. 推荐讲演路径

建议演示顺序：

1. `Bigmi Console -> Home`
   展示产品前台和平台总览。

2. `Bigmi Console -> Spaces`
   展示空间程序库，重点点 `Owner Arrives Home`、`Rental Check-in`、`Quiet Night`。

3. `Bigmi Console -> Marketplace`
   展示安装模板包和启动模板包。

4. `Bigmi Console -> Security`
   展示 Space Guard、Request Unlock、Approve Unlock。

5. `Bigmi Console -> Developer`
   展示 Python Runtime、Blueprint、Webhook、Node-RED 都进入同一 runtime。

6. `Node-RED`
   打开 `http://localhost:1880`，点击一个 flow，回到 Bigmi Console 看状态变化。

这条路径的叙事节奏是：

```text
产品前台 -> 空间价值 -> 模板生态 -> 安全可信 -> 开发者能力 -> 可视化编程
```

它适合商业计划书答辩，也适合 PPT 录屏。
