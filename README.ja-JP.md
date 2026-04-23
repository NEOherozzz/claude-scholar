<div align="center">
  <img src="LOGO.png" alt="Claude Scholar Logo" width="100%"/>

  <p>
    <a href="https://github.com/Galaxy-Dawn/claude-scholar/stargazers"><img src="https://img.shields.io/github/stars/Galaxy-Dawn/claude-scholar?style=flat-square&color=yellow" alt="Stars"/></a>
    <a href="https://github.com/Galaxy-Dawn/claude-scholar/network/members"><img src="https://img.shields.io/github/forks/Galaxy-Dawn/claude-scholar?style=flat-square" alt="Forks"/></a>
    <img src="https://img.shields.io/github/last-commit/Galaxy-Dawn/claude-scholar?style=flat-square" alt="Last Commit"/>
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License"/>
    <img src="https://img.shields.io/badge/Claude_Code-Compatible-blueviolet?style=flat-square" alt="Claude Code"/>
    <img src="https://img.shields.io/badge/Codex_CLI-Compatible-blue?style=flat-square" alt="Codex CLI"/>
    <img src="https://img.shields.io/badge/OpenCode-Compatible-orange?style=flat-square" alt="OpenCode"/>
  </p>

  <strong>Language</strong>: <a href="README.md">English</a> | <a href="README.zh-CN.md">中文</a> | <a href="README.ja-JP.md">日本語</a>
</div>

> 学術研究とソフトウェア開発のための半自動リサーチアシスタントであり、特にコンピュータサイエンスと AI 研究者に適しています。[Claude Code](https://github.com/anthropics/claude-code)、[Codex CLI](https://github.com/openai/codex)、[OpenCode](https://github.com/opencode-ai/opencode) をサポートし、文献管理、コーディング、実験分析、結果レポート、執筆、プロジェクト知識ベースの保守を支援します。

## 最新ニュース

- **2026-04-22**: **軽量なコア指示へ更新** — 大きな always-on `CLAUDE.md` / `AGENTS.md` をコンパクトなコア指示に置き換え、中国語 companion ファイルを追加し、詳細な skills、commands、agents、workflow は必要時に読む参照として残しました。これによりデフォルトの context コストを抑えます。
- **2026-04-15**: **pubfig と pubtab という 2 つの Python package を導入** — [`pubfig`](https://github.com/Galaxy-Dawn/pubfig) を論文品質の scientific figures 向け Python package、[`pubtab`](https://github.com/Galaxy-Dawn/pubtab) を publication-ready な tables と Excel↔LaTeX workflows 向け Python package として打ち出し、論文図、benchmark 表、書き出し制御、最終 QA までの生産経路をより明確にしました。
- **2026-04-15**: **publication-chart-skill を Claude Scholar に統合** — [`pubfig`](https://github.com/Galaxy-Dawn/pubfig) + [`pubtab`](https://github.com/Galaxy-Dawn/pubtab) を `publication-chart-skill` としてまとめてリポジトリに追加し、Claude Scholar の分析/執筆スタックの boundary に接続しました。これにより、論文品質の図表作業を汎用分析や prose skill に混ぜず、明示的な handoff で扱えるようになりました。

## クイックナビゲーション

| セクション | 役割 |
|---|---|
| [なぜ Claude Scholar なのか](#なぜ-claude-scholar-なのか) | プロジェクトの位置づけと適用場面を素早く理解する。 |
| [コアワークフロー](#コアワークフロー) | 研究構想から投稿までの主線を確認する。 |
| [クイックスタート](#クイックスタート) | フル / 最小 / 選択導入の方法を選ぶ。 |
| [使い始めのシナリオ](#使い始めのシナリオ) | インストール後の代表的な使い始め方を見る。 |
| [連携機能](#連携機能) | Zotero と Obsidian をどう接続するかを見る。 |
| [主要ワークフロー](#主要ワークフロー) | 中核となる研究・開発ワークフローを確認する。 |
| [支援ワークフロー](#支援ワークフロー) | 主ワークフローを支える背景メカニズムを確認する。 |
| [ドキュメント入口](#ドキュメント入口) | setup、設定、テンプレート文書へ移動する。 |
| [引用](#引用) | 論文・報告書・プロジェクト文書で Claude Scholar を引用する。 |

## なぜ Claude Scholar なのか

Claude Scholar は、研究者を置き換え、エンドツーエンドの全自動研究を目指すタイプのシステム**ではありません**。

核となる考え方はシンプルです。

> **最終判断は人間が担い、アシスタントは研究プロセスを加速する。**

そのため Claude Scholar は、文献整理、知識の蓄積、実験分析、結果報告、執筆支援のような「反復的で構造依存だが、人の判断が必要な仕事」に特に向いています。本質的な判断は、常に研究者自身が行うべきです。

- この問題に取り組む価値があるか
- どの文献が本当に重要か
- どの仮説をさらに検証すべきか
- どの結果が十分に信頼できるか
- 何を継続し、何を論文にし、何を投稿し、あるいはどこでやめるべきか

言い換えれば、Claude Scholar は**人間の意思決定を中心に据えた半自動研究アシスタント**であり、「全自動研究エージェント」ではありません。

## どんな人に向いているか

Claude Scholar は特に次のような人に向いています。

- **コンピュータサイエンス研究者**：文献、コード、実験、論文執筆を頻繁に切り替える人
- **AI / ML researcher**：構想、実装、分析、報告、rebuttal を一つの流れで回したい人
- **research engineer や大学院生**：人間の判断を保ちながら、より強いプロセス構造を導入したい人
- **ソフトウェア・計算駆動型の学術プロジェクト**：Zotero、Obsidian、CLI 自動化、追跡可能な project memory の恩恵を直接受けられる人

他分野にも役立ちますが、現状の設計重心はコンピュータサイエンス、AI、および近接する computational research に最も近いです。

## コアワークフロー

- **研究構想**：曖昧なテーマを具体的な研究問題、研究ギャップ、初期計画へ収束させる
- **文献ワークフロー**：Zotero コレクションを通じて論文を検索、取込、整理し、読む
- **論文ノート**：論文を構造化読書ノートと再利用可能な論点へ変換する
- **知識ベースへの蓄積**：安定知識を Obsidian に書き込み、`Papers / Knowledge / Experiments / Results / Writing` に振り分ける。ラウンド単位の実験レポートは `Results/Reports/` に保存する
- **実験推進**：仮説、実験ライン、実行履歴、主要発見、次アクションを追跡する
- **厳密分析**：`results-analysis` を用いて厳密統計、実際の科研図、分析成果物を生成する
- **結果レポート**：`results-report` を用いて完全な実験レビューを作成し、Obsidian へ書き戻す
- **執筆と発表**：安定した結論をレビュー、論文、rebuttal、発表資料、ポスター、発信素材へ展開する

## クイックスタート

### 前提条件

- [OpenCode](https://github.com/sst/opencode)
- Git
- （任意）Python + [uv](https://docs.astral.sh/uv/) — Python 開発用
- （任意）[Zotero](https://www.zotero.org/) + [Galaxy-Dawn/zotero-mcp](https://github.com/Galaxy-Dawn/zotero-mcp) — 文献ワークフロー用
- （任意）[Obsidian](https://obsidian.md/) — プロジェクト知識ベース用

### オプション 1：フルインストール（推奨）

```bash
git clone -b opencode https://github.com/Galaxy-Dawn/claude-scholar.git /tmp/claude-scholar
bash /tmp/claude-scholar/scripts/setup.sh
```

インストーラーは現在、**バックアップ付きの安全な増分更新**をサポートしています。
- リポジトリ管理の `skills/commands/plugins/scripts/utils/` を更新
- 上書き対象ファイルを `~/.opencode/.claude-scholar-backups/<timestamp>/` にバックアップ
- `opencode.jsonc` も `opencode.jsonc.bak` としてバックアップ
- `~/.opencode/AGENTS.md` が既に存在する場合は元ファイルを保持し、リポジトリ版を `~/.opencode/AGENTS.scholar.md` として保存
- `~/.opencode/AGENTS.zh-CN.md` が既に存在する場合は元ファイルを保持し、リポジトリ版の中国語 companion を `~/.opencode/AGENTS.zh-CN.scholar.md` として保存
- 既存の `env`、モデル / provider 設定、API key、permissions、auth、および `mcp` の現在値を保持
- リポジトリ管理の `agent/mcp/permission/plugin` 条目は、全置換ではなく不足項目を追加する形でマージ

**重要な AGENTS 説明**：すでに自分用の `~/.opencode/AGENTS.md` を持っている場合は、インストール後に `~/.opencode/AGENTS.scholar.md` と `~/.opencode/AGENTS.zh-CN.scholar.md` を確認し、必要な Claude Scholar の内容だけを自分のファイルに手動で merge してください。sidecar ファイルが自動で有効化されるとは考えないでください。

以後の増分更新は次の通りです。

```bash
cd /tmp/claude-scholar
git pull --ff-only
bash scripts/setup.sh
```

**Windows**：インストーラーは Git Bash / WSL から実行してください。

### オプション 2：最小インストール

研究ワークフローの小さなサブセットのみを導入します。

```bash
git clone -b opencode https://github.com/Galaxy-Dawn/claude-scholar.git /tmp/claude-scholar
mkdir -p ~/.opencode/plugins/lib ~/.opencode/skills
cp /tmp/claude-scholar/plugins/*.ts ~/.opencode/plugins/
cp /tmp/claude-scholar/plugins/lib/common.ts ~/.opencode/plugins/lib/
cp -r /tmp/claude-scholar/skills/ml-paper-writing ~/.opencode/skills/
cp -r /tmp/claude-scholar/skills/research-ideation ~/.opencode/skills/
cp -r /tmp/claude-scholar/skills/results-analysis ~/.opencode/skills/
cp -r /tmp/claude-scholar/skills/results-report ~/.opencode/skills/
cp -r /tmp/claude-scholar/skills/review-response ~/.opencode/skills/
cp -r /tmp/claude-scholar/skills/writing-anti-ai ~/.opencode/skills/
cp -r /tmp/claude-scholar/skills/git-workflow ~/.opencode/skills/
cp -r /tmp/claude-scholar/skills/bug-detective ~/.opencode/skills/
```

**インストール後**：最小化 / 手動インストールでは `opencode.jsonc` は**自動マージされません**。必要な plugin や MCP 条目だけを手動で取り込んでください。自分の `~/.opencode/AGENTS.md` がある場合も、関連部分だけを手動で merge し、丸ごと上書きしないでください。

### オプション 3：選択インストール

必要な部分だけをコピーします。

```bash
git clone -b opencode https://github.com/Galaxy-Dawn/claude-scholar.git /tmp/claude-scholar
cd /tmp/claude-scholar

cp plugins/*.ts ~/.opencode/plugins/
cp -r skills/latex-conference-template-organizer ~/.opencode/skills/
cp -r skills/architecture-design ~/.opencode/skills/
cp AGENTS.md ~/.opencode/AGENTS.md
cp AGENTS.zh-CN.md ~/.opencode/AGENTS.zh-CN.md
```

**インストール後**：選択的 / 手動インストールでも `opencode.jsonc` は自動マージされません。必要な plugin / MCP 条目だけを手動で取り込んでください。既に `~/.opencode/AGENTS.md` を持っている場合も、必要な内容だけを手動で merge してください。

## 使い始めのシナリオ

インストール後は、システム全体を先に覚えようとするよりも、自然言語で今やりたいことをそのまま伝えるのがいちばん簡単です。ここでは、最初の一歩として使いやすい代表的なシナリオをいくつか挙げます。

### 1. 新しい研究テーマを立ち上げる
**たとえばこう言えます:**
> [あなたの研究テーマ]について研究を始めたいです。文献に基づいた初期プラン、重要な未解決問題、次にやるべき具体的なステップを整理してください。

**Claude Scholarがよく支援する内容:**
- テーマを明確化して研究課題を絞り込む
- 優先して見るべき文献の方向を整理する
- 初期計画や仮説候補をまとめる
- 必要ならZoteroやObsidianにも流し込む

### 2. Zotero文献コレクションをレビューする
**たとえばこう言えます:**
> Zoteroにある brain foundation models 関連の文献コレクションをレビューして、主な流れ、研究ギャップ、次に有望な方向をまとめてください。

**典型的な出力:**
- テーマ別の論文整理
- 簡潔な文献総括
- ギャップ分析
- 次に掘る価値のある研究方向

### 3. 完了した実験結果を分析する
**たとえばこう言えます:**
> この実験フォルダの結果を分析して、各runで何が変わったのかを確認し、意思決定に使える要約を書いてください。

**典型的な出力:**
- 指標比較
- アブレーションやエラー分析の提案
- 何が堅い結論で、何がまだ弱く、次に何を走らせるべきかを整理した結果要約

### 4. 論文の節やrebuttal草稿を書く
**たとえばこう言えます:**
> このプロジェクトの現時点の知見と論文メモに基づいて、関連研究の節の草稿を書いてください。

または:

> これらの査読コメントに対するrebuttal草稿を手伝ってください。

**典型的な出力:**
- 構造化された節ドラフト
- より明確な論理展開
- 主張と根拠の対応整理
- 追加で検証や補強が必要な論点

### 実用上のメモ
- 最初は「全部やって」ではなく、具体的な一つのタスクから始めるのがおすすめです。
- すでに自分用のローカル`AGENTS.md`または`AGENTS.zh-CN.md`を運用している場合は、`AGENTS.scholar.md`または`AGENTS.zh-CN.scholar.md`から必要な内容だけを手動でマージしてください。別名で配置されたファイルが自動適用されるわけではありません。
- ZoteroとObsidianは必須ではありませんが、単発のチャット出力ではなく、継続的な文献ノートやプロジェクトメモリを残したい場合にはかなり有用です。

## プラットフォームサポート

Claude Scholar は現在、次の CLI ワークフローを対象にしています。

- **Claude Code** — 主たる導入対象
- **Codex CLI** — 対応ワークフローと対応文書を提供
- **OpenCode** — 代替 CLI としてサポート

トップレベルの目的は共通です。研究、コーディング、実験、レポート、執筆、プロジェクト知識ベース保守を一つの大きな流れで支えます。

## 連携機能

### Zotero

次のような場面に向いています。
- DOI / arXiv / URL から論文を取り込む
- collection 単位で論文をまとめて読む
- Zotero MCP を通して全文にアクセスする
- 詳細な論文ノートと文献統合を作る

詳しくは [MCP_SETUP.ja-JP.md](./MCP_SETUP.ja-JP.md) を参照してください。

### Obsidian

次のような場面に向いています。
- ファイルシステム中心のプロジェクト知識ベースを維持する
- `Papers/` を管理する
- `Knowledge/` を管理する
- `Experiments/` を管理する
- `Results/` を管理する
- `Results/Reports/` を管理する
- `Writing/` と `Daily/` を管理する

詳しくは [OBSIDIAN_SETUP.ja-JP.md](./OBSIDIAN_SETUP.ja-JP.md) を参照してください。

## 主要ワークフロー

研究構想から発表までを含む、完全な学術研究ライフサイクルの 7 段階です。

### 1. 研究構想（Zotero 統合）

アイデア生成から文献管理までを一体化した研究立ち上げフローです。

| 種類 | 名前 | 一行説明 |
|---|---|---|
| Skill | `research-ideation` | 曖昧な研究テーマを構造化問題、研究ギャップ分析、初期研究計画へ収束させる |
| Agent | `literature-reviewer` | 論文を検索・分類・統合し、実行可能な文献地図を作る |
| Command | `/research-init` | 文献検索、Zotero 整理、研究提案ドラフトまでを一括起動する |
| Command | `/zotero-review` | 既存 Zotero collection を構造化レビューし、比較と統合を行う |
| Command | `/zotero-notes` | Zotero collection をまとめて読み、構造化された論文読書ノートを生成する |

**進め方**
- **5W1H ブレインストーミング**：曖昧なテーマを構造化問題へ収束させる
- **文献検索と取込**：論文を探し、DOI/arXiv/URL を抽出し、Zotero に入れてテーマごとに整理する
- **PDF と全文**：PDF を添付できるなら添付し、全文を読めるなら読む。必要に応じて要旨分析へフォールバックする
- **研究ギャップ分析**：literature / methodology / application / interdisciplinary / temporal の各種ギャップを見つける
- **研究問題と計画**：文献レビューを、明確な研究問題、初期仮説、次の計画へ変換する

**典型的な成果物**
- 文献レビュー・ノート
- 構造化された Zotero コレクション
- 研究計画 / 方向ドラフト

### 2. ML プロジェクト開発

実験コード向けの、保守しやすい ML プロジェクト開発ワークフローです。

| 種類 | 名前 | 一行説明 |
|---|---|---|
| Skill | `architecture-design` | 新しい登録可能コンポーネントやモジュール追加時に、保守しやすい ML 構造を設計する |
| Skill | `git-workflow` | ブランチ規範、commit 規範、より安全な協業フローを整える |
| Skill | `bug-detective` | stack trace、shell エラー、コードパス問題を体系的に追跡する |
| Agent | `code-reviewer` | コード変更の正しさ、保守性、実装品質をレビューする |
| Command | `/plan` | 実装前に計画を作成・洗練する |
| Command | `/commit` | 現在の変更に対する規範的 commit を生成する |
| Command | `/code-review` | 現在の変更に焦点を当てたコードレビューを行う |
| Command | `/tdd` | 小さなテスト駆動ステップで機能実装を進める |

**進め方**
- **構造設計**：適切な場面では Factory / Registry パターンで ML コンポーネントを整理する
- **コード品質**：ファイル規模、型ヒント、設定駆動設計を維持する
- **問題調査**：stack trace、shell エラー、コードパス問題を体系的に扱う
- **Git 規律**：ブランチ戦略、commit 規範、安全な merge / rebase フローを維持する

### 3. 実験分析

厳密統計、科研図、分析成果物、実験後レポートを含む厳格な分析ワークフローです。

| 種類 | 名前 | 一行説明 |
|---|---|---|
| Skill | `results-analysis` | 厳密統計、実際の科研図、分析付録から成る分析パッケージを生成する |
| Skill | `results-report` | 分析成果物を、結論・制約・次アクションが明確な完全な実験レポートへまとめる |
| Command | `/analyze-results` | 厳密分析から最終レポート生成までを一括実行する |

**進め方**
- **データ処理**：実験ログ、metrics ファイル、結果ディレクトリを読む
- **統計検定**：適切な前提の下で t-test / ANOVA / Wilcoxon などの厳密統計検定を行う
- **科研可視化**：曖昧な作図提案ではなく、実際の科研図と解釈の手がかりを生成する
- **消融と比較**：コンポーネント寄与、性能 tradeoff、安定性を分析する
- **実験後レポート**：分析パッケージを、結論・制約・次アクションを含む完全な実験後レポートへ変換する

**典型的な成果物**
- `analysis-report.md`
- `stats-appendix.md`
- `figure-catalog.md`
- `figures/`
- Obsidian `Results/Reports/` に書き込まれる実験まとめレポート

### 4. 論文執筆

構造準備から草稿反復までの、体系的な論文執筆ワークフローです。

| 種類 | 名前 | 一行説明 |
|---|---|---|
| Skill | `ml-paper-writing` | repo、実験結果、文献コンテキストを基に投稿志向の ML/AI 論文を書く |
| Skill | `citation-verification` | 参考文献、メタデータ、claim-citation 対応を確認し、引用ミスを防ぐ |
| Skill | `writing-anti-ai` | 機械的な言い回しを減らし、明瞭さ、リズム、自然な学術トーンを改善する |
| Skill | `latex-conference-template-organizer` | 散らかった会議テンプレートを Overleaf-ready な執筆構造へ整理する |
| Agent | `paper-miner` | 高品質論文から再利用可能な書き方、構造、投稿ノウハウを抽出する |
| Command | `/mine-writing-patterns` | 論文を読み、再利用可能な執筆知識をグローバル paper-miner writing memory に統合する |

**進め方**
- **テンプレート準備**：会議テンプレートを Overleaf-ready な構造へ整理する
- **引用検証**：参考文献、メタデータ、claim-citation 対応を確認する
- **体系的執筆**：repo、実験結果、文献コンテキストに基づいて節ごとに書く
- **スタイル調整**：AI 痕跡を減らし、リズム、明瞭さ、学術トーンを改善する

### 5. 論文セルフレビュー

投稿前の品質保証ワークフローです。

| 種類 | 名前 | 一行説明 |
|---|---|---|
| Skill | `paper-self-review` | 投稿前に構造、論理、引用、図表、順守項目を体系的に確認する |

**進め方**
- **構造確認**：論理の流れ、章バランス、叙述の一貫性を確認する
- **論理検証**：claim-evidence の整合、仮説の明瞭さ、議論の一貫性を確認する
- **引用監査**：引用の正確さと完全性を点検する
- **図表品質**：caption 完整性、可読性、アクセシビリティを確認する
- **順守確認**：ページ制限、形式、開示要件を確認する

### 6. 投稿と Rebuttal

投稿準備と査読返信のワークフローです。

| 種類 | 名前 | 一行説明 |
|---|---|---|
| Skill | `review-response` | 査読コメントを、証拠ベースの rebuttal ワークフローへ整理する |
| Agent | `rebuttal-writer` | 専門的で礼儀正しく、構造の明確な rebuttal 文書を起草する |
| Command | `/rebuttal` | 査読コメントと既存証拠に基づき、完全な rebuttal 草稿を生成する |

**進め方**
- **投稿前確認**：会議 / ジャーナルの形式、匿名化、checklist 要件を確認する
- **査読分析**：コメントを実行可能な問題に分類する
- **返信戦略**：accept / defend / clarify / 追加実験のどれを取るか判断する
- **Rebuttal 執筆**：構造的で証拠に基づき、語調の整った返信文書を作る

### 7. 採択後処理

採択後の会議準備と研究発信ワークフローです。

| 種類 | 名前 | 一行説明 |
|---|---|---|
| Skill | `post-acceptance` | 発表、ポスター、発信素材の準備を支援する |
| Command | `/presentation` | 会議発表の構成と話し方ガイドを生成する |
| Command | `/poster` | 論文内容を整理し、ポスター構成とレイアウト指針を生成する |
| Command | `/promote` | 外部向け要約、投稿文、thread を起草する |

**進め方**
- **発表準備**：発表構成と資料指針を整える
- **ポスター整理**：ポスターの内容階層と版面を整理する
- **対外発信**：ソーシャルメディア、ブログ、簡明研究要約を生成する

## 支援ワークフロー

これらのワークフローは主ワークフローの背後で動き、全体体験を強化します。

### Obsidian プロジェクト知識ベース

Obsidian を、気軽に積んだメモ置き場ではなく、安定した研究知識の沈殿先として扱います。

| 種類 | 名前 | 一行説明 |
|---|---|---|
| Skill | `obsidian-project-memory` | プロジェクトレベルの Obsidian 知識ベースを維持し、どの安定知識を書き戻すかを判断する |
| Skill | `obsidian-project-bootstrap` | 新規または既存研究プロジェクト向けに Obsidian 知識ベース構造を初期化する |
| Skill | `obsidian-research-log` | 毎日の研究進捗、計画、発想、TODO を知識ベースへ書き込む |
| Skill | `obsidian-experiment-log` | 実験設定、実行過程、結果、次アクションを Obsidian に記録する |
| Command | `/obsidian-ingest` | 新しい Markdown ファイルやディレクトリを適切な知識ベース位置へ整理して取り込む |
| Command | `/obsidian-note` | 単一 note の検索、リネーム、アーカイブ、削除などのライフサイクル操作を行う |
| Command | `/obsidian-views` | `.base` などの Obsidian view ファイルを生成または更新する |

**進め方**
- 既存 repo を Obsidian vault にバインドする
- 安定知識を `Papers / Knowledge / Experiments / Results / Writing` に振り分け、ラウンド単位の実験レポートは `Results/Reports/` に保存する
- `Daily/` と project memory を保守的に維持する
- 新しい Markdown を分類し、正しい正規ノートへ統合する
- 必要な時だけ追加 view や canvas を生成する

**ノート言語設定**

Obsidian ノート生成・同期時の言語は次の優先順位で解決されます。
1. プロジェクト設定：`.opencode/project-memory/registry.yaml` の `note_language`
2. 環境変数：`OBSIDIAN_NOTE_LANGUAGE`
3. デフォルト：`en`

補足：ファイル名は `registry.yaml` のままですが、実際の on-disk format は JSON です。

プロジェクト単位の例：

```json
{
  "projects": {
    "my-project": {
      "project_id": "my-project",
      "vault_root": "/path/to/vault/Research/my-project",
      "note_language": "zh-CN"
    }
  }
}
```

同期時には英語と中国語の section heading がどちらも互換的に扱われるため、設定変更後でも過去の英語 / 中国語ノートは安全に更新できます。

### 自動化制約ワークフロー

クロスプラットフォーム plugins が日常的なチェックとリマインドを自動実行します。

**Plugin 一覧**
- `skill-eval.ts`
- `session-start.ts`
- `session-summary.ts`
- `stop-summary.ts`
- `security-guard.ts`

**進め方**
- **ユーザー質問前**：現在の prompt で発火すべき skills を評価し、関連 workflow ヒントを補足する
- **セッション開始時**：Git 状態、利用可能コマンド、project memory 文脈を表示する
- **セッション終了または停止時**：作業内容をまとめ、最低限のメンテナンス行動をリマインドする
- **安全防護**：破壊的コマンドを遮断し、危険だが妥当な操作には確認を要求する

### 知識抽出ワークフロー

専用 agents が論文や競技解法から再利用可能な知識を継続的に抽出します。

| 種類 | 名前 | 一行説明 |
|---|---|---|
| Agent | `paper-miner` | 高品質論文から再利用可能な執筆知識、構造パターン、投稿ノウハウを抽出する |
| Agent | `kaggle-miner` | 優れた Kaggle ワークフローから実装慣行と解法パターンを抽出する |

**進め方**
- 論文から書き方、会議要求、rebuttal 戦略を抽出する
- Kaggle ワークフローから実装パターンと解法構造を抽出する
- それらを skills と references に還流する

### Skill 進化システム

Claude Scholar には self-improving な skill ワークフローも内蔵されています。

| 種類 | 名前 | 一行説明 |
|---|---|---|
| Skill | `skill-development` | 明確な発火条件、構造、段階的展開を備えた新しい skill モジュールを作る |
| Skill | `skill-quality-reviewer` | 内容品質、構成、表現、構造完全性の観点から skill を審査する |
| Skill | `skill-improver` | 構造化された改善計画に基づいて既存 skill を継続改善する |

**進め方**
- 明確な発火説明を持つ新 skill を作る
- 複数の品質軸で skill をレビューする
- 改善提案を取り込み、継続的に反復する

## ドキュメント入口

- [MCP_SETUP.ja-JP.md](./MCP_SETUP.ja-JP.md) — Zotero / ブラウザ MCP 設定
- [OBSIDIAN_SETUP.ja-JP.md](./OBSIDIAN_SETUP.ja-JP.md) — Obsidian プロジェクト知識ベースワークフロー
- [AGENTS.md](./AGENTS.md) — 軽量な OpenCode コア指示
- [AGENTS.zh-CN.md](./AGENTS.zh-CN.md) — 軽量コア指示の中国語 companion ファイル
- [README.md](./README.md) — 英語版 README
- [README.zh-CN.md](./README.zh-CN.md) — 中国語版 README
- [opencode.jsonc](./opencode.jsonc) — plugin / MCP / agent / permission の任意設定テンプレート

## プロジェクトルール

Claude Scholar には次の領域のルールが含まれます。
- コードスタイル
- agent オーケストレーション
- 安全制約
- 実験再現性

常時有効なルールは主に `AGENTS.md` にあり、詳細なワークフローは同梱 skills と docs に残しています。

## コントリビューション

issue、PR、ワークフロー改善提案を歓迎します。

installer、Zotero ワークフロー、Obsidian ルーティングを変更したい場合は、提案に次を含めてください。
- ユーザーシナリオ
- 現在の制約
- 期待される挙動
- 互換性への影響

## ライセンス

MIT License。

## 引用

Claude Scholar があなたの研究またはエンジニアリングワークフローの助けになった場合は、次のように引用できます。

```bibtex
@misc{claude_scholar_2026,
  title        = {Claude Scholar: Semi-automated research assistant for academic research and software development},
  author       = {Gaorui Zhang},
  year         = {2026},
  howpublished = {\url{https://github.com/Galaxy-Dawn/claude-scholar}},
  note         = {GitHub repository}
}
```

## 謝辞

OpenCode 向けに構築され、より広い Claude Scholar エコシステムと整合するよう維持されています。

### 参考資料

本プロジェクトはコミュニティの優れた仕事から着想を得て構築されています。

- **[everything-claude-code](https://github.com/anthropics/everything-claude-code)** - Claude Code CLI の総合リソース
- **[AI-research-SKILLs](https://github.com/zechenzhangAGI/AI-research-SKILLs)** - 研究指向の skills と設定

これらのプロジェクトは、Claude Scholar の研究志向機能に貴重な知見と土台を与えています。

---

**データサイエンス、AI 研究、学術執筆のために。**

リポジトリ：[https://github.com/Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)
