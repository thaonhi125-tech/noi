import { getAssetFromKV } from '@cloudflare/kv-asset-handler';

addEventListener('fetch', (event) => {
  event.respondWith(handleEvent(event));
});

async function handleEvent(event) {
  try {
    // Serve static assets from the KV namespace
    return await getAssetFromKV(event, {
      // You can add custom logic here, like caching headers
    });
  } catch (e) {
    // If the asset is not found, you can return a 404 page
    // or fall back to your single-page application's index.html
    try {
      let pathname = new URL(event.request.url).pathname;
      let notFoundResponse = await getAssetFromKV(event, {
        mapRequestToAsset: (req) => new Request(`${new URL(req.url).origin}/index.html`, req),
      });

      return new Response(notFoundResponse.body, { ...notFoundResponse, status: 200 });
    } catch (e) {
      return new Response('Not Found', { status: 404 });
    }
  }
}
