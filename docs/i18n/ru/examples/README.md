<!-- translation-navigation -->
[English](../../en/examples/README.md) · [Русский](README.md) · [Español](../../es/examples/README.md) · [Français](../../fr/examples/README.md) · [Deutsch](../../de/examples/README.md) · [Português (Brasil)](../../pt-BR/examples/README.md) · [简体中文](../../zh-CN/examples/README.md) · [日本語](../../ja/examples/README.md) · [हिन्दी](../../hi/examples/README.md) · [العربية](../../ar/examples/README.md)

[Английский оригинал](../../../../examples/README.md)

[Русский](../README.md)

> Полный машинный перевод; носители языка его ещё не проверяли. Изображения, код, CAD и исходные PDF общие. При неоднозначности используйте английский оригинал.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="examples---parallel-gripper"></a>
# Примеры - параллельный сцепник

В этом каталоге есть примерный код, показывающий, как использовать параллельный захват в различных сценариях.

<a id="available-examples"></a>
## Доступные примеры

<a id="basic_usagepy"></a>
### `basic_usage.py`
Продемонстрирует основные действия захвата:
- Подключение к захватке
- Переход на конкретные позиции
- Информация о состоянии чтения
- Основное обращение с ошибками

**Использование:**
```bash
cd examples
python basic_usage.py
```

<a id="configuration"></a>
## Конфигурация

Прежде чем запустить примеры, вам может потребоваться скорректировать параметры конфигурации:

```python
config = GripperConfig()
config.DEVICENAME = '/dev/ttyUSB0'  # Linux/Mac
# config.DEVICENAME = 'COM7'        # Windows
config.STS_ID = 1                   # Servo ID
config.BAUDRATE = 1000000          # Communication speed
```

<a id="common-issues"></a>
## Общие вопросы

<a id="connection-problems"></a>
### Проблемы со связью
- **Окна**: Проверяйте Управляющий устройством для правильного порта COM
- **Linux**: Убедитесь, что пользователь имеет доступ к серийным портам (`sudo usermod -a -G dialout $USER`)
- **macOS**Использование: `/dev/cu.usbserial-*` или `/dev/tty.usbserial-*`

<a id="permission-errors"></a>
### Ошибки в разрешении
```bash
# Linux/macOS
sudo chmod 666 /dev/ttyUSB0
# or add user to dialout group
sudo usermod -a -G dialout $USER
```

<a id="stservo-sdk-issues"></a>
### STServo Проблемы SDK
Убедитесь, что STServo SDK установлен правильно:
1. Скачать из: [STServo Python SDK](https://files.waveshare.com/wiki/Bus-Servo-Adapter-(A)/STServo_Python.zip)
2. Извлечь загруженный файл ZIP и скопировать `STservo_sdk` папка (с самой папкой) к `software/python/` справочник

<a id="creating-your-own-examples"></a>
## Создайте свои собственные примеры

При создании новых примеров:

1. **Импортировать модуль сцепления**
   ```python
   from gripper_control import ParallelGripper, GripperConfig
   ```

2. **С грациозностью справляйтесь с ошибками**
   ```python
   try:
       gripper = ParallelGripper()
       if not gripper.connect():
           print("Connection failed!")
           return
       # Your code here
   finally:
       gripper.disconnect()
   ```

3. **Включить надлежащую документацию**
   - Ясный описание того, что делает пример
   - Необходимая настройка оборудования
   - Ожидаемое поведение

<a id="safety-notes"></a>
## Заметки о безопасности

⚠️ **Важные соображения безопасности:**
- Всегда следите за температурой и потоком
- Реализация правильного обращения с ошибками
- Сначала испытание с низкими силами
- Обеспечить правильную механическую установку
- Держите пальцы в стороне от движущихся частей

<a id="contributing-examples"></a>
## Примеры, способствующие

Мы приветствуем новые примеры! Прошу вас:
- Следуйте существующему стилю кода
- Включить всеобъемлющие замечания
- Перед подачей тщательно проверить
- Добавить запись в данный README

---

**Счастливая кодировка!** 🤖
<!-- /translated-content -->
