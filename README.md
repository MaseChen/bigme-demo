# Bigmi Presentation PoC

这个仓库不是为了交付一个完整平台，而是为了把 Bigmi 讲成一个更像产品的东西。

**Bigmi 不是另一个智能家居控制 App，而是智能家居和小型智能空间的可编程自动化中间层。**

当前这套 PoC 以本地容器化环境为底座，但前台已经被重新包装成更适合讲演的 Bigmi 产品界面：

- `Runtime / Hub` -> 本地状态层与场景执行层
- `Studio` -> Python Runtime + Node-RED Visual Rules
- `Marketplace` -> Bigmi 风格的模板商店前台，后台继续复用 Blueprint / HACS 路径
- `Safety & Permission` -> Security Center + 审批流 + Trace

Proposal 对齐说明见：

- [docs/bigmi-proposal-alignment.md](docs/bigmi-proposal-alignment.md)
- [docs/bigmi-technical-report-reference.md](docs/bigmi-technical-report-reference.md)

## 六个关键词

整个 PoC 都围绕 proposal 里的六个关键词组织：

- `高权限`
- `可编程`
- `跨生态`
- `开发者友好`
- `安全可控`
- `模板市场`

## 为什么这里仍然使用容器化 HA

这套仓库仍然借用了 Home Assistant 生态做底层 PoC，因为它能最快提供：

- 本地运行时
- 事件总线
- 模板与自动化能力
- 仪表盘与 Trace

但当前迭代已经开始主动做两件事：

- `前台去 HA 化`
- `保留底层能力，重做产品叙事`

所以你现在看到的重点不是“HA 里有什么卡片”，而是：

- Bigmi 如何展示空间级程序
- Bigmi 如何展示模板市场
- Bigmi 如何展示安全控制
- Bigmi 如何展示开发者工作流

## 目录结构

```text
.
├── appdaemon/
│   └── conf/
│       ├── appdaemon.yaml
│       └── apps/
│           ├── apps.yaml
│           ├── bigmi_runtime.py
│           └── house_program_demo.py
├── docs/
│   ├── apartment-owner-arrival-demo.md
│   ├── bigmi-proposal-alignment.md
│   ├── hacs-and-xiaomi.md
│   └── programmable-demos.md
├── ha/
│   ├── automations.yaml
│   ├── blueprints/
│   ├── configuration.yaml
│   ├── dashboards/
│   │   └── bigmi-console.yaml
│   ├── packages/
│   │   └── bigmi_demo.yaml
│   ├── scripts.yaml
│   └── www/
├── nodered/
│   └── data/
│       └── flows.json
├── docker-compose.yml
└── Makefile
```

## 启动步骤

### 1. 启动主界面

```bash
cp .env.example .env
make up
```

首次启动后访问 `http://localhost:8123` 完成初始化。

### 2. 生成 Long-Lived Access Token

在 Home Assistant Web UI 中打开你的用户资料页，创建 `Long-Lived Access Token`，然后写入本地 `.env`：

```bash
HA_TOKEN=your-token-here
```

### 3. 启动开发者栈

```bash
make studio
```

这会拉起：

- AppDaemon：`http://localhost:5050`
- Node-RED：`http://localhost:1880`

如果你只想单独拉起可视化规则编辑器，也可以执行：

```bash
make flow
```

### 4. 修改配置后的重启规则

- 改 `ha/configuration.yaml` 或 `ha/packages/*` 后，重启 Home Assistant
- 改 `appdaemon/conf/apps/*` 后，重新启动 `make studio`
- 改 `nodered/data/flows.json` 后，重启 Node-RED 容器

## 当前前台结构

`Bigmi Console` 现在被拆成两层：

### 1. User Console

面向讲演和“产品前台”：

- `Home`
- `Spaces`
- `Marketplace`
- `Security`

这一层刻意弱化 raw telemetry 和 helper 细节，优先展示：

- 空间场景
- 模板安装
- 安全状态
- 可理解的模式入口

### 2. Developer Console

面向技术讲解和后台能力证明：

- runtime audit
- payload / channel
- webhook / blueprint / Python 触发矩阵
- Node-RED 入口
- 时间线与 trace 配套讲法

## 最值得展示的四个升级点

### Node-RED 作为可视化规则编辑器

仓库已经加入 `Node-RED` 容器与一份预置 flow：

- [nodered/data/flows.json](nodered/data/flows.json)

这份 flow 用本地 webhook 触发：

- `rental` 与 `cinema` experience mode
- `owner_arrives_home` 与 `quiet_night_mode` apartment program

这样你打开 `http://localhost:1880` 后，不会看到空白编辑器，而是直接能讲：

- Bigmi 不只支持 Python
- 也支持可视化的 flow programming

### Marketplace UI 外壳

`Bigmi Console -> Marketplace` 现在是 Bigmi 风格前台：

- Featured Packs
- Install Featured Packs
- Launch Installed Pack Demos

它的前台是产品壳，后台仍然复用：

- Blueprint
- HACS 路径

这非常适合讲“普通用户一键安装，开发者提供模板”。

### User / Developer 双层仪表盘

当前 PoC 已经不再把所有 debug 信息都暴露给用户前台。

- 用户前台负责“看起来像产品”
- 开发者后台负责“证明底层能力是真的”

这一步对降低 HA 既视感很重要。

### Security Center

`Bigmi Console -> Security` 现在提供：

- `Space Guard` alarm posture
- 高风险动作审批流
- 手动触发 breach 的演示入口
- 后续升级到 `Alarmo` 的清晰承载位

也就是说，现在的安全叙事已经不只是一个开锁 demo，而是一个完整的“安全中心”页面。

## 三类核心 Demo

### 1. Python Runtime Demo

入口：

- `Bigmi Console -> Developer -> Fire Runtime Event`

作用：

- 证明 Bigmi 有统一本地 runtime
- UI 不是直接控制设备，而是把事件交给可编程层

### 2. Blueprint / Marketplace Demo

入口：

- `Bigmi Console -> Developer -> Run Blueprint Demo`
- `Bigmi Console -> Marketplace`

作用：

- 证明模板分发与安装叙事成立
- 证明开发者交付物可以标准化

### 3. Webhook / Visual Flow Demo

入口：

- `Bigmi Console -> Developer -> Run Mode Webhook`
- `Bigmi Console -> Developer -> Run House Webhook`
- `http://localhost:1880`

作用：

- 证明 Bigmi 可被外部系统调用
- 证明 Node-RED 可以成为可视化规则编辑器

详细操作稿见：

- [docs/programmable-demos.md](docs/programmable-demos.md)

## 实际应用场景 Demo

仓库内置了一套“智能公寓”空间程序库：

- `Owner Arrives Home`
- `Elder Care`
- `Energy Saver`
- `Pet Mode`
- `Rental Check-in`
- `Esports Room`
- `Cinema Room`
- `Quiet Night`
- `Work From Home`

入口位置：

- `Bigmi Console -> Spaces`

核心脚本：

- [house_program_demo.py](appdaemon/conf/apps/house_program_demo.py)

说明文档：

- [docs/apartment-owner-arrival-demo.md](docs/apartment-owner-arrival-demo.md)

## Proposal 关键词如何映射到当前 PoC

### 高权限

- 一个场景会影响多个房间和多台设备
- `Spaces` 页展示空间级程序
- `Security` 页展示高风险审批和 alarm posture

### 可编程

- Python Runtime
- Webhook
- Blueprint
- Node-RED Visual Rules

### 跨生态

- 当前仍用 Xiaomi / Tuya / Matter bridge 状态做抽象
- 重点是先讲统一编排层，而不是设备数量

### 开发者友好

- Python 脚本结构清晰
- Node-RED 预置 flow 可直接演示
- Developer Console 把调试能力收拢到一处

### 安全可控

- 高风险动作审批
- `Space Guard`
- runtime audit
- automation trace

### 模板市场

- Marketplace UI 外壳
- Blueprint 作为最小分发形态
- HACS 作为后续扩展分发渠道

## 建议的 PPT 取景顺序

1. `Bigmi Console -> Home`
先讲“这看起来已经不是 Home Assistant 的默认控制台了”。

2. `Bigmi Console -> Spaces`
展示空间程序和八种场景库。

3. `Bigmi Console -> Marketplace`
讲模板市场与一键安装。

4. `Bigmi Console -> Security`
讲高权限、安全可控、审批和 alarm posture。

5. `Bigmi Console -> Developer`
最后再揭示 Python runtime、Webhook、Blueprint、Node-RED 都汇总到同一个本地运行时。

## 当前最重要的手动提醒

- 第一次加载这些升级后的页面前，先重启 Home Assistant
- 如果 Developer Console 里的动作不响应，重新跑一次 `make studio`
- 如果要演示 Node-RED，打开 `http://localhost:1880` 确认 flow 已加载
- `.env` 里有 token，录屏时不要展示终端里的敏感环境变量
