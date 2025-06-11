# API Contract

All endpoints are prefixed with `/api/`.

## Menu
- `GET /api/menu/` list items
- `POST /api/menu/` create item (admin)

## Orders
- `POST /api/orders/` create new order
- `GET /api/orders/<id>/` retrieve order (auth required)

## Reservations
- `GET /api/reservations/availability/<date>/` check slot availability
- `POST /api/reservations/` create a reservation
