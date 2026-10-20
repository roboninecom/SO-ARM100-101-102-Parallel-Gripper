<!-- translation-navigation -->
[English](../en/CLAUDE.md) · [Русский](CLAUDE.md) · [Español](../es/CLAUDE.md) · [Français](../fr/CLAUDE.md) · [Deutsch](../de/CLAUDE.md) · [Português (Brasil)](../pt-BR/CLAUDE.md) · [简体中文](../zh-CN/CLAUDE.md) · [日本語](../ja/CLAUDE.md) · [हिन्दी](../hi/CLAUDE.md) · [العربية](../ar/CLAUDE.md)

[Английский оригинал](../../../CLAUDE.md)

[Русский](README.md)

> Полный машинный перевод; носители языка его ещё не проверяли. Изображения, код, CAD и исходные PDF общие. При неоднозначности используйте английский оригинал.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="claudemd"></a>
# CLAUDE.md

Данный файл дает руководство Клод-коду (claude.ai/code) при работе с кодом в этом хранилище.

<a id="what-this-repository-is"></a>
## Что это за хранилище

Проект аппаратного обеспечения с открытым исходным кодом: 3D-печатный параллельный захват для SO-ARM100/101 роботская рука (по Robonine). Многолицензированные: CERN-OHL-P-2.0 для оборудования/CAD, Apache-2.0 для программного обеспечения, CC BY 4.0 для документов  ⁇  карта находится в `LICENSING.md`, машинночитаемой версии в `REUSE.toml`, присвоение третьим лицам в `NOTICE`. Новые файлы должны быть охвачены `REUSE.toml`; `reuse lint` проходит в предвыборной форме. Большинство репо представляет собой модели CAD (`models/`), документация (`docs/`), а также изображения (`assets/`). Код живет в двух местах:

- `software/python/gripper_control.py` ⁇  самостоятельный сервоконтрольный скрипт для Feetech STS3215 (зависит от STServo SDK, который клонируется вручную  ⁇  см. `software/python/requirements.txt`; он отсутствует на PyPI). `examples/basic_usage.py` импорт из него через `sys.path` Хак.
- `simulation/so_arm_101_description/` — a ROS2 Описание пакета, который симулирует руку+захват в 5 двигателях физики. Здесь живут все тесты и большинство информаторов.

<a id="commands"></a>
## Приказы

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

ИС (`.github/workflows/ci.yaml`): предварительное обязательство, XML/YAML валидация, `xacro ... sim_backend:=<backend> | check_urdf` для всех5задние стороны внутри `ros:humble` Контейнер, и самый красивый номер. Изменение УРФД должно оставаться действительным для **все** Задние направления, а не только те, на которые ты стремишься.

<a id="simulation-architecture"></a>
## Архитектура моделирования

Один параметризированный описание робота управляет каждым симулятором:

- `urdf/so_101.urdf.xacro` Единственный источник истины. Ксакроарг `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` выбирает `ros2_control` плагин (посредством `urdf/so_101.ros2_control.xacro`) во время расширения.
- `config/controllers.yaml` определяет одинаковые соединения/контроллеры для всех задних концов; `launch/sim.launch.py` с `sim:=<backend>` является единственной входной точкой.
- Робот:5-Рука DOF + захват с2призма, где левый клейм отражает правую сторону через `<mimic>`.
- Метки разделены: `meshes/visual/` (высокая поли) против `meshes/collision/` (конвексные корпуса, регенерированные с `scripts/generate_collision_meshes.py`).

Изменение названий соединений, ссылок или контроллеров обычно требует скоординированных редактирования по файлам xacro. `controllers.yaml`, и испытания в `test/`.

<a id="cad-models-and-part-numbering"></a>
## Модели CAD и нумерация деталей

Части в `models/parts/` использование Robonine частичные номера (например, `RB9.01.062.010 Main frame.STL`). Эти цифры упоминаются во всех `README.md` (типовая таблица), `docs/bom.md`, и `docs/assembly-guide.md` ⁇  Добавление или переименование части означает обновление этих документов. STL являются двойными; варианты кодируют толерантность соответствия в названии файла (например, `RB9.01.062.021 (D6.1) Clamp.STL` для разных диаметров палочки). Запретные крючки (белое пространство, EOF, концы линий) намеренно исключают `.stl/.STL/.STEP` файлы, и файлы более 1 МБ отклоняются `check-added-large-files`.

<a id="conventions"></a>
## Собрания

- Python: flake8 с `--max-line-length=100`, изортированный с черным профилем (применяется предварительным обязательством; `software/` и `examples/` исключаются из флаки8).
- Документы дублируются по конструкции (РЕДМ обобщает bom.md, specifications.md, assembly-guide.md⁇  сохранять их последовательность при изменении спецификаций, деталей или цен.
- Не добавлять `Co-Authored-By: Claude` Линия к обязательствам.
<!-- /translated-content -->
