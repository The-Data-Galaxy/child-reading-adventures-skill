# v0.1.0 开源发布检查表

## 核心与范围

- [x] `INTAKE.md`、`SKILL.md`、`EVAL.md`、`TESTS.md`、`CHANGELOG.md` 与 `benchmark/` 存在。
- [x] README 说明用途、适用场景、非目标、限制与反馈方式。
- [x] 公开包不改变已接受的 Skill 目的、输出契约或 benchmark criteria。

## 验证

- [x] 固定 smoke benchmark 与 baseline 报告存在。
- [x] 页码、成人／儿童分离、阅读依赖与开放玩法定向回归存在。
- [x] 真实 DOCX/PDF 双文件渲染检查完成；产物不公开。
- [x] 公开包结构、合同、治理、manifest、安装与链接检查通过。

## 公共安全

- [x] 不含真实儿童身份、照片、声音、私人阅读记录或用户产物。
- [x] 不含图书正文、未经授权副本或大段引文。
- [x] 不含凭证、`.env`、私钥、客户材料或本地安装副本。
- [x] README 明确儿童隐私、版权、安全与非保证边界。
- [x] Apache-2.0 许可证存在。

## 发布

- [ ] canonical worktree 位于 `open-source/child-reading-adventures-skill/`。
- [ ] origin、仓库注册、共享 hooks 与 GitHub gate 正确。
- [ ] dry run、apply、repository gate、commit 与 push 完成。
