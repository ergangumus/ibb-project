Carpark Managment System

Bu proje, Django Rest Framework tabanlı bir backend ve React tabanlı bir frontend içeren bir harita gösterimi uygulamasıdır.

Proje Alanları
 Proje iki ana alanda yürütülmektedir:

1. Backend (Django Rest Framework)
2. Frontend (React)


Özellikler

Backend
- Django Rest Framework ile REST API hizmetleri sağlanmaktadır.
- django-import-export ile veri import/export işlemleri yapılmaktadır.
- Backend ortamı Docker kullanılarak ayağa kaldırılmaktadır.

Frontend
- Harita gösterimi için Maplibre kullanılmaktadır.
- Harita verileri, MapTiler Streets Stili üzerinden yüklenmektedir.
- Frontend tarafı npm kullanılarak başlatılmaktadır.

Kurulum

Gereksinimler
- Docker ve Docker Compose kurulu olmalıdır.
- npm kurulumu gerekmektedir (frontend için).

Backend Kurulumu

Docker Compose kullanarak backend’i ayağa kaldırın:
- docker-compose up --build

ispark-frontend Kurulumu
- cd ispark-frontend

NPM ile bağımlılıkları yükleyin:
- npm install

Uygulamayı başlatın:
- npm start


Kullanım

Backend Komutları

Migration oluşturma:
- docker-compose run --rm app sh -c "python manage.py makemigrations"

Migration’ları uygulama:
- docker-compose run --rm app sh -c "python manage.py migrate"

Testlerin çalıştırılması:
- docker-compose run --rm app sh -c "python manage.py test"

Teknolojiler

Backend:

- Django Rest Framework
- django-import-export
- Docker ve Docker Compose

Frontend:
- React
- Maplibre
- MapTiler
