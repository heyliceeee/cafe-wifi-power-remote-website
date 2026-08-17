# **Café Finder — Catalog for Remote‑Work Friendly Cafés**

Café Finder is a lightweight Flask frontend that displays a catalog of cafés ideal for remote work.  
It consumes an external REST API and presents the data through a clean, anime‑inspired UI built with Bootstrap and custom CSS.

The project focuses exclusively on **read‑only browsing**:  
no creation, editing, or deletion of cafés.

---

## **Features**

- Fetches café data from a REST API (`/all`)
- Displays all cafés in a responsive grid of clickable cards
- Each card opens a detailed café page
- Clean, pastel anime-inspired design
- Fully static frontend (no write operations to the API)
- Mobile-friendly layout

---

## **Tech Stack**

- **Flask** — routing and template rendering  
- **Jinja2** — dynamic HTML templates  
- **Bootstrap 5** — layout and components  
- **Bootstrap Icons** — iconography  
- **Noto Sans JP** — anime-style typography  
- **Custom CSS** — pastel gradients, card animations, and UI polish  
- **REST API** — external data source for cafés  