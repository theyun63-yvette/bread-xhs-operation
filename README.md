# bread xhs operation

「cos面包大人」的小红书运营资料与带记忆 Skill。私有仓库，包含个人经历、偏好、文风、对标分析和作品进度。

## 从这里开始

当前使用的技能入口是 [面包的小红书运营助手](skills/mianbao-xiaohongshu/SKILL.md)。先读 [账号与偏好](skills/mianbao-xiaohongshu/memory/profile.md) 和 [最新进度](skills/mianbao-xiaohongshu/memory/current.md)，再按任务读相关案例与参考。

- [文风与编辑方法](skills/mianbao-xiaohongshu/references/voice.md)
- [九图回归篇成稿](skills/mianbao-xiaohongshu/references/return-post.md)
- [九位参考博主](skills/mianbao-xiaohongshu/references/creators.md)
- [共识修正记录](skills/mianbao-xiaohongshu/memory/decisions.md)

## 换模型或平台

支持 Agent Skills 的平台可以使用 skills/mianbao-xiaohongshu 整个目录，或 [技能压缩包](exports/mianbao-xiaohongshu.zip)。普通聊天平台可上传 [跨平台单文件记忆](exports/面包账号记忆-跨平台.md)，要求先读取记忆再继续讨论。

仅给模型一个私有仓库链接，不保证它有访问权限。平台需要实际读取文件。没有写文件能力时，让模型输出本轮记忆增量，由用户保存。

## 资料结构

- skills/mianbao-xiaohongshu：当前有效的技能、记忆、文风、案例和导出脚本。
- exports：用于迁移的完整zip和单文件Markdown快照。
- archive：此前的完整讨论归纳、语雀保存证明、早期运营及MCP草案。
- manifest.sha256：本次全部文件的校验清单，不包含清单自身。

历史资料保留原文以便回溯，其中固定栏目比例、转型声明、音乐合辑精简等旧建议可能已被后续讨论取代。当前用户说明与技能内最新记忆优先，不能把 archive 中的旧建议自动当成现行规则。

## 更新与导出

日常修改技能目录里的记忆；导出快照和GitHub内容不会自动随聊天同步。将新成果提交到仓库后，其他平台仍需重新读取最新版本。

在仓库目录中运行：

```bash
python3 skills/mianbao-xiaohongshu/scripts/export_portable.py --output-dir exports --as-of YYYY-MM-DD
```

日期使用用户当天日期。导出不会核验发布状态，也不会修改既有事实。归档的MCP文件是接口和配置草案，没有部署远程服务或配置访问凭据。

本次归档：2026-11-02。回归篇是否实际发布仍以用户后续确认或可核验结果为准。
