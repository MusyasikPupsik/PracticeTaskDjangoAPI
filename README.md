# Django REST API - Полная реализация ролевой модели доступа

Проект представляет собой полноценный REST API, построенный на базе Django и Django REST Framework (DRF). Архитектура полностью покрывает все 23 сущности структуры базы данных и реализует строгое разграничение доступа на уровне отдельных объектов (Object-level permissions).

## 🔐 Реализованная ролевая модель
Контроль доступа динамически интегрирован с таблицами `ProjectMembership`, `TeamMembership` и `Curator`:
1. **Просмотр (`viewer`)** — Доступ только к безопасным методам чтения (`GET`, `HEAD`, `OPTIONS`). Любые попытки изменения данных (`POST`, `PUT`, `PATCH`, `DELETE`) блокируются системой с ответом `403 Forbidden`.
2. **Редактирование (`editor` / `owner`)** — Полный доступ ко всем CRUD-операциям в рамках своих проектов.
3. **Кураторы (`Curator`)** — Обладают глобальными административными правами доступа ко всем веткам данных.

## 🔑 Аутентификация
Внедрена строгая JWT-аутентификация (`django-rest-framework-simplejwt`). Все эндпоинты закрыты глобально и требуют передачи токена в заголовках запроса.

## 📂 Полный перечень эндпоинтов API (23 сущности)
* `/api/auth/token/` — Получение JWT-токена (вход для фронтенда)
* `/api/auth/token/refresh/` — Обновление JWT-токена
* `/api/users/` — Управление пользователями
* `/api/projects/` — Проекты
* `/api/hypotheses/` — Гипотезы
* `/api/actions/` — Действия по гипотезам
* `/api/data/` — Данные гипотез
* `/api/insights/` — Инсайты
* `/api/teams/` — Команды
* `/api/project-memberships/` — Управление членством в проектах
* `/api/team-memberships/` — Управление членством в командах
* `/api/curators/` — Реестр кураторов
* `/api/hypothesis-statuses/` — Статусы гипотез
* `/api/hypothesis-metrics/` — Метрики гипотез
* `/api/hypothesis-metric-values/` — Значения метрик
* `/api/assistant-functions/` — Функции ИИ-ассистента
* `/api/requests-to-assistant/` — Запросы к ассистенту
* `/api/chats-with-assistant/` — Чаты с ассистентом
* `/api/openai-history/` — Лог истории OpenAI
* `/api/hypothesis-content-versions/` — Версионирование контента гипотез
* `/api/action-content-versions/` — Версионирование действий
* `/api/data-content-versions/` — Версионирование данных
* `/api/insight-content-versions/` — Версионирование инсайтов
* `/api/user-actions/` — Лог действий пользователей
* `/api/global-properties/` — Глобальные системные свойства
* `/api/project-changes-summaries/` — Саммари изменений проектов
* `/api/hypothesis-changes-summaries/` — Саммари изменений гипотез
* `/api/action-changes/` — Изменения действий
* `/api/data-changes/` — Изменения данных
* `/api/insight-changes/` — Изменения инсайтов
* `/api/metric-changes/` — Изменения метрик
* `/api/user-settings/` — Настройки пользователей

## 🚀 Как протестировать ролевую схему локально
1. Установите зависимости: `pip install -r requirements.txt`
2. Выполните миграции: `python manage.py migrate`
3. Создайте суперпользователя: `python manage.py createsuperuser`
4. Запустите сервер: `python manage.py runserver`
5. Перейдите в панель администратора http://localhost:8000/admin/ и добавьте проект, а также запись в **Project memberships**, привязав вашего пользователя с ролью `viewer`.
6. Перейдите на страницу инстанса http://localhost:8000/api/projects/1/ и попробуйте отправить запрос `PUT` или `DELETE`. Система заблокирует действие с ошибкой `"You do not have permission to perform this action."`.
