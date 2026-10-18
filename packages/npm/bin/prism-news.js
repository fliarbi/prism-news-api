#!/usr/bin/env node
// prism-news CLI (npm): prism-news COMMAND [QUERY|ID] [--field value ...]
import { PrismNews, PrismAPIError, listTopics, loadTable, TABLES, VERSION } from "../index.js";

const NEWS = {
  overview: ["POST", "/v1/overview"], headlines: ["POST", "/v1/headlines"], themes: ["POST", "/v1/themes"],
  "theme-headlines": ["GET", "/v1/themes/{arg}/headlines"], sentiment: ["POST", "/v1/sentiment"],
  priority: ["POST", "/v1/priority"], trends: ["POST", "/v1/trends"], geography: ["POST", "/v1/geography"],
  coverage: ["POST", "/v1/coverage"], export: ["POST", "/v1/export"], article: ["GET", "/v1/articles/{arg}"],
  related: ["GET", "/v1/articles/{arg}/related"], classes: ["GET", "/v1/classes"], class: ["GET", "/v1/classes/{arg}"],
  "class-headlines": ["GET", "/v1/classes/{arg}/headlines"], me: ["GET", "/v1/me"], status: ["GET", "/v1/status"],
  vocabulary: ["GET", "/v1/vocabulary"],
};

const usage = `prism-news ${VERSION} (npm: prism-news-api)
usage: prism-news COMMAND [QUERY|ID] [--field value ...]
       prism-news call METHOD PATH [JSON] [--business]
       prism-news datasets list [--cluster NAME] | datasets get SLUG [TABLE]   (open datasets, no key)
commands: ${Object.keys(NEWS).sort().join(", ")}
Key from PRISM_API_KEY; base URL from PRISM_API_BASE (default https://radar-api.fliarbi.com/news).
Example: prism-news headlines "electric vehicle" --since 2026-01-01 --until 2026-04-30 --limit 20`;

function value(v) {
  if (/^(true|false)$/i.test(v)) return v.toLowerCase() === "true";
  if (/^-?\d+(\.\d+)?$/.test(v)) return Number(v);
  return v;
}

function parse(argv) {
  const pos = [], fields = {}, flags = {};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--business") flags.business = true;
    else if (a.startsWith("--")) {
      let [name, inline] = a.slice(2).split(/=(.*)/s);
      if (inline === undefined) {
        if (i + 1 >= argv.length) fail(`--${name} needs a value`, 2);
        inline = argv[++i];
      }
      name = name.replace(/-/g, "_");
      const v = value(inline);
      fields[name] = name in fields ? [].concat(fields[name], v) : v;
    } else pos.push(a);
  }
  return { pos, fields, flags };
}

function fail(msg, code = 1) { console.error(msg); process.exit(code); }

async function main(argv) {
  if (!argv.length || ["-h", "--help", "help"].includes(argv[0])) return console.log(usage);
  if (["-V", "--version"].includes(argv[0])) return console.log(VERSION);
  const [cmd, ...rest] = argv;
  const { pos, fields, flags } = parse(rest);
  if (cmd === "datasets") {
    const sub = pos[0] ?? "list";
    if (sub === "list") {
      for (const t of listTopics({ cluster: fields.cluster })) console.log(`${t.slug.padEnd(26)} ${t.cluster.padEnd(12)} ${t.url}`);
      return;
    }
    if (sub === "get" && pos[1]) {
      const table = pos[2] ?? "monthly";
      if (!TABLES.includes(table)) fail(`unknown table ${table}; choose one of ${TABLES.join(", ")}`, 2);
      return console.log(JSON.stringify(await loadTable(pos[1], table), null, 1));
    }
    fail("usage: prism-news datasets list [--cluster NAME] | datasets get SLUG [TABLE]", 2);
  }
  let method, path, body = fields;
  if (cmd === "call") {
    if (pos.length < 2) fail("usage: call METHOD PATH [JSON]", 2);
    [method, path] = [pos[0].toUpperCase(), pos[1]];
    body = { ...(pos[2] ? JSON.parse(pos[2]) : {}), ...fields };
  } else if (NEWS[cmd]) {
    [method, path] = NEWS[cmd];
    if (path.includes("{arg}")) {
      if (!pos.length) fail(`${cmd} needs an argument`, 2);
      path = path.replace("{arg}", encodeURIComponent(pos.shift()));
    }
    if (pos.length && !("q" in body)) body = { q: pos.join(" "), ...body };
  } else fail(`Unknown command ${JSON.stringify(cmd)}.\n${usage}`, 2);
  const client = new PrismNews();
  if (!client.apiKey) fail("Set PRISM_API_KEY (create a key in the Fliar dashboard).");
  const out = await client.request(method, path, body, { business: !!flags.business });
  console.log(JSON.stringify(out, null, 1));
  if (out && out.ok === false) process.exit(1);
}

main(process.argv.slice(2)).catch((e) => {
  if (e instanceof PrismAPIError) { console.log(JSON.stringify(e.payload, null, 1)); fail(e.message); }
  fail(e?.message ?? String(e));
});
