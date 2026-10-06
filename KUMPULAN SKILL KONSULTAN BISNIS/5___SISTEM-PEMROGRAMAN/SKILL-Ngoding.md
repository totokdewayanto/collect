---
name: universal-landing-page-architect
description: Skill terstandarisasi CHIPS-v2 untuk merancang dan menghasikan kode front-end landing page universal yang modern, responsif, dan fleksibel untuk berbagai jenis sistem atau produk web.
version: 1.0.0
tags: [frontend, landing-page, universal-template, chips-v2, web-architect]
---

# Universal Landing Page Architect Skill

Skill ini bertindak sebagai panduan operasional (SOP) dan meta-generator untuk membangun *front-end landing page* universal yang dapat diterapkan pada jenis aplikasi, sistem, maupun produk web apapun (SaaS, E-Commerce, Portal Informasi, Dashboard, Company Profile, dll).

---

## Overview & Execution Context

- **Primary Persona**: Master Web Front-End Architect & UI/UX Systems Designer.
- **Target Harnesses**: Claude Code, Codex CLI, Cursor, Copilot, OpenCode, Antigravity, Pi.
- **Input Requirements**: 
  - Nama produk/sistem & deskripsi nilai utama (*value proposition*).
  - Skema warna atau tema visual (*branding assets*).
  - Daftar fitur utama, testimoni, atau struktur navigasi yang diinginkan.
- **Primary Triggers**: `/generate-landing-page`, `/buat-landing-page`, `/landing-page-gen`, `[buatkan landing page universal]`

---

## Core Framework & Operational Formulas

### 1. Struktur Komponen Universal Landing Page
Setiap *landing page* universal disusun menggunakan blok modular standar berikut:
1. **Header & Navigation**: Logo, tautan navigasi semantik, dan tombol aksi (*CTA Primary*).
2. **Hero Section**: Judul utama (*headline*), sub-judul (*subheadline*), tombol *Call to Action* (CTA), serta elemen visual utama/mockup.
3. **Value Proposition / Benefits**: 3-4 kartu pilar keunggulan utama produk/sistem.
4. **Feature Showcase**: Demonstrasi fitur atau modul sistem secara interaktif/visual.
5. **Social Proof & Metrics**: Statistik kunci (kartu KPI), logo mitra, atau testimoni pengguna.
6. **Pricing / Package Matrix (Opsional)**: Tabel perbandingan paket atau tingkatan layanan.
7. **FAQ Accordion**: Pertanyaan umum dengan interaksi *toggle*.
8. **Final Call-to-Action (CTA) Banner**: Penutup kuat untuk mendorong konversi pengguna.
9. **Footer**: Hak cipta, navigasi sekunder, dan tautan media sosial.

### 2. Decision Tree / Logic Matrix

```
IF input menyertakan parameter branding/warna THEN
  -> Inisialisasi CSS Custom Properties (--primary, --accent, --bg, --text) di :root
ELSE
  -> Gunakan palette warna netral-modern default (Slate/Indigo theme)

IF jenis sistem adalah SaaS / Aplikasi Web THEN
  -> Tampilkan Hero Mockup + Statistik KPI + Fitur Interaktif + Pricing Matrix
ELSE IF jenis sistem adalah Company Profile / Service THEN
  -> Tampilkan Hero Video/Gambar + Services Grid + Testimoni + Form Kontak
ELSE
  -> Tampilkan Struktur Landing Page Universal Standard 8 Blok

IF file output tidak ditentukan secara spesifik THEN
  -> Generasi struktur 3-berkas flat tanpa bundler (index.html, style.css, script.js)
```

---

## Step-by-Step SOP (Execution Procedure)

### Step 1: Input Validation & Architecture Setup
1. Identifikasi nama produk/sistem, target audiens, dan tujuan utama konversi.
2. Tentukan variabel desain dasar: sistem font semantik, skala tipe spasial, dan *color palette*.
3. Pastikan struktur proyek menggunakan arsitektur *zero-build* 3 berkas utama (`index.html`, `style.css`, `script.js`).

### Step 2: HTML5 Semantic Markup Construction (`index.html`)
1. Gunakan tag semantik HTML5 (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`).
2. Terapkan atribut `id` dan `class` modular BEM (*Block Element Modifier*) atau utilitas semantik yang konsisten.
3. Pastikan seluruh tombol CTA dan tautan navigasi memiliki atribut *accessibility* (ARIA labels) yang lengkap.

### Step 3: CSS3 Design System & Responsive Layout (`style.css`)
1. Deklarasikan variabel warna, sistem tipografi, dan *spacing* pada blok `:root`.
2. Gunakan Flexbox dan CSS Grid untuk tata letak yang responsif secara *mobile-first*.
3. Sertakan *breakpoint* standar (`@media (max-width: 768px)` dan `@media (max-width: 1024px)`).
4. Terapkan efek visual halus (seperti *hover states*, transisi CSS, dan *box-shadow* modern).

### Step 4: Vanilla ES6+ Interactive Scripting (`script.js`)
1. Tambahkan fitur interaktif bawaan:
   - *Smooth scrolling* untuk navigasi internal.
   - *Mobile navigation toggle* (hamburger menu).
   - *Accordion toggle* untuk section FAQ.
   - *Dynamic stats counter* atau tab *switcher* fitur.
2. Gunakan `addEventListener` murni tanpa *inline event handlers* pada HTML (`onclick="..."`).

### Step 5: Quality Assurance & Optimization Gate
1. Verifikasi keterbacaan kontras warna (*WCAG compliance*).
2. Pastikan tidak ada dependensi eksternal yang rusak atau *script bundler* yang tidak diperlukan.
3. Validasi ketahanan responsif pada tampilan layar ponsel, tablet, dan desktop.

---

## Presentation & Output Formatting

Output hasil generasi wajib disajikan secara terstruktur dengan pembagian 3 berkas utama:

### 1. `index.html` (Kerangka Semantik)
```html
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Nama Sistem/Produk] - Landing Page</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <!-- Header Nav -->
  <header class="navbar">...</header>

  <!-- Hero Section -->
  <section class="hero">...</section>

  <!-- Features Section -->
  <section class="features">...</section>

  <!-- CTA & Footer -->
  <footer class="footer">...</footer>

  <script src="script.js" defer></script>
</body>
</html>
```

### 2. `style.css` (Sistem Desain Modern & Responsif)
```css
:root {
  --primary: #4f46e5;
  --primary-hover: #4338ca;
  --bg: #ffffff;
  --surface: #f8fafc;
  --text: #0f172a;
  --text-muted: #64748b;
  --border: #e2e8f0;
  --radius: 0.5rem;
}

/* Reset & Base Styling */
* { margin: 0; padding: 0; box-sizing: border-border; }
body { font-family: system-ui, -apple-system, sans-serif; color: var(--text); background: var(--bg); }

/* Responsive Grid & Utilities */
.container { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; }
```

### 3. `script.js` (Interaktivitas Native ES6+)
```javascript
document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Toggle
  // Smooth Scroll Navigation
  // Interactive Component Handlers
});
```

---

## Special Constraints & Quality Gates (DO NOTs)

- ❌ **DILARANG mengikat template pada satu domain spesifik**: Jangan gunakan istilah hardcoded khusus satu industri (seperti "stok", "inventaris", "pasien") kecuali diminta spesifik oleh pengguna.
- ❌ **DILARANG menggunakan alat pembangun / build tools**: Jangan sertakan `package.json`, Webpack, Vite, atau skrip kompilasi Node.js.
- ❌ **DILARANG memakai inline event listener**: Hindari penulisan `onclick="..."` atau `onsubmit="..."` di dalam tag HTML.
- ❌ **DILARANG menghasilkan layout non-responsif**: Setiap komponen wajib memiliki tampilan yang rapi baik di layar mobile (360px) maupun desktop (1200px+).
- ❌ **DILARANG mengabaikan hierarki tipografi**: Setiap halaman wajib memiliki tepat 1 tag `<h1>` pada bagian Hero.

---

## Sample Invocation & Usage

- `/generate-landing-page nama="SaaS Analytics" warna="indigo"`
- `/buat-landing-page "Portal Edukasi Online dengan fitur kursus, testimoni, dan FAQ"`
