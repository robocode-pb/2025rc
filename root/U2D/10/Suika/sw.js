const CACHE_NAME = 'suika-cache-v1';
const urlsToCache = [
  "./",
  "./index.html",
  "./manifest.json",
  "./Build/Build.data",
  "./Build/Build.framework.js",
  "./Build/Build.loader.js",
  "./Build/Build.wasm"
];

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
