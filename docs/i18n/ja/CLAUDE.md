<!-- translation-navigation -->
[English](../en/CLAUDE.md) · [Русский](../ru/CLAUDE.md) · [Español](../es/CLAUDE.md) · [Français](../fr/CLAUDE.md) · [Deutsch](../de/CLAUDE.md) · [Português (Brasil)](../pt-BR/CLAUDE.md) · [简体中文](../zh-CN/CLAUDE.md) · [日本語](CLAUDE.md) · [हिन्दी](../hi/CLAUDE.md) · [العربية](../ar/CLAUDE.md)

[英語原文](../../../CLAUDE.md)

[日本語](README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="claudemd"></a>
# CLAUDE.md

このファイルは,このリポジトリのコードと作業する際にクラウド・コード (claude.ai/code) に指針を提供する.

<a id="what-this-repository-is"></a>
## このリポジトリとは

オープンソースハードウェアプロジェクト: 3Dプリントの並行グリッパー SO-ARM100/101 ロボット腕 ( Robonine). 複数のライセンス: CERN-OHL-P-2.0 ハードウェア/CAD Apache-2.0 ソフトウェアについて CC BY 4.0 ドキュメント  ⁇  の地図は, `LICENSING.md`,機械読み取れるバージョン `REUSE.toml`,第三者属性 `NOTICE`. 新しいファイルは, `REUSE.toml`; `reuse lint` 実行する. ほとんどのレポはCADモデル (`models/`),文書 (`docs/`),および画像 (`assets/`). コードは二か所にあります：

- `software/python/gripper_control.py` ⁇  自動セルボ制御スクリプト Feetech STS3215 (この項目は STServo SDKは手動にクローンされる `software/python/requirements.txt`PyPIではありません. `examples/basic_usage.py` 輸入品は `sys.path` ハック
- `simulation/so_arm_101_description/` — a ROS2 5つの物理エンジンで腕+グリッパーをシミュレーションする (謙虚) 記述パッケージ ここに全ての検査とほとんどの情報提供者が住んでいます

<a id="commands"></a>
## 命令

```bash
# Lint (what CI runs; hooks exclude STL/STEP files)
pre-commit run --all-files

# Offline tests (65 pytest tests; deps: pytest trimesh numpy mujoco pyyaml)
cd simulation/so_arm_101_description
python -m pytest test/ -v

# Single test file / single test
python -m pytest test/test_urdf_structure.py -v
python -m pytest test/test_config.py -k <name> -v

# Validate xacro/URDF XML without ROS2
python simulation/so_arm_101_description/scripts/validate_xml.py simulation/so_arm_101_description/urdf/*.xacro

# Docker (from simulation/so_arm_101_description/; no ROS2 install needed)
docker compose run test          # run pytest suite
docker compose run validate      # xacro + check_urdf for all 5 backends
docker compose run check-launch  # verify launch files parse
docker compose run gazebo        # or: mujoco, webots, rviz (need X11)
```

CI (`.github/workflows/ci.yaml`) 実行:事前コミット,XML/YAML認証 `xacro ... sim_backend:=<backend> | check_urdf` 5つのバックエンドの内側に `ros:humble` 容器とピテスト・スイート URDFの変更は, **すべて** 狙っているだけではありません

<a id="simulation-architecture"></a>
## シミュレーションアーキテクチャ

単一のパラメータ化されたロボット記述を、すべてのシミュレーターで使用します：

- `urdf/so_101.urdf.xacro` 真実の唯一の源です ゼクロアルグ `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` 選択する `ros2_control` プラグイン (経由) `urdf/so_101.ros2_control.xacro`) 拡大時に.
- `config/controllers.yaml` すべてのバックエンドに同一の結合/コントローラーを定義する. `launch/sim.launch.py` と `sim:=<backend>` 唯一の入口点です
- ロボット: 5DOF腕+グリッパー 2つのプリズマティック・クランプ関節で,左クランプが右側を反射する `<mimic>`.
- メッシュは分割される. `meshes/visual/` (高ポリー) vs `meshes/collision/` (コンベックス型船体,再生された `scripts/generate_collision_meshes.py`).

結合,リンク,またはコントローラー名前の変更には,xacroファイル全体で調整された編集が必要です. `controllers.yaml`試験は `test/`.

<a id="cad-models-and-part-numbering"></a>
## CADモデルと部品番号付け

部品 `models/parts/` 使用 Robonine パーツ番号 (例: `RB9.01.062.010 Main frame.STL`). この数字は `README.md` (印刷表) `docs/bom.md`そして `docs/assembly-guide.md` 部分の追加または名称変更は,その文書を更新することでもあります. STLはバイナリで,バリエーションはファイル名にフィット トランスメントをコードする (例: `RB9.01.062.021 (D6.1) Clamp.STL` 棒の直径が異なる場合). 預約前のハック (ホワイトスペース,EOF,ラインエンド) を故意に排除する `.stl/.STL/.STEP` 1 MB以上のファイルが拒否される `check-added-large-files`.

<a id="conventions"></a>
## 大会

- Python: flake8 と `--max-line-length=100`ブラックプロフィールで並べられる (事前コミットによって強制される) `software/` そして `examples/` フラックから除外されている (8)
- 文書はデザインによって複製されます (READMEの要約) bom.md, specifications.md, assembly-guide.md)  ⁇  仕様や部品,価格の変更時に一貫性を維持する.
- 追加する `Co-Authored-By: Claude` 約束へのライン
<!-- /translated-content -->
