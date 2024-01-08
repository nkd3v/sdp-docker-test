# SDP Docker Assignment

Start dev server: `docker compose up --build`

Start test server: `docker compose -f compose.test.yaml up --build`

Shutdown dev server: `docker compose down`

Shutdown test server: `docker compose -f compose.test.yaml down`

Shutdown dev server and remove dev volume: `docker compose down -v`

Shutdown test server and remove test volume: `docker compose -f compose.test.yaml down -v`