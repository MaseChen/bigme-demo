# Bigmi 可编程 Demo 操作稿

这份文档覆盖当前最适合讲演的四条可编程入口：

- Python Runtime
- Blueprint Marketplace
- Webhook / API
- Node-RED Visual Rules

它们共同证明的不是“系统里有几个触发按钮”，而是：

**Bigmi 可以把模板、UI、可视化流程和外部 API 统一收束到同一个本地运行时中。**

## 1. Python Runtime Demo

目标：证明 Bigmi 可以作为“代码驱动的自动化中间层”。

操作步骤：

1. 打开 `Bigmi Console -> Developer`
2. 点击 `Fire Runtime Event`
3. 观察：
   - 模式被切换
   - `Last Runtime Action` 更新
   - `Last Runtime Channel` 变成 `event:dashboard-event`
   - AppDaemon 日志出现自定义事件处理记录

建议录屏画面：

- `Bigmi Console -> Developer`
- `docker compose logs -f appdaemon`

建议讲法：

- 按钮只是入口，真正逻辑在 Python runtime
- 所有触发最终都回到同一条场景运行链路
- 这让 Bigmi 更像一个 automation layer，而不是一个遥控器页面

## 2. Blueprint Marketplace Demo

目标：证明开发者写一次模板，普通用户可以复用。

模板文件：

- `ha/blueprints/automation/bigmi/programmable_scene_trigger.yaml`

已预装 demo automation：

- `Bigmi Blueprint Programmable Rental Demo`

操作步骤：

1. 打开 `Bigmi Console -> Developer`
2. 点击 `Run Blueprint Demo`
3. 观察：
   - `rental` 模式被激活
   - `Last Runtime Channel` 变成 `event:blueprint-marketplace`
   - 然后切到 `Bigmi Console -> Marketplace` 讲“这是 Bigmi 的模板前台壳”

建议讲法：

- 开发者不是直接交付一个硬编码规则
- 开发者交付的是一个标准化、可复用、可安装的自动化接口
- Marketplace 前台可以 Bigmi 化，底层继续复用 Blueprint / HACS

## 3. Webhook / API Demo

目标：证明 Bigmi 可以被外部程序调用，而不只是被 UI 按钮触发。

### 方式 A：Developer 页面一键触发

1. 打开 `Bigmi Console -> Developer`
2. 点击 `Run Mode Webhook`
3. 观察：
   - `cinema` 模式激活
   - `Last Runtime Channel` 变成 `event:ha-rest-command`
   - trace 可在稍后单独展示

### 方式 B：终端 curl 触发

```bash
curl -X POST http://localhost:8123/api/webhook/bigmi_demo_scene \
  -H "Content-Type: application/json" \
  -d '{"mode":"rental","source":"curl","note":"External API demo"}'
```

Windows PowerShell 可改用：

```powershell
Invoke-RestMethod -Method Post -Uri "http://localhost:8123/api/webhook/bigmi_demo_scene" -ContentType "application/json" -Body '{"mode":"rental","source":"powershell","note":"External API demo"}'
```

观察点：

- `Last Program Payload` 记录 mode、source、note
- `Last Runtime Channel` 变成 `event:curl`
- AppDaemon 统一接管这个外部调用

建议讲法：

- Bigmi 不只是一个界面
- Bigmi 还是一个可被程序调用的平台能力

## 4. Node-RED Visual Rules Demo

目标：证明 Bigmi 不只对写代码的用户友好，也支持可视化流程编排。

操作步骤：

1. 执行 `make studio`
2. 打开 `http://localhost:1880`
3. 观察预置 flow：
   - `Launch Rental Host Experience`
   - `Launch Cinema Experience`
   - `Owner Arrives Home Program`
   - `Quiet Night Program`
4. 点击任意 inject 节点
5. 回到 `Bigmi Console -> Developer` 或 `Spaces` 看状态变化

建议讲法：

- Node-RED 不是另一套孤立逻辑
- 它只是 Bigmi 的又一个编程入口
- Python、Blueprint、Webhook、Node-RED 最终共用一个 runtime

## 一句总结

当前四条入口共用一条运行链路：

`User Console / Developer Console / Blueprint / Webhook / Node-RED -> Home Assistant Event or Webhook -> Bigmi Runtime -> 模式编排 / 日志 / Trace`

如果在 PPT 里只保留一句话，推荐：

> Bigmi unifies templates, visual flows, UI actions, and external APIs into one programmable local runtime.
