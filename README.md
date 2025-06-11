# Fire & Fork

Premium flame‑kissed dining experience. This repo contains the full stack application built with Next.js and Django.

## Prerequisites

- **Node.js 20**
- **pnpm** package manager (`npm i -g pnpm`)
- **Docker v26** and **docker-compose**

## Quick Start

1. Copy `.env.example` to `.env` and fill in secrets.
2. Run the stack:

```bash
docker-compose up --build
```

Frontend runs on `http://localhost:3000` and backend API on `http://localhost:8000`.

## Repository Structure

```
.github/workflows/    # CI configuration
frontend/             # Next.js 14 app
  app/                # App Router
  components/
  lib/
  public/
  tailwind.config.ts
backend/
  fireandfork/        # Django project
  apps/
    menu/
    orders/
    reservations/
Dockerfile            # For backend and frontend (within folders)
docker-compose.yml    # Local development stack
```

## Development

- Frontend uses **Next.js 14**, **Tailwind CSS** and **shadcn/ui** components.
- Backend is **Django 4.2** with **Django REST Framework**.
- Postgres 16 is used for persistence.

Run tests via GitHub Actions or locally:

```bash
# Backend
cd backend
pip install -r requirements.txt
python manage.py test
```

```bash
# Frontend
cd frontend
pnpm install
pnpm build
```

## Deployment

Preview deployments are set up using **Netlify** (frontend) and **Fly.io** (backend). On each pull request a preview will be built automatically.

1. Push your branch to GitHub.
2. Netlify will build the frontend and provide a unique preview URL.
3. Fly.io will deploy the API for testing.

## Environment Variables

See `.env.example` for all required configuration including Cloudinary, Twilio and Resend credentials.

### Pull Request Previews

This project uses **Netlify** for frontend previews and **Fly.io** for the backend.
When you open a pull request, GitHub Actions will build and deploy both services.
Links to the temporary preview URLs will appear automatically in the PR checks.
