# 安装说明

版本：`v0.1.1`

## 安装到 Codex

将发布包中的 `design-child-reading-adventures/` 目录复制到：

```text
~/.codex/skills/design-child-reading-adventures/
```

刷新或重启 Codex，使 Skill 列表重新加载。

## Smoke Prompt

```text
请使用 design-child-reading-adventures，为一本儿童读物设计3个阅读游戏。
孩子8岁，喜欢推理；目前只提供书名和出版社。不要编造人物、情节、引文或原书页码，并说明还需要什么材料才能做得更具体。
```

预期行为：选择 `ideas` 模式；声明有限证据；不生成完整手册；不编造书中细节；说明版权页、目录或相关节选能解锁更具体设计。

## 卸载与回退

删除或移走 `~/.codex/skills/design-child-reading-adventures/`，再刷新 Codex。升级前可备份旧目录，以便直接恢复。
