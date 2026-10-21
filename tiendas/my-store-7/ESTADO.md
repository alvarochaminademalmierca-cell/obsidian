# ESTADO — My Store 7

- **Tienda:** My Store 7 — `tczi3w-uv.myshopify.com`
- **Tema EN VIVO:** "My Store 7 – New Design (EN)" — `gid://shopify/OnlineStoreTheme/202256875903` (publicado por el usuario)
- **Tema de trabajo (NO publicado):** "My Store 7 – v2 (offer picker)" — `gid://shopify/OnlineStoreTheme/202257957247`
- **Previsualización v2:** https://tczi3w-uv.myshopify.com/products/smart-automatic-pet-feeder?preview_theme_id=202257957247
- **Tema antiguo:** Helio — `gid://shopify/OnlineStoreTheme/201844982143`
- Nota: el tema en vivo no se puede editar por API; cada cambio = duplicar, editar la copia y que el usuario la publique.
- **Fase completada:** 5 (construcción + producto). Falta: revisión del usuario y publicar el tema (fase 6, lo hace el usuario desde el panel: Tienda online → Temas → Publicar).

## Productos
| Producto | ID | Handle | Plantilla | Precio NA |
|---|---|---|---|---|
| Smart Laser Cat Toy & Pet Camera | 16031483330943 | smart-laser-cat-toy-camera | product.mt-laser | 150 USD |
| Smart Automatic Pet Feeder (4L) | 16031483429247 | smart-automatic-pet-feeder | product.mt-feeder | 85 USD (todas las variantes) |

- Títulos, descripciones, SEO, opciones de variantes reescritos en inglés (redirecciones desde los handles antiguos creadas).
- Opciones del comedero: "Bowl" (Stainless Steel Bowl / Standard (No Steel Bowl)) y "Model" (15 valores limpios).

## Mercados, precios y envíos
- **Precio único mundial:** 85 USD comedero / 150 USD láser. Lista `Worldwide USD` asignada a los mercados North America, International (resto del mundo) y Spain (base USD, monedas locales → ES ≈ 133,57 € / 75,69 €, UK 115 £ / 65 £, CA 215 / 122 CAD).
- Mercado **International** — `gid://shopify/Market/115741884799`.
- Mercado **North America** (US, CA, MX) — `gid://shopify/Market/115741327743`, moneda base USD, monedas locales activas.
- Lista de precios fija **North America USD** — `gid://shopify/PriceList/37763809663` (catálogo `gid://shopify/MarketCatalog/191855296895`).
- Zona de envío **North America** (US, CA, MX): "Free Tracked Shipping" 0 €. US y CA se sacaron de la zona "Internacional".
- España/UE: sin cambios (precios en EUR originales).

## Descuento
- Automático **"Bundle & Save 20%"** — `gid://shopify/DiscountAutomaticNode/2649780257151`: 20% en los 2 productos con mínimo 2 unidades de esos productos (también aplica a 2 unidades del mismo producto).

## Secciones creadas (prefijo mt-)
- `mt-announcement` (barra superior en header-group), `mt-hero`, `mt-trust-bar`, `mt-products`, `mt-bundle`, `mt-feature`, `mt-guarantee`, `mt-faq`, `mt-product` (página de producto: galería, variantes, urgencia, upsell bundle, confianza, acordeones, barra fija móvil).
- `snippets/mt-icon.liquid`, `assets/mt-styles.css`, `assets/mt-scripts.js`.
- Plantillas: `templates/index.json`, `templates/product.mt-laser.json`, `templates/product.mt-feeder.json` (generadas con `theme/generar-plantillas.py`).
- `sections/header-group.json` (header blanco, sin transparencia) y `sections/footer-group.json` (textos en inglés, sin redes sociales de ejemplo).

## Urgencia (todo real / editable)
- Stock bajo: solo aparece si el stock real de la variante ≤ 15.
- Cuenta atrás hasta la hora de corte diaria (16:00 hora local del cliente) para "processed today".
- Mensaje de temporada navideña (editable).
- No se han puesto reseñas ni contadores de "personas viendo" inventados (prohibido por la FTC en EE. UU.).

## Páginas
- `/pages/shipping` y `/pages/returns` creadas y en el menú principal.
- Menú principal: Home, Smart Feeder, Laser Cat Toy, Shipping, Returns, Contact.

## Pendientes / decisiones del usuario
- Pegar las políticas legales (Refund, Shipping, Terms) en Ajustes → Políticas (sin permiso para escribirlas por API).
- Confirmar plazos de envío (7–15 días hábiles) y garantía de 30 días.
- Nombre de marca y logo (ahora sale "My Store 7").
- Publicar el tema cuando dé el visto bueno.

## v2 página de producto
- Mensajes de urgencia arriba del todo (stock real, cuenta atrás, temporada).
- Selector de oferta "Just this one" / "Bundle & save 20%" (preseleccionado) justo bajo el precio; al lado de las fotos en ordenador y bajo las fotos en móvil (galería 4:3 en móvil para que se vea antes).
- El botón principal añade el producto solo o el pack completo. Estilos en `assets/mt-offers.css`.
