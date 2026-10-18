import { test } from "node:test";
import assert from "node:assert/strict";
import { PrismNews, PrismAPIError, listTopics, tableUrl, parseCSV } from "../index.js";

const fakeFetch = (seen, status = 200, body = '{"ok":true}') => async (url, init) => {
  seen.push({ url, init });
  return { ok: status < 300, status, text: async () => body };
};

test("POST sends key and q", async () => {
  const seen = [];
  const c = new PrismNews({ apiKey: "k", baseUrl: "https://x.test/news/", fetch: fakeFetch(seen) });
  await c.headlines("floods", { limit: 5, since: undefined });
  assert.equal(seen[0].url, "https://x.test/news/v1/headlines");
  assert.equal(seen[0].init.headers["X-API-Key"], "k");
  assert.deepEqual(JSON.parse(seen[0].init.body), { q: "floods", limit: 5 });
});

test("GET uses query string and compare shapes queries", async () => {
  const seen = [];
  const c = new PrismNews({ apiKey: "k", baseUrl: "https://x.test/news", fetch: fakeFetch(seen) });
  await c.classHeadlines(55, { limit: 3, classes: [0, 55] });
  assert.equal(seen[0].url, "https://x.test/news/v1/classes/55/headlines?limit=3&classes=0%2C55");
  await c.compare(["ev", "battery storage"], { since: "2026-01-01" });
  assert.deepEqual(JSON.parse(seen[1].init.body).queries[1], { name: "battery storage", filters: { since: "2026-01-01", q: "battery storage" } });
});

test("errors raise PrismAPIError", async () => {
  const c = new PrismNews({ apiKey: "bad", fetch: fakeFetch([], 401, '{"ok":false,"error":{"kind":"invalid_key"}}') });
  await assert.rejects(c.me(), (e) => e instanceof PrismAPIError && e.status === 401 && e.kind === "invalid_key");
});

test("datasets", () => {
  assert.equal(listTopics().length, 60);
  assert.ok(tableUrl("floods").endsWith("/fliarbi/floods-news-2019-2026/resolve/main/data/floods-news-sample.csv"));
  assert.deepEqual(parseCSV('a,b\r\n1,"x,y"\r\n'), [{ a: "1", b: "x,y" }]);
});
