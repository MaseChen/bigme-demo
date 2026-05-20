# Bigmi 可编程 Demo 操作稿

这份文档只覆盖三条速成 demo：

- Python Runtime Demo
- Blueprint Marketplace Demo
- Webhook / API Demo

这三条 demo 对应 proposal 中的三个重点属性：

- `可编程`
- `开发者友好`
- `模板市场`

它们共同证明的不是“系统里有三个按钮”，而是：

**Bigmi 可以把不同来源的触发统一收束到同一个本地运行时中。**

## 1. Python Runtime Demo

目标：证明 Bigmi 可以作为“代码驱动的自动化中间层”。

操作步骤：

1. 打开 `Bigmi Console -> Studio`
2. 点击 `Fire Runtime Event`
3. 观察：
   - 模式被切换
   - `Last Runtime Action` 更新
   - `Last Runtime Channel` 变成 `event:dashboard-event`
   - AppDaemon 日志出现自定义事件处理记录

建议录屏画面：

- Lovelace `Studio` 页
- `docker compose logs -f appdaemon`

建议讲法：

- 这不是普通 UI 按钮直接控制设备
- 按钮只是触发入口，真正的逻辑在 Python runtime 里
- 这意味着高阶用户可以把简单规则升级成复杂程序

## 2. Blueprint Marketplace Demo

目标：证明开发者写一次模板，普通用户可以复用。

仓库中的模板：

- `ha/blueprints/automation/bigmi/programmable_scene_trigger.yaml`

已预装的 demo automation：

- `Bigmi Blueprint Programmable Rental Demo`

操作步骤：

1. 打开 `Bigmi Console -> Studio`
2. 点击 `Run Blueprint Demo`
3. 观察：
   - `rental` 模式被激活
   - `Last Runtime Channel` 变成 `event:blueprint-marketplace`
   - 在 `Settings -> Automations & scenes -> Automations` 中打开该自动化的 `Trace`

建议讲法：

- 这个模板不直接控制设备，而是把标准化事件发给 Bigmi Runtime
- 说明 Bigmi Marketplace 的核心不是“规则碎片”，而是“可复用的自动化接口”
- 这也说明 Bigmi 可以把“开发者交付物”标准化，而不是要求用户理解底层代码

## 3. Webhook / API Demo

目标：证明 Bigmi 可以被外部程序调用，而不仅是 Home Assistant UI 内部按钮。

### 方式 A：Studio 页面一键触发

1. 打开 `Bigmi Console -> Studio`
2. 点击 `Run Webhook Demo`
3. 观察：
   - `cinema` 模式激活
   - `Last Runtime Channel` 变成 `event:ha-rest-command`
   - 打开 `Bigmi Webhook Programming Surface` 的 `Trace`

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

- `Last Program Payload` 会记录 mode、source、note
- `Last Runtime Channel` 会变成 `event:curl`
- AppDaemon 会把这个外部调用统一编排进场景运行时

建议讲法：

- Bigmi 不只是一个界面，而是一个可被程序调用的平台能力
- 这为后续 SDK、第三方集成、B2B 对接留下了产品空间

## 一句总结

这三条 demo 共用一条运行链路：

`Dashboard / Blueprint / Webhook -> Home Assistant Event -> Bigmi Python Runtime -> 模式编排 / 日志 / Trace`

这正是 Bigmi 作为 programmable automation layer 的最小可见形态。

如果在 PPT 中只保留一句话，推荐：

> Bigmi unifies templates, UI actions, and external APIs into one programmable local runtime.
