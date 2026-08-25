# 10 - 评价类素材（Starsand Island 星砂岛）

> 抓取日期：2026-08-25。铁律遵守：以下所有事实均来自实际访问的来源，逐条标注来源编号；引用评论为如实摘录/摘译（标注原文语言）；未找到的内容在缺口清单中如实标注。

## 页面目标关键词

- 星砂岛 评价 / Starsand Island 好评率 / 星砂岛 值得买吗
- Starsand Island Steam 评测 / 差评 / review
- 星砂岛 争议 / AI 争议 / 水军刷好评 / controversy
- Starsand Island Metacritic / OpenCritic 评分

## 来源清单

1. **Steam 评价统计 API**（官方一手数据）
   - 全语言汇总：https://store.steampowered.com/appreviews/2966320?json=1&language=all&purchase_type=all&num_per_page=0
   - 简中子集：https://store.steampowered.com/appreviews/2966320?json=1&language=schinese&purchase_type=all&num_per_page=0
   - 提供：好评率、总评论数、评分档位（appid 2966320）
2. **Steam 评论区（appreviews API，按有用数排序的真实评论）**
   - 英文好评/差评、简中好评/差评各若干条，同一 API（review_type=positive/negative, language=english/schinese）
   - 单条评论可定位：https://steamcommunity.com/app/2966320/reviews/ 内按 recommendationid（下文每条附 id）
3. **Steam 商店 appdetails API**：https://store.steampowered.com/api/appdetails?appids=2966320
   - 提供：发售日、开发商/发行商官方名称
4. **Reddit r/CozyGamers controversy 帖**（CDP 实际访问 old.reddit.com 读取）
   - https://old.reddit.com/r/CozyGamers/comments/1r2r2ou/the_emerging_starsand_island_controversy_what_is/
   - 提供：争议帖标题、正文、高赞评论原文
5. **Metacritic PC 版媒体评分页**：https://www.metacritic.com/game/starsand-island/critic-reviews/?platform=pc
   - 提供：Metascore、各媒体分数与短评
6. **OpenCritic 游戏页**（CDP 实际访问渲染后页面）：https://opencritic.com/game/19485/starsand-island
   - 提供：Top Critic Average、推荐率、各媒体分数与评测摘录
7. **Game Rant 报道**：https://gamerant.com/starsand-island-steam-reviews-controversy/
   - 提供：EA 上线时"可疑好评"事件的媒体报道 + 开发商 Discord 回应
8. **PC Gamer 相关文章**（仅标题/定位，未逐篇深读）
   - https://www.pcgamer.com/games/life-sim/starsand-island-is-the-first-cant-miss-cozy-game-of-2026-and-its-already-taken-over-20-hours-from-me/
   - https://www.pcgamer.com/games/sim/starsand-island-is-a-warm-familiar-farming-sim-hug-that-comes-with-all-of-the-weird-jank-that-seems-to-haunt-3d-cosy-games/

## 提取的事实内容

### 一、Steam 评价数据（来源 1、3，抓取于 2026-08-25）

- 官方名称 **Starsand Island**，开发商/发行商均为 **Seed Sparkle Lab**（注意：不是"Seed Lab"），1.0 发售日 **2026-08-18**（此前 2026-02-11 开启 Early Access，EA 时间见来源 7）。
- **全语言汇总：6,848 条评论，5,375 好评 / 1,473 差评，好评率 78.5%，评分档位「Mostly Positive / 多半好评」**。
- **简体中文子集：2,279 条评论，1,545 好评 / 734 差评，好评率 67.8%，档位「Mixed / 褒贬不一」**——中文区明显比全球更差评。
- Steam 商店页无 Metacritic 分数挂载（appdetails 返回 metacritic: null）。

### 二、Steam 代表性评论摘录（来源 2；均为按 helpful 数排序的真实评论，id=recommendationid）

**英文好评（原文英文，摘译+关键句保留原文）：**

- 【好评，40 有用，26.6h，id 233321209】画风与氛围打动人："blend of cozy nostalgic reminiscent of Stardew Valley and Animal Crossing... charming 3D anime-style visuals... capybaras, cats, and stray dogs, creates a relaxed atmosphere"。
- 【好评，18 有用，284.8h，id 233194292】理性派长评："This game is an adorably cute farming sim with a bit of adventure/combat thrown in... I have almost 300hrs... for $40, I'm happy with that cost to time investment ratio."（承认很多人对 1.0 有意见，但认为时长性价比够）
- 【好评，35 有用，35.2h，id 231481145】"one of the best farming and exploration life sims ive ever played... huge island full of things to do"——种田/钓鱼/养殖/探索内容量获认可。
- 【好评，14 有用，51.4h，id 233141076】"混合感受"型好评：不在乎恋爱线只想收集的话体验很好，但"there's been waves and waves of communication and deadline problems. There's been a strange back and forth on AI usage for months"（好评里也在提 AI 争议与沟通问题）。
- 【好评，5 有用，44.4h，id 231627483】总结式："You'll like this if you want zero pressure crafting, fishing, and farming... You'll be disappointed if you are looking for a deep story and complex world building/lore."

**英文差评（原文英文，摘译+关键句保留原文）：**

- 【差评，2,113 有用（该作最高赞差评），23.3h，id 232572288】指控刷好评+缝合："Don't be fooled, the reviews are astroturfed to hell... designed by Chinese gacha/mmo businessmen... frankenstein everything cozy gamers would like into one game... and lie about romance features to get sales."
- 【差评，1,775 有用，34.4h，id 231831979】"undisclosed ai, tencent backing. not an indie studio. kickstarter was a success, scammed tons of people who STILL haven't gotten their keys. the day 1 dlc is $20..."（注：评论称腾讯背景，Reddit 高赞评论称疑为金山/Kingsoft 系，均为玩家指控，非官方证实）
- 【差评，765 有用，2.0h，id 233140222】1.0 与 EA 几乎无差："even the full release feels just as incomplete... emphasizing that they're a 'small indie developer' to gain goodwill... is just pathetic."
- 【差评，406 有用，85.9h，id 231788505】"The game is riddled with AI, the discord community is toxic, the developers lied about being a small studio and paid for fake positive reviews upon early access release."（玩家指控汇总型差评）
- 【差评，239 有用，0.2h，id 233143790】联机设计差评："Multiplayer is locked behind hours of single-player gameplay... progress is only awarded to the host."
- 【差评，160 有用，0.9h，id 233076868】恋爱对象砍角色："Youfang was removed as a romance option right before 1.0... I feel genuinely deceived."（Kickstarter 老支持者）
- 【差评，145 有用，22.9h，id 231707547】"The use of AI without disclosing it on the Steam page is also (I'm pretty sure) against the rules? My heart is shattered."

**简中好评（原文中文，原样摘录）：**

- 【好评，0 有用，93.5h，id 232586829】"画风清新养眼，玩法简单治愈，适合上班族休闲打发时间用，音乐也还不错。需要改进：中后期很长时间就是重复劳作，畜牧养殖太麻烦，人物好感剧情有待开发"
- 【好评，1 有用，91h，id 233157586】赞松弛感："我对这个游戏的松弛感和自由度感觉很赞……没有那么多繁琐的剧情任务……想做肝帝没问题，想慢悠悠过任务看风景也没问题"
- 【好评，1 有用，85.2h，id 232631888】"优点：画风好看×3。缺点：1 内容单薄，基本玩到夏天或者秋天就很无聊了；2 NPC 对话尬死了；3 BUG 忒多了。整体还行。"（简中好评普遍是"勉强好评"，多条自述在 6-7 分档）

**简中差评（原文中文，原样摘录）：**

- 【差评，737 有用（简中最高赞差评），135.2h，id 231814983】"您真的要端着您那史一样的 AI 文本恋爱剧情和 0 主线发布正式版吗？……您现在的当务之急应该是把您工作时的 deepseek 关了"（AI 文案 + 无主线）
- 【差评，131 有用，54.9h，id 233125968】列举式长差评："刚发售时就请了一堆水军刷好评，被发现后官方回答说不是自己买的，可能是'同行捧杀'……内容空洞重复……种地系统却是一大坨屎……NPC 和死人一样"
- 【差评，33 有用，5.7h，id 233137305】联机差评："劳资就是冲着这个联机来玩的，结果联机就是一坨……把联机的内容放在两小时之后的流程里"（联机锁前置任务 + 客机进度不保留是简中差评高频点）
- 【差评，16 有用，2.0h，id 231655041】"界面和整个游戏逻辑，我感觉有一种浓烈的手游感。人物动作非常不流畅。"

**差评主题归纳（基于以上实际评论，非编造）**：① 未披露的生成式 AI 使用指控；② EA 上线期水军/刷好评指控；③ "伪独立工作室"（疑有大厂背景）；④ 1.0 相比 EA 无实质新内容、无主线剧情；⑤ 联机实现差（锁前置、客机不存进度）；⑥ Kickstarter 支持者 key 延迟发放；⑦ 首日 $20 DLC；⑧ 砍恋爱角色 Youfang。好评主题：画风/氛围/治愈、内容量大、无压力松弛感、性价比时长。

### 三、媒体评价（来源 5、6、8）

- **Metacritic（PC）：Metascore 68（Mixed or Average），10 家媒体**（来源 5）。分数带极宽：GAMINGbible 100（"The very best of Animal Crossing, Stardew Valley, and The Sims, with Studio Ghibli flair"）→ Gameliner 50（"Beautiful presentation undercut by lack of compelling story, memorable characters"）。中间档：COGconnected 70、Game8 70（"hollow narrative, underdeveloped relationships, numerous bugs"）、Gamersky 70、Tech-Gaming 69、Final Weapon 60。
- **OpenCritic：Top Critic Average 73，Critics Recommend 54%，共 13 篇评测**（来源 6，2026-08-25 实际页面读取）。代表分数：Nintendo Life 6/10（"ubiquitous bugs and performance issues weigh the entire experience down"，NS2 版）、Push Square 7/10、CGMagazine 4.5/10（"the Nintendo Switch 2 version is filled with so many bugs, it needs an industrial-grade insecticide"）、Video Chums 8.5/10、COGconnected 70/100（"1.0 is a massive leap forward from Early Access... one of the most versatile life sims available"）、Gamersky 7/10（中文评测："大部分机制仍相当基础……NPC 缺乏足够生动的反应"）。
- 媒体共识：美术/氛围/自由度受肯定；剧情单薄、NPC 缺乏生气、bug 多（尤其主机/NS2 版）是主要扣分点。
- PC Gamer 发过正面向体验文（标题称"the first can't-miss cozy game of 2026"），也发过指出"3D cozy 游戏通病式 jank"的文章（来源 8，仅标题定位，未逐篇深读）。

### 四、Reddit r/CozyGamers controversy 帖（来源 4，⚠️重点）

- **标题**："The emerging Starsand Island controversy - what is going on?"
- **URL**：https://old.reddit.com/r/CozyGamers/comments/1r2r2ou/the_emerging_starsand_island_controversy_what_is/
- **数据**：414 points，340 comments，发帖时间 2026-02-12（即 EA 上线次日，不是 1.0 时期）
- **帖子正文要点**（原文英文，如实转述）：楼主看到 Steam 差评后起疑，列出开发者被指控的多项内容（楼主强调 all alleged / 均为指控）：刷机器人好评、不透明的反作弊软件、生成式 AI 使用（楼主后来编辑补充"there does not seem to be proof for that"/当时似乎没有实证）、以大厂背书却自称独立工作室、审查自家 Discord 等。
- **高赞评论**（原文英文，摘译）：
  - 【685 赞，u/savageexplosive】游戏 subreddit 有全貌：测试者和 Kickstarter 支持者没按时拿到 key；Xbox 版很糟；"the devs are flooding Steam with fake reviews from accounts with 0 achievements after 4 hours in the game"——假好评措辞诡异：夸"尚未实装的联机"、上线不到 24 小时就称"每天都在玩"、莫名强调买断制不用氪金。"Not sure about AI usage, though, looks like it's only alleged."（AI 使用当时仅为指控）
  - 【196 赞，u/tay_rae1】辟谣+指认："they're not backed by EA but there's suspicion they are affiliated with Kingsoft"——疑与金山（Kingsoft）子公司西山居（Seasun）有关：商标登记在 Kingsoft 名下、游戏文件里发现 "Seasun" 标签、运行时会连接带 Seasun 名的域名。
  - 【121 赞，u/PrinceMaker】"If you can look past one thing there's something else... $20 day one DLC is the cherry on top."（争议一个接一个，不打算给钱）
  - 【75 赞，u/whodeyfan21】Kickstarter 支持者自述：发 key 的问卷不走 Kickstarter、进了垃圾邮件，至今没拿到 key，各渠道无回应。
  - 【59 赞，u/Gniph】"The negative ones were the only ones that sounded like actual people who played the game."（差评反而像真人写的）
  - 【45 赞，u/roses_at_the_airport】自称 gamedev 从业相关者："I cannot overstate how these people are not, in fact, indies."；提及 Steam 上有长帖讨论反作弊、反 mod、商标属于中国大公司、过度遥测等。
- **争议核心一句话**：EA 上线首日爆出"可疑刷好评"+ 疑似金山/西山居背景却营销为独立工作室 + Kickstarter 发 key 事故 + 首日 $20 DLC + AI 使用疑云（当时无实证，1.0 后 Steam 差评中"未披露 AI"已成高频指控）。

### 五、开发商对刷好评事件的回应（来源 7，Game Rant 报道，二手媒体转述）

- Seed Sparkle Lab 在 Discord 公告中承认注意到"a large number of overly positive praise comments"（大量过度正面的好评），称非官方所为，请幕后者立即停止（报道标题引语 "We kindly ask you to stop"）。
- 报道事实：可疑好评来自游戏时长不足 10 分钟的账号，大量集中在上线时刻发布，部分可疑账号随后退款；YouTuber Josh (@JoshGamingGarden) 记录了活动模式几乎相同的账号群。
- 时间线（据该报道）：EA 上线 2026-02-11，可疑活动被曝 2026-02-12。报道当时（EA 期）游戏约 91% 好评/1,700+ 评论、售约 2 万份/约 $55.3 万收入——注意这些是 EA 期媒体数字，与本文抓取的 1.0 后数据（78.5%/6,848 条）不同期，不可混用。
- ⚠️ 此为二手媒体转述，开发商 Discord 原始公告未直接核验。

## 缺口清单

- 【待确认】Steam"最近 30 天"好评率：appreviews API 的 day_range 参数未生效（返回与总体相同），未拿到 1.0 发售后独立时段的好评率，需商店页人工核对。
- 【待确认】开发商 Discord 原始公告全文（仅有 Game Rant 二手转述）。
- 【待确认】"金山/西山居背景""腾讯背景""付费水军系官方购买""未披露生成式 AI"均为玩家/Reddit 指控，未见官方承认或权威媒体实锤报道；引用时必须标注"玩家指控"。
- 【待确认】Reddit 帖中提到的 Steam 论坛"反作弊/遥测长帖"与"假评论证据帖"的具体 URL（评论中为站内链接，未展开抓取）。
- 【未找到】Metacritic 用户评分数字（本次未抓取用户评分页）。
- 【未找到】主流大媒体（IGN/GameSpot/RPS/Destructoid）的正式打分评测——搜索未见，Metacritic/OpenCritic 收录的以中小媒体为主。
