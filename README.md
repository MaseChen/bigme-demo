# Bigmi Home Assistant PoC

这个仓库不是为了证明“Home Assistant 可以做自动化”，而是为了证明 Bigmi 的核心命题：

**Bigmi 不是另一个智能家居控制 App，而是智能家居和小型智能空间的可编程自动化中间层。**

当前仓库把 Bigmi 的四个核心模块，映射成一套可以本地快速启动、截图、录动图、讲解商业计划书的 Home Assistant PoC：

- `Runtime / Hub` -> Home Assistant Container
- `Studio` -> AppDaemon Python 应用
- `Marketplace` -> Blueprint + HACS 安装路径
- `Safety & Permission` -> Automation Trace + 二次审批流

Proposal 对齐说明见：

- [docs/bigmi-proposal-alignment.md](docs/bigmi-proposal-alignment.md)

## 六个关键词

整个 PoC 的文档和演示都围绕 proposal 中的六个关键词组织：

- `高权限`
- `可编程`
- `跨生态`
- `开发者友好`
- `安全可控`
- `模板市场`

讲演时，建议始终把这些词和具体画面绑在一起，而不是只讲抽象概念。

## 为什么这里用容器化 HA

Home Assistant 官方当前仍然把 macOS 的推荐安装方式指向虚拟机里的 Home Assistant OS；同时官方文档也保留了 `Home Assistant Container` 作为可自行编排的安装类型。为了在这台 M2 MacBook Air 上更快做 Bigmi 商业计划书的 PoC 和演示截图，这个仓库采用 Docker Desktop 跑 `Home Assistant Container`，而不是完整 HA OS。

这意味着：

- 好处是启动快、目录清晰、适合做概念验证。
- 代价是没有 HA OS 的 add-ons 和一键管理能力。
- 所以 `Studio` 这里不依赖 add-on，而是用独立容器跑 AppDaemon。

## 目录结构

```text
.
├── appdaemon/
│   └── conf/
│       ├── appdaemon.yaml
│       └── apps/
│           ├── apps.yaml
│           └── bigmi_runtime.py
├── docs/
│   ├── bigmi-proposal-alignment.md
│   ├── apartment-owner-arrival-demo.md
│   ├── hacs-and-xiaomi.md
│   └── programmable-demos.md
├── ha/
│   ├── automations.yaml
│   ├── blueprints/
│   │   └── automation/
│   │       └── bigmi/
│   │           └── experience_mode.yaml
│   ├── configuration.yaml
│   ├── dashboards/
│   │   └── bigmi-console.yaml
│   ├── packages/
│   │   └── bigmi_demo.yaml
│   ├── scenes.yaml
│   ├── scripts.yaml
│   └── www/
│       └── bigmi-stage.svg
├── .env.example
├── docker-compose.yml
└── Makefile
```

## 启动步骤

### Windows 兼容性说明

这个 PoC 的核心运行方式是 `Docker Desktop + docker compose`，这部分在 Windows 上可行。  
但仓库里默认展示的 `make`、`cp`、多行 `curl` 命令更偏 Bash/macOS/Linux，需要在 Windows 上换成等价命令，或者在 Git Bash / WSL 中执行。

### 1. 启动 Home Assistant

```bash
cp .env.example .env
make up
```

Windows PowerShell 可改用：

```powershell
Copy-Item .env.example .env
docker compose up -d homeassistant
```

首次启动后，访问 `http://localhost:8123` 完成 Home Assistant 初始化。

如果你是在已有 HA 容器基础上追加这套配置，而不是第一次启动，修改完 `configuration.yaml` 后需要重启 Home Assistant，侧边栏里的 `Bigmi Console` 才会出现。

### 2. 生成 Long-Lived Access Token

在 Home Assistant Web UI 中：

1. 右下角进入你的用户资料页。
2. 在 `Long-Lived Access Tokens` 区域创建一个 token。
3. 把它写进本地 `.env`：

```bash
HA_TOKEN=your-token-here
```

### 3. 启动 AppDaemon Studio 容器

```bash
make studio
```

Windows PowerShell 可改用：

```powershell
docker compose --profile studio up -d
```

启动后你可以：

- 打开 Home Assistant：`http://localhost:8123`
- 打开 AppDaemon 管理页面：`http://localhost:5050`
- 用 `docker compose logs -f appdaemon` 录制 Python 自动化日志画面

## 三个速成可编程 Demo

仓库已经内置三条能快速体现 Bigmi 编程潜力的 demo。  
这三条 demo 不是彼此独立的小把戏，而是共同证明：

- Bigmi 有统一 runtime
- Bigmi 能接收不同编程入口
- Bigmi 能把模板、UI、API 汇总到同一条执行链路

1. `Python Runtime Demo`
在 `Bigmi Console -> Studio` 点击 `Fire Runtime Event`，自定义事件会进入 AppDaemon runtime 并驱动模式切换。

2. `Blueprint Marketplace Demo`
点击 `Run Blueprint Demo`，一个 Marketplace 风格的 blueprint automation 会把标准事件发给 Bigmi runtime。

3. `Webhook / API Demo`
点击 `Run Webhook Demo`，或直接执行：

```bash
curl -X POST http://localhost:8123/api/webhook/bigmi_demo_scene \
  -H "Content-Type: application/json" \
  -d '{"mode":"rental","source":"curl","note":"External API demo"}'
```

Windows PowerShell 可改用：

```powershell
Invoke-RestMethod -Method Post -Uri "http://localhost:8123/api/webhook/bigmi_demo_scene" -ContentType "application/json" -Body '{"mode":"rental","source":"powershell","note":"External API demo"}'
```

详细操作稿见：

- [docs/programmable-demos.md](docs/programmable-demos.md)

## 实际应用场景 Demo

仓库还内置了一套更接近真实业务叙事的 `智能公寓` 场景。  
它的重点不是“多几个虚拟设备”，而是把“房子”抽象成一个可编程对象，把不同生活与运营模式抽象成可维护、可复用的空间程序。

- 六个空间加一个支持系统层：玄关、客厅、厨房、卧室、浴室、书房、Support Systems
- 一个场景库：`Owner Arrives Home`
- 八个扩展场景：`Elder Care`、`Energy Saver`、`Pet Mode`、`Rental Check-in`、`Esports Room`、`Cinema Room`、`Quiet Night`、`Work From Home`
- 一个复位程序：`Reset Apartment`

入口位置：

- `Bigmi Console -> Apartment`

编程脚本位置：

- [house_program_demo.py](appdaemon/conf/apps/house_program_demo.py)

说明文档：

- [docs/apartment-owner-arrival-demo.md](docs/apartment-owner-arrival-demo.md)

## Proposal 关键词如何落地到当前 PoC

### 高权限

- 一个动作会影响多个房间和多台设备
- `Owner Arrives Home` 会同时操作灯光、窗帘、空调、扫地机、热水器
- `Safety Lab` 则展示高风险动作的审批流

### 可编程

- Python Runtime：房间和程序被写成结构化代码
- Blueprint：自动化能力可参数化复用
- Webhook/API：外部系统可直接触发程序

### 跨生态

- 当前用 Xiaomi / Tuya / Matter 三个 bridge 状态做抽象
- 目的是先证明“统一编排层”，后续再换成真实设备

### 开发者友好

- 关键逻辑集中在少量清晰文件里
- AppDaemon 脚本比零散规则更像真实工程
- Trace、日志、Lovelace 演示页都适合作为调试入口

### 安全可控

- 敏感动作需要二次确认
- 所有演示链路都有审计字段和 trace
- 当前 PoC 强调本地运行而不是云端黑盒

### 模板市场

- Blueprint 是 Marketplace 的最小可见形态
- 当前 demo 先证明“开发者写模板，用户安装模板”这件事成立

## 演示映射

### 1. Runtime / Hub

HA 启动后，在仪表盘和实体页里你会看到一组虚拟的 Bigmi 设备与模式开关，用来模拟：

- Xiaomi 生态接入
- Tuya 生态接入
- Matter 生态接入
- 电竞房 / 民宿 / 影音室 三种场景

这些实体由 `ha/packages/bigmi_demo.yaml` 定义，便于后续换成真实设备。

### 2. Studio

`appdaemon/conf/apps/bigmi_runtime.py` 是这次的核心 PoC 文件。它用 Python 类监听模式切换，并调用 HA 服务来：

- 互斥切换模式
- 更新运行状态
- 触发脚本
- 产生日志和通知

而 [house_program_demo.py](appdaemon/conf/apps/house_program_demo.py) 则进一步展示：

- 房间可以被抽象成结构化对象
- 程序可以被抽象成步骤列表
- 高阶用户可以直接改步骤顺序、房间映射和设备行为
- 同一套 apartment model 可以支持照护、节能、宠物、民宿、电竞、影音、夜间安静、居家办公等不同模式

这正好对应 Bigmi 的“开发者可编程自动化层”定位。

### 3. Marketplace

仓库内已经放入一个可导入的 Blueprint：

- `ha/blueprints/automation/bigmi/experience_mode.yaml`

它可以在 HA UI 中被重复实例化，适合演示“模板市场 / 一键导入自动化”。  
HACS 与 Xiaomi Miot 的接入说明见：

- [docs/hacs-and-xiaomi.md](docs/hacs-and-xiaomi.md)

### 4. Safety & Permission

`ha/automations.yaml` 里预置了敏感设备二次审批流：

- 用户请求敏感开锁
- 系统标记待审批
- 管理员确认后才真正执行

每条自动化都配置了 `trace.stored_traces`，方便你在 HA 里打开彩色 Trace 视图做 PPT 截图。

## 建议的 PPT 取景顺序

1. `Bigmi Console -> Apartment`
先讲真实空间程序和场景库，最能直观体现“可编程”和“高权限”。

2. `Bigmi Console -> Studio`
再讲统一 runtime、Blueprint 和 Webhook 三种编程入口。

3. `Settings -> Automations & scenes`
展示 Blueprint 和自动化实例，突出模板市场。

4. `Trace` 页面
点开 `Bigmi Webhook Programming Surface`、`Bigmi Blueprint Programmable Rental Demo` 或安全审批自动化，展示完整执行链路。

5. AppDaemon 日志
录制 Python runtime 日志，讲开发者体验和本地执行能力。

6. `Settings -> Devices & services -> Entities`
最后再补 Xiaomi / Tuya / Matter 三组虚拟接入能力，讲跨生态。

## 后续最值得继续做的两步

1. 通过 HACS 安装 `Xiaomi Miot`，把现在的虚拟实体替换成真实米家设备。
2. 加一个专门面向投资人演示的 Lovelace 页面，把商业价值、Trace 截图入口和真实设备状态做成更强叙事的“Roadshow Dashboard”。
