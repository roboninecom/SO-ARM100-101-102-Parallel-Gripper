<!-- translation-navigation -->
[English](../../../en/community/histology-slide-gripper/README.md) · [Русский](README.md) · [Español](../../../es/community/histology-slide-gripper/README.md) · [Français](../../../fr/community/histology-slide-gripper/README.md) · [Deutsch](../../../de/community/histology-slide-gripper/README.md) · [Português (Brasil)](../../../pt-BR/community/histology-slide-gripper/README.md) · [简体中文](../../../zh-CN/community/histology-slide-gripper/README.md) · [日本語](../../../ja/community/histology-slide-gripper/README.md) · [हिन्दी](../../../hi/community/histology-slide-gripper/README.md) · [العربية](../../../ar/community/histology-slide-gripper/README.md)

[Английский оригинал](../../../../../community/histology-slide-gripper/README.md)

[Русский](../../README.md)

> Полный машинный перевод; носители языка его ещё не проверяли. Изображения, код, CAD и исходные PDF общие. При неоднозначности используйте английский оригинал.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="histology-slide-gripper-community-mod"></a>
# Гистология Слайд-грипер (общинный модуль)

Общественный вариант SO-ARM100/101 Параллельный Захват [Михаил Виачеславов](https://github.com/histochemichael), адаптированный для гистологической и гистотехнологической автоматизации: мягкий подбор стандартных 75 x 25 мм микроскопических слайдов, слайд-окрашивающих диппер/раков, а также непосредственное визуализацию зацепки камерой.

<div align="center">

![Демо гистологии слайд-захват](../../../../../community/histology-slide-gripper/assets/histology-slide-gripper-demo.gif)

*SO-ARM100/101 параллельный захват с использованием специальных клеймов для обработки микроскопических слайдов и окрашивающего погрузчика/рака.*

</div>

<a id="what-changed-vs-the-base-gripper"></a>
## Что изменилось по сравнению с базовым захватом

| Дополнение | Описание |
|----------|-------------|
| Запчасти для слайдов микроскопа | Длинная, плоская геометрия клапа поддерживает прямое воспроизведение стандартных 75 x 25 мм микроскопных слайдов. |
| Руководство слайд-раком/загрузкой | Расстояние между скоплениями и концами включает в себя слайд-окрашивающие диперы/раки, такие как слайд-окрашивающий дипер Medicus Health, связанный ниже. |
| Угловый держатель Arducam | Печатный держатель нацелен на камеру USB с глобальным перекрытием Arducam в челюстках захватника для подробного мониторинга слайда и отбора стойки. |
| Полная сборка CAD | Полная печатная СТЛ и редактируемая сборка STEP [`cad/`](../../../../../community/histology-slide-gripper/cad). |

<a id="gallery"></a>
## Галерея

<div align="center">

| Однократный слайд-поиск | Окрашивающее подъемное устройство для погрузки | Вид подъемника Arducam |
|:-:|:-:|:-:|
| ![Сцепление с микроскопическим слайдом](../../../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg) | ![Ключ, выровненный с пластинным окрашивающим диппером](../../../../../community/histology-slide-gripper/assets/slide-gripper-staining-dipper.jpg) | ![Подъемник Arducam над челюстями захвата](../../../../../community/histology-slide-gripper/assets/arducam-holder-front.jpg) |

| Передний вид | Геометрия ящерицы | Изометрическая сборка |
|:-:|:-:|:-:|
| <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-front.png" alt="Front CAD view of the microscope slide gripper mod" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-side.png" alt="Angled CAD view showing the microscope slide jaw geometry" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-isometric.png" alt="Isometric CAD view of the full microscope slide gripper assembly" width="250"> |

</div>

<a id="cad-files"></a>
## Файлы CAD

| Файл | Формат | Использование |
|------|--------|-----|
| [`cad/the-parallel-microscope-slide-gripper.stl`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.stl) | СТЛ | Печатная полная сборка для микроскопа слайд-захваттора. |
| [`cad/the-parallel-microscope-slide-gripper.step`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.step) | Шаг | Изменимый источник CAD для полной сборки. |

<a id="add-on-bill-of-materials"></a>
## Дополнительный список материалов

Эти элементы являются специфическими для рабочего процесса слайда/рака и не являются частью базовой захвата [БОМ](../../docs/bom.md).

| Компонент | КТИ | Примечания | Ссылка |
|-----------|:---:|-------|------|
| Arducam 100fps Mono Global Shutter USB Камера, OV9281 | 1 | Камера, используемая с угловым держателем для наблюдения за скользком и стойкой вблизи челюстей. | [Amazon UK](https://www.amazon.co.uk/Arducam-Shutter-Distortion-Computer-Raspberry/dp/B0FXWWF55X) |
| Пластиковая дубка с ручкой | 1+ | Справочная окраска диппера/целевой стойки; предназначена для стандартных 75 x 25 мм слайдов. | [Медикус здоровье](https://www.medicus-health.com/slide-staining-dipper.html) |
| Параллельная микроскопическая слайд-захватка | 1 | Печать `the-parallel-microscope-slide-gripper.stl`; Файл STEP включен для редактирования. | [`cad/`](../../../../../community/histology-slide-gripper/cad) |

<a id="mujoco-simulation"></a>
## MuJoCo Симуляция

<div align="center">

![SO-ARM101 гистологический слайд-захват, работающий в MuJoCo](../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

*SO-ARM101 с гистологическим слайд-захватником, установленным и работающим в MuJoCo.*

</div>

Самостоятельный MuJoCo Модель 3.4.0 доступна в [`mujoco/`](mujoco/README.md). Включает в себя полное SO-ARM101 Модель, маши для захватления, самостоятельная тест-банка для захватления, сценарии построения и проверка безголовного захвата и подъема.

Из корня хранилища:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py
```

Используйте `sg_grip` контроль в MuJoCo зритель, чтобы открыть и закрыть челюсти. Смотрите [симуляция README](mujoco/README.md) для деталей модели, контроля, проверки и инструкций по восстановлению.

<a id="notes"></a>
## Примечания

- Фinger gripper предназначены для стандартных 75 x 25 мм микроскопных слайдов и слайд-окрашивающих дипер/раков.
- Сборка поддерживает визуализацию камеры на стороне челюстей захвата, чтобы камера могла наблюдать за слайдом и рекпаном.
- Сначала проверьте с помощью некритических слайдов и настройте печатный материал, наполнитель и силу захвата для вашего рабочего процесса.

<a id="links"></a>
## Ссылки

- 🎥 [Демо: слайд- и окрашивающий стойка (LinkedIn)](https://www.linkedin.com/posts/michael-viacheslavov_histology-histotechnology-robotics-ugcPost-7482570199859240960-Gqpw/)
<!-- /translated-content -->
