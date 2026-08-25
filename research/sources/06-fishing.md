# 06 - 钓鱼机制 / 钓点 / 鱼种（Starsand Island 星砂岛）

> 调研日期：2026-08-25 · appid 2966320 · 开发/发行：Seed Sparkle Lab
> 版本背景（重要）：本作 **2026-02-11 进入 Early Access**，**2026-08-18 发布 Version 1.0 正式版**（1.0 新增 4 人联机等）[S10]。目前全网可查的系统性钓鱼资料（官方职业攻略、鱼类清单、Fish King 攻略）**基本都产自 EA 时期（2026 年 2-3 月）**，正式版是否有增删未见系统性汇总，下文逐条标注。

# 页面目标关键词

- 英文：Starsand Island fishing guide / fish list / all fish / Fish King(s) / legendary fish / bait (Bug Bait, Veggie Bait, Minced Fish Bait) / fishing rod / fishing spots / Luminwave / Coral Sea / Celestwave / Moonlit Forest fishing / fish pond / fish trap / Angler profession
- 中文：星砂岛 钓鱼攻略 / 鱼类图鉴 / 鱼王 / 传说鱼 / 鱼饵 / 钓点 / 钓鱼职业 / 鱼塘

# 来源清单

- **[S1] Steam 商店页（官方一手）** https://store.steampowered.com/app/2966320/ — 官方定位描述（"reel in a big catch"）、发售日 Aug 18 2026、开发商 Seed Sparkle Lab。
- **[S2] 官网攻略《Part 1: Learning to Fish | Your First Catches》（官方一手）** https://www.starsandisland.com/en/#/ （GUIDE → Profession 栏目；正文经官网 omni API 提取，contentId `sw3cukk749hd`，发布 2026-02-12）— 钓鱼小游戏操作、Angler 职业前期任务链。
- **[S3] 官网攻略《Part 2: Leveling Up | On the Hunt for Fish Kings》（官方一手）** 同上，contentId `sw3gajo3wdmp` 同栏目（发布 2026-02-12）— 中高级 Angler 任务链、6 大 Fish King、鱼竿等级要求、鱼塘/孵化器/鱼笼系统。
- **[S4] 官网《Fishing Tools & Equipment Overview》（官方一手）** 同上（发布 2026-02-27）— 工具稀有度色阶；⚠️ 具体工具数值以长图形式呈现，文字不可提取。
- **[S5] 官网《Starsand Island Aquatic Life Quick Guide》（官方一手）** 同上（发布约 2026-03-26）— 按季节 × 水域的全鱼分布框架（内容主体为长图）；官方钓点区域命名。
- **[S6] TechRaptor《Starsand Island Fishing Guide | Fish List》（专业媒体）** https://techraptor.net/gaming/guides/starsand-island-fishing-guide-fish-list （发布 2026-02-11，EA 首发日）— 钓鱼机制说明 + 全量鱼表（~110 种，含季节/天气/水域/时间/鱼饵）。
- **[S7] Steam 玩家指南《Fish 🐟 [King]》 by あじさい** https://steamcommunity.com/sharedfiles/filedetails/?id=3673965770 （2026-02-26，EA 期）— 6 条 Fish King 逐条实测（地点/时间/季节/鱼饵/截图）。
- **[S8] Steam 玩家指南《Рыба. Ранний доступ. [RU]》 by KyubiTV** https://steamcommunity.com/sharedfiles/filedetails/?id=3677321554 （2026-03-02 发布、03-29 更新；标题自注明"Early Access 时点"）— 按钓点分章的全鱼表，可与 S6 交叉验证。
- **[S9] Steam 玩家指南《Starsand Island - Things Worth Noting》** https://steamcommunity.com/sharedfiles/filedetails/?id=3665494640 （EA 期）— 钓鱼体力消耗、Steamed Fish 增益、鱼售价区间。
- **[S10] Steam 官方 News（官方一手）** 1.0 预告 https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1839676055888250 （2026-07-31）；1.08.3916 补丁 https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1841579228664922 （2026-08-20）— EA→1.0 时间线；正式版后与钓鱼相关的修复条目。
- **[S11] Steam 讨论区（正式版后玩家讨论）** https://steamcommunity.com/app/2966320/discussions/0/586183630899081198/ （2026-08-21）— Pumpkin Carnival 活动中"海岸钓 jellyfish"的实测讨论。
- **[S12] Reddit r/Starsandisland：th.gl 互动地图发布帖** https://old.reddit.com/r/Starsandisland/comments/1rmao95/ （2026-03-06）— 第三方互动地图 https://starsandisland.th.gl/ ，含 fishing spots 图层。
- **[S13] Reddit r/Starsandisland：社区收集追踪表** https://old.reddit.com/r/Starsandisland/comments/1t82tmn/ （2026-05-09）— 玩家维护的 Fish/Bugs/Livestock Google Sheet（地点/季节/天气/时间/鱼饵 + 进度勾选）。

# 提取的事实内容

## 1. 钓鱼玩法机制（小游戏）

- 官方商店描述把钓鱼列为核心玩法之一（"reel in a big catch / celebrate bountiful catches"）[S1]。
- 基本流程：水面会出现 **fish shadow（鱼影）**，右键瞄准抛竿（PC）。鱼第一次触碰鱼饵通常是**假咬（fake-out）**，要等真正咬钩再收线 [S2]。
- 收线小游戏是**张力控制**：按住左键收线，**鱼线变红=快断线，松开左键让线恢复；变白后继续按住收线**，交替进行直到把鱼拖上岸 [S2]。TechRaptor 同口径描述："reel it in gradually; let go as the line turns red to avoid breaking it" [S6]，两来源交叉一致。
- 早期拿到基础 **Wooden Rod** 后即可在任意水体钓鱼；进阶鱼需要提升 fishing profession 拿更好的鱼竿并解锁鱼饵（bait）[S6]。
- 每次钓鱼消耗 **10 stamina** [S9]。
- 料理增益：**Steamed Fish** 提供 "Never Skunked"（30 秒）——鱼不再试探鱼饵、直接咬钩，不可叠加 [S9]。（正式版后讨论区有玩家反馈 grape juice 类饮品的 buff 文案疑似错标为 fishing buff，属 bug 讨论 [S10 同期讨论区，thread 586183940257235984]。）
- 船钓：Junior Angler 试炼中可在 Starsand Port 租船，**开船撞向水面鱼影可直接捞鱼**（任务要求捞 10 条）[S2]。

## 2. 鱼饵 / 鱼竿 / 设施系统

- 鱼饵共三类：**Bug Bait / Veggie Bait / Minced Fish Bait**（俄语指南译作 Meat Bait，指同一物；玩家指南 S7 也简写为 Meat）[S6][S8]。鱼饵通过 **Bait Maker** 制作，蓝图在渔具店 **Dive & Reels** 解锁 [S2]。
- 挑食示例（官方）：Moorish Idol 吃 Bug + Minced Fish Bait；**Tuna 只吃 Minced Fish Bait** [S2]。
- 鱼竿有等级与稀有度：工具稀有度色阶为 **White-1, Cyan-2, Blue-3, Purple-4, Yellow-5, Red-6** [S4]。官方点名鱼竿：**Noble Rod（Level 3）**、更高级的 **Solar Rod** [S3]。Giant Barb（Level 4 稀有大鱼）建议 Noble Rod 起步、Solar Rod 更稳 [S3]。挑战 Fish King 建议**至少 Level 4 鱼竿**，Level 3 中只有 Noble Rod 有渺茫机会 [S3]。⚠️ 完整鱼竿数值表在官网是长图，文字未能提取（见缺口）。
- 职业进阶解锁设施：**Fish Trap / Fish Cage**（被动自动捕鱼，海水专用任务需放海里）、**Small Fish Pond**（鱼塘养鱼产 Fish Eggs）、**Incubator**（孵化鱼卵，可能产稀有副产物 **Crystallized Scales**，可在 Alex 家具店换装饰）[S3][S6]。1.08.3916 补丁提到 **Stone Fish Pond**（获得后图鉴显示修复），说明鱼塘有多档 [S10]。
- Angler 职业等级线（官方，导师为 **Francis**）：**Apprentice → Junior → Intermediate → Senior → Expert** [S2][S3]。各级任务：钓任意 3 条鱼（新手）；钓 Tuna + Moorish Idol（Junior，需先重建 Starsand Port 才能出海）；建鱼塘+孵化产线（Intermediate）；收集 **20 种海洋鱼**做生态修复（Senior）；捕获**任意 2 条 Fish King**（Expert）[S2][S3]。
- 正式版 1.08.3916 修复了 "Become a Senior Angler!" 任务中 **Pufferfish** 需求数量显示错误 [S10]——注意：Pufferfish 未出现在 EA 期两份全鱼表 [S6][S8] 中，提示正式版任务/鱼池有 EA 清单未覆盖的内容（待确认）。

## 3. 钓点 / 地图区域

官方与两份鱼表口径一致的水域分区 [S5][S6][S8]：
- **岛上淡水**：River（河）、Lake（湖）
- **近海**：Ocean（海岸，无需开船）
- **出海海域（需开船 / Sailing required）**：**Luminwave**、**Coral Sea**、**Celestwave** [S5]。（⚠️ 命名差异：官网 Part 2 一处把 Swordfish 的海域写作 "Coralwave"，同一官网 Aquatic 指南与 S6/S8 均写 "Coral Sea"，实为同一区域。）
- **Moonlit Forest（月光森林）内部水域**：**Dreamfall Garden**、**Darkwater Shore** [S5][S8]。（⚠️ 命名差异：TechRaptor 表内把这两处的具体钓点写作 **Spore Cascade**（对应 Glowfish 系）与 **Spiritshade River**（对应 Green Swordtail 系）[S6]；官网 Part 2 还出现 "Dreamscape Lake near Spore Cascade" 的表述 [S3]。判断：Spore Cascade/Spiritshade River 是 Dreamfall Garden/Darkwater Shore 区域内的具体水体，各来源粒度不同。）
- 实用交通：从码头乘船去 Celestwave 约花费 **30**（金币）[S7，玩家实测]；玩家常用 Teleporter 放船上往返 [S7]。Dreamfall Garden 的钓点在瀑布边，瀑布后有可进入的空间 [S7]。
- 地图工具：官网自带 MAP 页（互动地图）[S5 所在官网]；第三方互动地图 **starsandisland.th.gl**（Starsand Island + Moonlit Forest cave 双图，含 fishing spots、宝箱、NPC 图层，支持简繁中文）[S12]。

## 4. 已确认鱼种（EA 期全量清单，S6 × S8 交叉验证）

两份独立全鱼表（TechRaptor 英文 [S6]、KyubiTV 俄文 [S8]）鱼名与分区高度一致，共约 **110 种水生生物**（含虾类）。按水域摘录（英文名保留原文；完整逐条表见 S6/S8/S13 原文）：

- **River（约 30 种）**：Giant Barb, Giant River Prawn, Zander, Electric Eel, Four-Eyed Sleeper, Payara, Red Carp, Pale Chub, Pope's Goby, Redtail Catfish, Carp, Common Rudd, Flathead Catfish, Archerfish, Chinese Hooksnout Carp, Clown Featherback, Guppy, Snakehead, Tilapia, Glass Bloodfin Tetra, Leaffish, Magnificent Killifish, Motoro Stingray, Arowana, Holland's Carp, Upside-Down Catfish, Lungfish, Royal Twig Catfish, Siberian Taimen + **Paddlefish (King), Arapaima (King)** [S6][S8]
- **Lake（约 24 种）**：Bighead Carp, Green Sunfish, Velora Cichlid, Cleaner Fish, Ide, Wheatfish, Crucian Carp, Koi, Medaka, Pumpkinseed, Silver Carp, Topmouth Culter, Betta, Grass Carp, Paradise Fish, Bitterling, Cichlid, Kissing Gourami, Alligator Gar, Chinese Perch, Mud Carp, Alaska Blackfish, Baikal Sculpin, Lake Trout [S6][S8]
- **Ocean 海岸（约 27 种）**：Brown Tiger Prawn, Clownfish, Greasyback Shrimp, Boxfish, Spinefoot, Yellowtail Damselfish, Black Scraper, Blue Angelfish, Royal Gramma, Anchovy, Noodlefish, Potato Grouper, Moorish Idol, Redfish, Tiger Puffer, Emperor Angelfish, Foureye Butterflyfish, Lionfish, Butterflyfish, Discus, Orangespine Unicornfish, Mackerel, Red Porgy, Trevally, Barracuda, Rainbow Trout, Whitefish [S6][S8]
- **Luminwave（5 种）**：**Megamouth Shark (King)**, Anglerfish, Viperfish, Mola Mola, Tuna [S6][S8]
- **Coral Sea（5 种）**：**Swordfish (King)**, Humphead Wrasse, Bass, Blue Tang, Sardine [S6][S8]
- **Celestwave（5 种）**：**Long-barbelled Dragonfish (King)**, Dolphinfish, Ribbon Eel, Flounder, Mandarinfish [S6][S8]
- **Dreamfall Garden / Spore Cascade（4 种）**：Pearl Glowfish, Fringetail Glowfish, Comet Glowfish, **Glowfish (King)** [S6][S8]
- **Darkwater Shore / Spiritshade River（4 种）**：Green Swordtail, Daisy's Ricefish, Ink Phoenixfish, Glassfish [S6][S8]

稀有度（S8 按图鉴框色记录）：灰(常见) < 绿 < 蓝 < 紫 < 金（Fish King 为金）。这与官方工具色阶 [S4] 不是同一套（前者为鱼、后者为工具），注意区分。

## 5. 稀有鱼 / 传说鱼（Fish Kings）

官方设定：全岛共 **6 条传说级 Fish King**，分布在不同水域，Expert Angler 认证只需捕获**任意 2 条** [S3]。三来源（官方 S3、玩家实测 S7、鱼表 S8）交叉后的逐条信息：

- **Paddlefish (King)** — River；Spr/Win；6:00–22:00；Bug/Veggie Bait；任意天气。公认最容易，开局就可能钓到；实测点：镇上瀑布 [S3][S7][S8]
- **Arapaima (King)** — River；Sum/Aut；12:00–2:00；Veggie/Meat(Minced Fish) Bait；Sunny/Rainy。实测点：农场北侧河流、去 Green Pasture Ranch 的木桥附近，约凌晨 2 点 [S3][S7][S8]
- **Glowfish (King)** — Moonlit Forest 的 Dreamfall Garden（Spore Cascade 瀑布）；仅 **Aut**；**0:00–2:00**；Bug Bait [S3][S7][S8]
- **Megamouth Shark (King)** — Luminwave 海域；全季节；20:00–2:00；Meat(Minced Fish) Bait；任意天气 [S3][S7][S8]
- **Long-barbelled Dragonfish (King)** — Celestwave 海域；全季节；20:00–2:00；Meat(Minced Fish) Bait [S3][S7][S8]
- **Swordfish (King)** — Coral Sea 海域；全季节；**6:00–18:00**（白天）；Meat(Minced Fish) Bait [S3][S7][S8]

玩家经验：除 Paddlefish/Swordfish 外，其余 King 集中在 **00:00–02:00** 窗口出没，建议船上放 Teleporter 快速往返 [S7]。装备门槛见上文（≥Level 4 鱼竿）[S3]。

## 6. 钓鱼与季节 / 天气 / 时间的关系

- 每种鱼有独立的 **Active Seasons（Spr/Sum/Aut/Win）× Weather（Sunny/Snowy/Rainy）× Time of Day × Bait** 组合 [S6][S8]，例如：Carp 仅春季晴天 6:00–20:00；Lungfish 仅冬季下雪 10:00–20:00；Barracuda 仅冬季下雪 16:00–24:00 [S6][S8]。
- 深海（Luminwave/Celestwave）夜行鱼集中在 20:00–24:00/–2:00（Anglerfish, Viperfish, Ribbon Eel, Mandarinfish 及两条夜行 King）[S6][S8]。
- 官方明确提示部分海鱼**白天限定、18:00 后消失**（Tuna、Moorish Idol），夜里去 Luminwave 钓它们是浪费时间 [S2]。
- Moonlit Forest 内水域的非 King 鱼基本 6:00–2:00 全时段可钓，受季节控制（如 Fringetail Glowfish 仅春、Comet Glowfish 仅夏、Glassfish 仅秋）[S6][S8]。
- 游戏内时间约定：清单普遍以 6:00 为一天起点、2:00 为末尾（即夜里 2 点后至清晨 6 点无鱼表条目）[S6][S8]。

## 7. 正式版（2026-08-18 后）与钓鱼相关的增量信息

- 1.0 官方公告确认多人联机下可以一起钓鱼（"farm, fish, build, explore… together"）[S10]。
- 正式版季节活动 **Pumpkin Carnival**：NPC Delphin 提示 **jellyfish 会漂到海岸**，玩家实测**只能在海岸（coast）钓到**，其他钓点无效 [S11]。（jellyfish 不在 EA 鱼表中，属活动产物。）
- 1.08.3916（2026-08-20）修复：Stone Fish Pond 图鉴显示、"Become a Senior Angler!" 任务 Pufferfish 数量显示、水榭/入水异常等 [S10]。
- 经济参考（EA 期玩家观察，仅供参考）：鱼直接售价约 **30–100 coins**/条，与虫、作物同档 [S9]。⚠️ 未找到任何来源的**全量鱼价表**。

# 缺口清单（未找到，标待确认）

1. **正式版 1.0 是否新增/调整了鱼种与钓鱼数值**——所有系统性鱼表均为 EA 期（2026-02/03），未找到 1.0 对照版清单；Pufferfish、jellyfish 两例说明正式版存在 EA 表外内容。待确认。
2. **每种鱼的售价表**——只有 30–100 coins 的粗略区间 [S9]，无逐条价格。待确认（严禁编造）。
3. **鱼竿完整清单与数值**（各等级名称/属性/获取方式）——官网 Tools & Equipment 文章正文为长图 [S4]，文字不可提取；仅确认 Wooden Rod、Noble Rod (Lv3)、Solar Rod 三个名字。待确认。
4. **鱼饵配方与制作材料明细**——仅知 Bait Maker + 三种鱼饵名，配方未找到。待确认。
5. **鱼的尺寸/星级/品质机制**（是否有大小或品质区分）——未在任何来源看到说明。待确认。
6. **手柄/Switch 版钓鱼操作**——机制描述均基于 PC 鼠标操作 [S2][S6]。待确认。
7. **r/StarsandIsland 上关于稀有鱼的深度讨论**——子版实际名为 r/Starsandisland，检索到的钓鱼相关帖以工具帖（地图、追踪表）为主，未找到成规模的传说鱼攻略讨论帖。
8. **Steam 讨论区 rod/bait 关键词检索无命中**（2026-08-25 检索），正式版后的钓鱼专题讨论目前较少，仅活动鱼、buff bug 等零星帖。

---
— by Claude Code · 2026-08-25
