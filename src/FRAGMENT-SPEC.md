# 页面 fragment 写作规范（两个写作 agent 共用）

每个页面 = src/content/{slug}.html 一个 HTML 片段（不含 <html>/<head>/<body>，会被 build.py 包进 layout）。

## 结构（普通攻略页）
<h1>页面主标题（含目标关键词，自然表达）</h1>
<p class="updated">Last updated {{UPDATED}} · Based on version 1.0 and community sources — items marked “TBC” are awaiting verification.</p>
<p>开头 2-4 句：直接回答该页关键词对应的核心问题（用户 10 秒拿到答案）。</p>
<h2>…（3-6 个 H2 分节，每节 2-5 段或表格/列表）</h2>
…
<div class="related"><b>Related guides:</b> <a href="/guides/xxx/">Xxx</a> · <a href="/guides/yyy/">Yyy</a></div>

## 硬规则
1. 事实只能来自 research/sources/ 对应素材文件；素材里标"待确认/单源"的信息要么不写，要么写出并标 <span class="tbc">(TBC)</span>
2. 数值类信息注明版本背景（如 "reported during Early Access, may differ in 1.0"）
3. 禁止编造：数值、兑换码、角色喜好、日期。素材没有=不写
4. 每页正文 700-1300 词英文（codes/platforms 这类可短至 400-600）；表格优先于长段落
5. title 40-60 字符含关键词；description 140-160 字符——写进 pages 的 JSON，不写在 fragment 里
6. 只有一个 H1；H2 分节；层级正确
7. 相关链接 2-3 个，指向真实存在的站内页面（页面清单见下）
8. 兑换码页特殊：如实写"截至 2026-08-25 官方未发放过任何公开兑换码 + Redeem Gift 系统存在 + 警惕假码站"，这就是页面价值

## 站内页面清单（可互链）
/ /guides/ /guides/beginner-guide/ /guides/characters/ /guides/gift-guide/ /guides/romance/ /guides/make-money/ /guides/fishing/ /guides/farm-layout/ /guides/gift-codes/ /guides/platforms/ /guides/review/

## pages JSON 条目格式（每个 agent 交付自己负责页面的 JSON 数组文件）
[{"url":"/guides/xxx/","fragment":"xxx.html","crumb":"Xxx","title":"…","description":"…"}]
