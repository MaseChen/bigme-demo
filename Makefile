up:
	docker compose up -d homeassistant

studio:
	docker compose --profile studio up -d

down:
	docker compose down

logs:
	docker compose logs -f homeassistant

logs-studio:
	docker compose logs -f appdaemon
