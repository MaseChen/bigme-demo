# HACS 与 Xiaomi 接入说明

## HACS 在这个 PoC 里的角色

Bigmi 的 `Marketplace` 模块，在这次 PoC 里用两部分来模拟：

- Home Assistant Blueprints：展示“一键导入模板”
- HACS：展示“社区商店 / 扩展分发渠道”

由于当前仓库采用的是 `Home Assistant Container`，不是 Home Assistant OS，所以这里不走 add-on 方式，而是按 HACS 官方文档在现有 HA 实例里安装。

## 建议安装顺序

1. 先把本仓库的 Home Assistant 跑起来。
2. 在 HA Web UI 中完成初始配置。
3. 按 HACS 官方文档安装 HACS。
4. 在 HACS 中搜索并安装 `Xiaomi Miot`。

## Xiaomi Miot 方案建议

如果你的目标是尽快做演示和截图，优先建议：

- `al-one/hass-xiaomi-miot`

这个集成支持通过 HACS 安装，适合把米家设备快速映射进 HA。  
如果后面要强调“小米官方对接”路线，也可以对比研究：

- `XiaoMi/ha_xiaomi_home`

## 这一步接到 Bigmi 叙事里的方式

- HACS -> Bigmi Marketplace 的“开发者分发渠道”
- Xiaomi Miot -> Bigmi Runtime / Hub 的“米家生态接入”
- Blueprint -> Bigmi 模板市场的“一键安装体验”

## 你完成安装后，建议优先录的三个画面

1. HACS 集成页里看到 `Xiaomi Miot`
2. HA 设备页里出现真实米家设备实体
3. 基于 Blueprint 或 AppDaemon 对这些实体执行自动化
