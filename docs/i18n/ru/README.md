<!-- translation-navigation -->
[English](../en/README.md) · [Русский](README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [हिन्दी](../hi/README.md) · [العربية](../ar/README.md)

[Английский оригинал](../../../README.md)

[Русский](README.md)

> Полный машинный перевод; носители языка его ещё не проверяли. Изображения, код, CAD и исходные PDF общие. При неоднозначности используйте английский оригинал.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm100101-parallel-gripper"></a>
# SO-ARM100/101 Параллельный захват

<div align="center">

[![SO-ARM101 Параллельный захват](../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

**🎥 [Посмотрите, как работает захват!](https://youtube.com/shorts/bSyXjgNGXZk)**

Лёгкий параллельный захват для 3D-печати, разработанный **[Robonine](https://robonine.com)** для open-source SO-ARM100/101 робототехническая платформа.

[![Оборудование: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt)
[![Программное обеспечение Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt)
[![Документы: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt)
[![Стоимость: ~$70](https://img.shields.io/badge/Cost-~%2470-green.svg)](docs/bom.md)
[![Сборка: 30 минут](https://img.shields.io/badge/Assembly-30%20min-orange.svg)](docs/assembly-guide.md)

---

**Вопросы? Мы здесь, чтобы помочь!**
⁇  Электронная почта: [hello@robonine.com](mailto:hello@robonine.com)

</div>

---

<a id="-key-features"></a>
## ✨ Ключевые особенности

| Особенность | Описание |
|---------|-------------|
| **120N Прицепная сила** | Надежный параллельный механизм челюсти |
| **14 мм/с Скорость** | Скорость работы сцепления |
| **84 мм полный удар** | Широкое открытие для различных объектов |
| **0.5mm Повторяемость** | Высокая точность позиционирования |
| **Камера совместима** | Поддержка RealSense, Orbbec, камеры USB |
| **3D-печать** | Все части печатаются на стандартных принтерах FDM |
| **~ $62 Общая стоимость** | Доступное решение с открытым исходным кодом |
| **Легкая сборка** | 30-45 минут с основными инструментами |

---

<a id="-gallery"></a>
## ⁇  Галерея

<div align="center">

<a id="gripper-on-so-arm101"></a>
### Захват на SO-ARM101

![Захват, установленный на SO-ARM101](../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*Гриптер следового устройства, интегрированный с SO-ARM101 роботская рука*

<a id="dimensions"></a>
### Размеры

![Размеры захвата](../../../assets/images/specification/08-gripper-dimensions-3d.png)

*128 × 109 × 130.5мм, полный удар84Мм*

</div>

---

<a id="-specifications"></a>
## ⁇  Спецификации

<a id="gripper-parameters"></a>
### Параметры захвата

| Параметр | Значение |
|-----------|-------|
| Максимальная сила похватывания | **120 N** |
| Максимальная скорость захвата | **14 мм/с** |
| Полный удар | **84 мм** |
| Повторяемость | **0.5Мм** |
| Масса сборки (PLA, 30% наполнения) | **170 g** |
| ДОФ | **1** |

<a id="dimensions-1"></a>
### Размеры

| Размер | Значение |
|-----------|-------|
| Ширина | 128 мм |
| Глубина | 130.5Мм |
| Высота | 109 мм |

<a id="servo-parameters-feetech-sts3215"></a>
### Серво параметры (Feetech STS3215)

| Параметр | Значение |
|-----------|-------|
| Операционное напряжение | 12V |
| Крутящий момент при остановленном валу | 30 кг·см |
| Скорость (без нагрузки) | 45 оборотов в минуту |
| Кодировщик | Абсолютная магнитная 12-битная |
| Протокол | RS485/TTL до 1 Мбит/с |
| Операционная температура | -20°C ~ 60°C |

---

<a id="-camera-compatibility"></a>
## ⁇  Совместимость с камерой

Захват поддерживает несколько камер с помощью совместимого держателя камеры:

| Камера | Тип | Случай использования |
|--------|------|----------|
| IMX335 5MP USB | РГБ | Основные задачи по видению |
| GC2093 2MP USB | РГБ | Бюджетный вариант |
| Orbbec Близнецы 2 | RGB-D | 3D восприятие |
| RealSense D405 | RGB-D | Глубина близкого диапазона |
| RealSense D435/D435i | RGB-D | Общие цели |
| RealSense D455 | RGB-D | Глубина на длинном расстоянии |

<div align="center">

![Различные камеры, установленные на захват](../../../assets/images/specification/09-camera-types.png)

*RealSense, модуль камеры USB, Orbbec Близнецы 2*

</div>

---

<a id="-bill-of-materials"></a>
## ⁇  Документ о материалах

**Общая стоимость: ~ $62** ([Полный BOM с Amazon ссылки](docs/bom.md))

| Категория | Компоненты | Восточная. Стоимость |
|----------|------------|-----------|
| Электроника | Feetech STS3215 Серво + серво-автобусный адаптер | ~$40 |
| Подшипники | MF106ZZ (x2) | ~$2 |
| Алюминиевые/углеродные трубы | D6x1x125 мм (x2) | ~$4 |
| 3D-печать | 8 частей (~100-150 г PLA) | ~$12 |
| Крепёж | Винты M2/M4, гайки M2, установочные винты M3 | ~$3 |

---

<a id="-quick-start"></a>
## ⁇  Быстрый старт

<a id="1-print-the-parts-2-4-hours"></a>
### 1. Печать части (2-4 часа)

Загрузить файлы STL из [`models/parts/`](models/README.md). Совместим с популярными принтерами, такими как **Лаборатория бамбу А1 мини**, **Пруза MINI+**, и любой принтер с постелью ≥180×180 мм.

| Часть | КТИ | Настройки |
|------|:---:|----------|
| Основная рама (RB9.01.062.010) | 1 | 20% наполнения |
| Зажим (RB9.01.062.020) | 2 | 20% наполнения |
| Зубчатая рейка (RB9.01.062.030) | 2 | 100% наполнитель |
| Шестерня (RB9.01.062.040) | 1 | 100% наполнитель |
| Держатель камеры (RB9.01.060.074) | 1 | 20% наполнения |
| Держатель (RB9.01.060.080) | 1 | 20% наполнения |
| Проставка камеры (RB9.01.060.090) | 1 | 20% наполнения |
| D405 держатель (RB9.01.060.110) | 1 | 20% наполнения |

<a id="2-order-components-1-2-days"></a>
### 2. Компоненты заказа (1-2 дня)

Посмотрите . [Сборник материалов](docs/bom.md) для прямых ссылок на Amazon.

<a id="3-assemble-30-45-minutes"></a>
### 3. Собрание (30-45 минут)

Следуйте [Руководство по собранию](docs/assembly-guide.md) с поэтапными изображениями:

1. Закрепите шестерню на диске сервопривода и установите сборку на сервопривод
2. Вставить сервокабель
3. Использование Feetech Программное обеспечение перемещает серво на минимальное положение (переместить пластинку в программном обеспечении влево)
4. Прикрепите зубчатые рейки к зажимам
5. Вставьте направляющие стержни в оба зажима
6. Установите подшипники в основную раму и закрепите винтами
7. Защёлкните направляющие стержни в раме
8. Разведите зажимы в крайние левое и правое положения
9. Установите сервопривод и закрепите винтами
10. Установите проставку и UVC-камеру; используйте 4x винта и гайки M2 (необязательно)
11. Установите на манипулятор (необязательно)

<a id="4-software"></a>
### 4. Программное обеспечение

```bash
# Configure servo motor if necessary
https://lab.robonine.com/tools/robonine/feetech-bus

# Control gripper
https://lab.robonine.com/tools/robonine/control-robot
```

---

<a id="-repository-structure"></a>
## ⁇  Структура хранилища

```
├── assets/
│   └── images/
│       ├── assembly/          # Assembly step images
│       └── specification/     # Technical drawings
├── docs/
│   ├── assembly-guide.md                # Step-by-step assembly
│   ├── bom.md                           # Bill of materials with links
│   ├── Parallel gripper by Robo9.pdf    # Gripper product specification
│   ├── quick-start.md                   # Getting started guide
│   ├── SO-ARM101 by Robo9.pdf           # SO-ARM101 product specification
│   └── specifications.md               # Technical specifications
├── models/
│   ├── parts/                                    # Individual STL files
│   └── Follower gripper (165x165 bed size).STL   # Complete assembly (165×165mm bed)
├── community/
│   └── histology-slide-gripper/   # Community variant (CAD, MuJoCo model)
├── simulation/
│   ├── README.md                  # Simulation overview
│   ├── gazebo/                    # Gazebo guide
│   ├── mujoco/                    # MuJoCo guide
│   ├── webots/                    # Webots guide
│   ├── coppeliasim/               # CoppeliaSim guide
│   ├── isaac_sim/                 # Isaac Sim guide
│   └── so_arm_101_description/    # ROS2 package (URDF, launch, Docker)
├── software/
│   └── python/                # Control software
├── examples/                  # Usage examples
├── HARDWARE-LICENSE.txt       # CERN-OHL-P-2.0 (CAD, geometry)
├── SOFTWARE-LICENSE.txt       # Apache-2.0 (code)
├── DOCS-LICENSE.txt           # CC BY 4.0 (docs, images)
├── LICENSING.md               # Which licence covers what
├── NOTICE                     # Third-party attribution
├── REUSE.toml                 # Machine-readable licence map
├── RELICENSING.md             # Record of the 2026 relicensing
└── CONTRIBUTING.md
```

---

<a id="-documentation"></a>
## ⁇  Документация

| Документ | Описание |
|----------|-------------|
| [Быстрое руководство по запуску](docs/quick-start.md) | Беги через 30 минут. |
| [Руководство по собранию](docs/assembly-guide.md) | Шаг за шагом с изображениями |
| [Руководство по сборке захватов (PDF)](../../Assembly%20Guide%20Follower%20Gripper.pdf) | Инструкции по монтажу печатного захватника |
| [SO-ARM101 Руководство по собранию (PDF)](../../Assembly%20Guide%20SO-ARM101.pdf) | Полное SO-ARM101 инструкции по монтажу рук |
| [Сборник материалов](docs/bom.md) | Список деталей с ссылками на Amazon |
| [Спецификации](docs/specifications.md) | Технические подробности |
| [3D-модели](models/README.md) | Печать настройки и файлы |
| [Спецификации продукта параллельного грипера (PDF)](../../Parallel%20gripper%20by%20Robo9.pdf) | Спецификация продукта параллельного захватного устройства от Robo9 |
| [SO-ARM101 Спецификация продукта (PDF)](../../SO-ARM101%20by%20Robo9.pdf) | SO-ARM101 Спецификация продукта робот-руки от Robo9 |

---

<a id="-hardware-requirements"></a>
## ⁇  Требования к оборудованию

<a id="electronics"></a>
### Электроника
- 1× Feetech STS3215 Сервомотор
- 1× Автобусная сервоадаптерная панель (Waveshare)

<a id="mechanical"></a>
### Механические
- 2× MF106ZZ Подшипники (6×10×3 мм)
- 2× Алюминиевые/углеродные трубы D6x1×125 мм

<a id="fasteners"></a>
### Крепёж
- 2 × M4 × 8 винтов DIN 7991
- 4x M2x8 DIN 912 винтовки
- 4× M2 DIN 934 орехи
- 4× M3×4 DIN 913 наборы винтов

<a id="tools-required"></a>
### Необходимые инструменты
- Крестовая отвёртка (PH1)
- Шестигранные ключи M2 (H1.5) и M4 (H2.5)

---

<a id="-simulation"></a>
## ⁇ ️ Симуляция

SO-ARM101 можно моделировать в 5 физических движках с помощью пакета описания ROS2 и единого параметризованного URDF. Установка ROS2 не требуется — всё запускается через Docker.

<div align="center">

| Gazebo (Огневая крепость) | MuJoCo |
|:-:|:-:|
| ![SO-ARM-101 в Gazebo](../../../assets/images/simulation/gazebo/gazebo_pick_place.png) | ![SO-ARM-101 в MuJoCo](../../../assets/images/simulation/mujoco/mujoco_pick_place.png) |

</div>

| Симулятор | Статус | Докер |
|-----------|--------|--------|
| [Gazebo](simulation/gazebo/README.md) | Готов. | `docker compose run gazebo` |
| [MuJoCo](simulation/mujoco/README.md) | Готов. | `docker compose run mujoco` |
| [Webots](simulation/webots/README.md) | Нестабильный | `docker compose run webots` |
| [CoppeliaSim](simulation/coppeliasim/README.md) | Не проверено | Внешний симулятор |
| [НВИДИЯ Isaac Да , да .](simulation/isaac_sim/README.md) | Не проверено | Внешний симулятор |

**Быстрый старт (Docker):**

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

Смотрите [Руководство по моделированию](simulation/README.md) для полного настройки, архитектурных деталей и командования роботом.

---

<a id="-community-mods"></a>
## ⁇  Моды Сообщества

Варианты сцепления, построенные сообществом, каждая самостоятельная [`community/`](../../../community):

| Мод | Автор | Описание |
|-----|--------|-------------|
| [Гистология Слайд-захват](community/histology-slide-gripper/README.md) | [Михаил Виачеславов](https://github.com/histochemichael) | Ключи для слайдов микроскопа 75 x 25 мм и окрашивающих дипер/раков, а также угловой держатель Arducam для мониторинга хвата. |

<div align="center">

<a href="community/histology-slide-gripper/README.md"><img src="../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg" alt="Histology slide gripper mod holding a microscope slide" width="400"></a>

*Histology Slide Gripper mod  ⁇  нажмите для полного описания, файлов CAD и демо*

</div>

---

<a id="-contributing"></a>
## ⁇  Содействие

Мы приветствуем пожертвования! Пожалуйста , не стесняйтесь:
- ⁇  Отчет о ошибках и проблемах
- ⁇  Предложить новые функции
- ⁇  Подача запросов на вывод
- Улучшение документации

---

<a id="-license"></a>
## ⁇  Лицензия

Авторское право (c) 2025 Robonine. Этот проект имеет несколько лицензий  ⁇  различные виды
материалы имеют разные лицензии:

| Материал | Лицензия |
|---|---|
| Дизайн оборудования  ⁇ `models/`, общественный CAD, сетки сцепления | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| Программное обеспечение `software/`, `examples/`, `simulation/`, код моделирования в `community/` | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| Документация и изображения `docs/`, `assets/`, все `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

Посмотрите . [`LICENSING.md`](LICENSING.md) для точной карты файла по файлу и
[`REUSE.toml`](../../../REUSE.toml) для машиночитаемой версии.

**Не все здесь RobonineЭто работа.** В. SO-ARM101 извлекаются ручные сетки
от [TheRobotStudioПроект вверх по течению](https://github.com/TheRobotStudio/SO-ARM100)
и остаться Apache-2.0; гистологический слайд-захват привел
[@histochemichael](https://github.com/histochemichael). Посмотрите . [`NOTICE`](../../../NOTICE)
перед повторным использованием любой сетки.

Освобождения до и включая `v0.3.1` были опубликованы в соответствии с GPL-3.0 и остаются
доступны в этих условиях  ⁇  см. [`RELICENSING.md`](RELICENSING.md).

---

<a id="-links"></a>
## ⁇  Ссылки

- [Feetech STS3215 Серво](https://www.feetechrc.com/525603.html)
- [Waveshare Автобусный сервоадаптер](https://www.waveshare.com/bus-servo-adapter-a.htm)
- [STServo Python SDK](https://github.com/FEETECH-RC/STServo_SDK_Python)

---

<a id="-engineering-team"></a>
## ⁇  Инженерная команда

| Название | Роль | Контакт |
|------|------|---------|
| **Борис Котов** | Инженер программного обеспечения | [Телеграмм](https://t.me/bkotov) |
| **Алан Субин** | Инженер по проектированию | [Ссылка на LinkedIn](https://www.linkedin.com/in/alan-subin/) |

---

<div align="center">

**Построен для робототехники сообщества [Robonine](https://robonine.com)** 🤖

**Вопросы? Мы здесь, чтобы помочь!**
⁇  Электронная почта: [hello@robonine.com](mailto:hello@robonine.com)

</div>
<!-- /translated-content -->
