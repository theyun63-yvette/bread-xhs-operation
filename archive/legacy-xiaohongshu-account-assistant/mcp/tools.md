# MCP 工具接口约定

这份文件定义 MCP 服务向大模型提供的最小工具集合。工具只读取 GitHub 仓库中的 Markdown，不默认修改仓库。

## `get_account_memory`

读取 `memory/account-memory.md`，用于恢复账号长期背景、定位、受众和历史资产。

参数：无。

## `get_content_strategy`

读取 `memory/content-strategy.md`，用于判断栏目、标题、内容结构和复盘指标。

参数：无。

## `get_brand_safety`

读取 `memory/brand-safety.md`，用于检查隐私、商业化、职场和赚钱内容风险。

参数：无。

## `get_current_phase`

读取 `memory/current-phase.md`，用于获得当前人生阶段、内容优先级和待验证假设。

参数：无。

## `search_account_memory`

在所有 Markdown 记忆和运营文件中按关键词搜索，返回匹配文件、段落标题和相关文本。

参数：

```json
{
  "query": "深圳实习 开销"
}
```

## `get_recent_experiments`

读取 `operations/experiment-log.md` 或仓库中最近的复盘记录，用于判断哪些内容假设已经验证。

参数：

```json
{
  "limit": 10
}
```

## `propose_memory_update`

生成记忆文档的修改建议，但不直接提交 GitHub。需要用户确认后，才允许通过另一个明确的写入流程修改仓库。

参数：

```json
{
  "file": "memory/current-phase.md",
  "reason": "深圳实习第一周已经完成",
  "proposed_changes": "..."
}
```

## 调用原则

1. 生成选题、标题或正文前，至少读取账号记忆、内容策略和当前阶段。
2. 涉及收入、公司、客户、合作或职场时，额外读取安全边界。
3. 发现记忆文档之间冲突时，报告冲突，不自行覆盖。
4. MCP 默认只读，避免模型未经确认改变长期策略。

