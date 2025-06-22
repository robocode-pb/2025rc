const fs = require('fs');
const path = require('path');

const buildDir = process.argv[2] || './'; // Папка білда, передати як аргумент
const manifestPath = path.join(buildDir, 'manifest.json');
const swPath = path.join(buildDir, 'sw.js');
const indexPath = path.join(buildDir, 'index.html');

if (!fs.existsSync(indexPath)) {
  console.error(`index.html не знайдено в ${buildDir}`);
  process.exit(1);
}

// Функція створення manifest.json
function createManifest(gameName) {
  return {
    name: gameName,
    short_name: gameName,
    start_url: "./index.html",
    display: "standalone",
    background_color: "#000000",
    theme_color: "#1e1e1e",
    description: `${gameName} Unity WebGL Game as PWA`,
    icons: [
      {
        src: "TemplateData/favicon.ico",
        sizes: "64x64 32x32 24x24 16x16",
        type: "image/x-icon"
      }
    ]
  };
}

// Читаємо index.html
let html = fs.readFileSync(indexPath, 'utf8');

// Додаємо посилання на manifest в head, якщо нема
if (!html.includes('rel="manifest"')) {
  html = html.replace(
    /<\/head>/i,
    `  <link rel="manifest" href="manifest.json" />
  <meta name="theme-color" content="#1e1e1e" />
</head>`
  );
  console.log('Додано посилання на manifest у <head>');
} else {
  console.log('Manifest вже є у <head>, пропускаємо');
}

// Додаємо реєстрацію service worker перед </body>, якщо нема
if (!html.includes('navigator.serviceWorker.register')) {
  html = html.replace(
    /<\/body>/i,
    `<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('sw.js')
    .then(() => console.log('Service Worker зареєстровано'))
    .catch(err => console.log('Помилка реєстрації Service Worker:', err));
}
</script>
</body>`
  );
  console.log('Додано реєстрацію Service Worker');
} else {
  console.log('Service Worker реєстрація вже є, пропускаємо');
}

// Робимо резервну копію index.html
fs.writeFileSync(indexPath + '.bak', html, 'utf8');
console.log('Створено резервну копію index.html.bak');

// Записуємо оновлений index.html
fs.writeFileSync(indexPath, html, 'utf8');
console.log('Оновлено index.html');

// Отримаємо ім’я гри з назви папки білда
const gameName = path.basename(path.resolve(buildDir));

// Зберігаємо manifest.json
const manifest = createManifest(gameName);
fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), 'utf8');
console.log('Створено manifest.json');

// Створюємо sw.js з кешуванням файлів із Build/ папки
// Збираємо файли в кеш
const buildFilesDir = path.join(buildDir, 'Build');
let cacheFiles = [
  './',
  './index.html',
  './manifest.json'
];

if (fs.existsSync(buildFilesDir)) {
  const buildFiles = fs.readdirSync(buildFilesDir);
  buildFiles.forEach(f => {
    cacheFiles.push(`./Build/${f}`);
  });
} else {
  console.warn('Папка Build/ не знайдена, кешування Build файлів не додано');
}

const swContent = `const CACHE_NAME = '${gameName.toLowerCase()}-cache-v1';
const urlsToCache = ${JSON.stringify(cacheFiles, null, 2)};

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
    .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
    .then(response => response || fetch(event.request))
  );
});
`;

fs.writeFileSync(swPath, swContent, 'utf8');
console.log('Створено sw.js');

console.log('PWA файли додано успішно!');
