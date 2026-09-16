# tgbot-ops

**小o机器人**（https://tgcfym.us.ci）的运营仓库 —— GitHub 免费资源作业面。

主仓库 `tgcfym/tgbot` 是**私有**的（2,000 分钟/月），本仓库**公开**，因此吃满
GitHub Actions 公有仓库的**无限免费分钟数**。

| 用途 | 文件 | 官方免费额度 |
|---|---|---|
| 健康探测（每 15 分钟） | `.github/workflows/health.yml` | 公有仓库 = 无限分钟 |
| 镜像发布到 ghcr.io | `.github/workflows/docker.yml` + `Dockerfile` | 公开包免费 |
| 静态页（GitHub Pages） | `docs/index.html` | 1 GB 站点 / 100 GB 月带宽 |
| 云端开发环境 | `.devcontainer/devcontainer.json` | 120 hrs/月 |

## 60 天保活（关键）

GitHub 会在仓库**连续 60 天无活动**后**自动停用定时工作流** —— 这是免费算力最常见的静默失效原因。
本仓库每月 1 号自动提交一次 `status/last-alive.txt`，让定时探测永久有效。

## 安全

本仓库**不含任何密钥**、不含主仓库源码。
探测只访问公开端点 `/health` 与 `/api/stats` —— 不消耗任何 AI 配额。
