// prism-news-api: zero-dependency client for the Prism News API by Fliar, plus the open
// news-topic datasets (January 2019 - July 2026). ESM, Node 18+ and modern browsers (global fetch).
export const VERSION = "0.1.0";
export const DEFAULT_BASE_URL = "https://radar-api.fliarbi.com/news";
export const DEFAULT_BUSINESS_BASE_URL = "https://radar-api.fliarbi.com/business-news";

const env = (name) => (typeof process !== "undefined" && process.env ? process.env[name] : undefined);
const enc = (s) => encodeURIComponent(String(s));

export class PrismAPIError extends Error {
  constructor(status, payload) {
    const err = payload && typeof payload === "object" ? payload.error : null;
    super(`HTTP ${status}${err?.kind ? " " + err.kind : ""}${err?.reason ? ": " + err.reason : ""}`);
    this.name = "PrismAPIError";
    this.status = status;
    this.kind = err?.kind ?? null;
    this.payload = payload;
  }
}

export class PrismNews {
  constructor({ apiKey, baseUrl, businessBaseUrl, timeoutMs = 180000, fetch: fetchImpl } = {}) {
    this.apiKey = apiKey ?? env("PRISM_API_KEY") ?? "";
    this.baseUrl = (baseUrl ?? env("PRISM_API_BASE") ?? DEFAULT_BASE_URL).replace(/\/+$/, "");
    this.businessBaseUrl = (businessBaseUrl ?? env("PRISM_BUSINESS_API_BASE") ?? DEFAULT_BUSINESS_BASE_URL).replace(/\/+$/, "");
    this.timeoutMs = timeoutMs;
    this._fetch = fetchImpl ?? globalThis.fetch;
  }

  async request(method, path, body = {}, { business = false } = {}) {
    if (!this.apiKey) throw new PrismAPIError(401, { error: { kind: "no_key", reason: "set PRISM_API_KEY or pass apiKey" } });
    const clean = Object.fromEntries(Object.entries(body ?? {}).filter(([, v]) => v !== undefined && v !== null));
    method = method.toUpperCase();
    let url = (business ? this.businessBaseUrl : this.baseUrl) + path;
    const init = { method, headers: { "X-API-Key": this.apiKey, "Content-Type": "application/json" } };
    if (typeof window === "undefined") init.headers["User-Agent"] = `prism-news-js/${VERSION}`;
    if (method === "GET") {
      const qs = new URLSearchParams(Object.entries(clean).map(([k, v]) => [k, Array.isArray(v) ? v.join(",") : String(v)])).toString();
      if (qs) url += "?" + qs;
    } else {
      init.body = JSON.stringify(clean);
    }
    if (typeof AbortSignal !== "undefined" && AbortSignal.timeout) init.signal = AbortSignal.timeout(this.timeoutMs);
    const res = await this._fetch(url, init);
    const text = await res.text();
    let payload;
    try { payload = text ? JSON.parse(text) : {}; } catch { payload = { ok: false, error: { kind: "not_json", reason: text.slice(0, 200) } }; }
    if (!res.ok) throw new PrismAPIError(res.status, payload);
    return payload;
  }

  _post(path, q, fields = {}, business = false) {
    return this.request("POST", path, q === undefined || q === null ? fields : { q, ...fields }, { business });
  }

  // free
  me() { return this.request("GET", "/v1/me"); }
  status() { return this.request("GET", "/v1/status"); }
  vocabulary() { return this.request("GET", "/v1/vocabulary"); }

  // news
  overview(q, f) { return this._post("/v1/overview", q, f); }
  headlines(q, f) { return this._post("/v1/headlines", q, f); }
  themes(q, f) { return this._post("/v1/themes", q, f); }
  themeHeadlines(themeId, f) { return this.request("GET", `/v1/themes/${enc(themeId)}/headlines`, f); }
  sentiment(q, f) { return this._post("/v1/sentiment", q, f); }
  priority(q, f) { return this._post("/v1/priority", q, f); }
  trends(q, f) { return this._post("/v1/trends", q, f); }
  geography(q, f) { return this._post("/v1/geography", q, f); }
  coverage(q, f) { return this._post("/v1/coverage", q, f); }
  export(q, f) { return this._post("/v1/export", q, f); }
  compare(queries, filters = {}) {
    const common = Object.fromEntries(Object.entries(filters).filter(([, v]) => v !== undefined && v !== null));
    const items = queries.map((q) => typeof q === "string"
      ? { name: q, filters: { ...common, q } }
      : { name: q.name, filters: { ...common, ...(q.filters ?? {}) } });
    return this.request("POST", "/v1/compare", { queries: items });
  }
  article(id) { return this.request("GET", `/v1/articles/${enc(id)}`); }
  related(id, f) { return this.request("GET", `/v1/articles/${enc(id)}/related`, f); }
  classes() { return this.request("GET", "/v1/classes"); }
  classInfo(code) { return this.request("GET", `/v1/classes/${enc(code)}`); }
  classHeadlines(code, f) { return this.request("GET", `/v1/classes/${enc(code)}/headlines`, f); }

  // business news (same key)
  business(endpoint, q, f) { return this._post(`/v1/business/${String(endpoint).replace(/^\/+|\/+$/g, "")}`, q, f, true); }
  companyNews(domain, f) { return this.request("GET", `/v1/business/companies/${enc(domain)}/news`, f, { business: true }); }
}

// ---- open datasets -----------------------------------------------------------------
export const HF_ORG = "fliarbi";
const SUFFIX = "-news-2019-2026";
export const TABLES = ["sample", "monthly", "countries", "cities", "continents", "country_tone", "country_trend",
  "organisations", "themes", "tone_by_year", "states_india", "states_us", "research_by_year", "top_papers",
  "patents_by_year", "patent_offices", "patent_cpc"];
const TOPICS = [
  ["snowfall", "snowfall", "weather"],
  ["hurricanes", "hurricanes", "disasters"],
  ["covid", "covid", "health"],
  ["floods", "floods", "disasters"],
  ["waste-management", "waste management", "urban"],
  ["mental-health", "mental health", "health"],
  ["earthquakes", "earthquakes", "disasters"],
  ["weather", "weather", "weather"],
  ["climate-change", "climate change", "environment"],
  ["lung-cancer", "lung cancer", "health"],
  ["tornadoes", "tornadoes", "disasters"],
  ["cybercrime", "cybercrime", "crime"],
  ["pfas", "pfas", "water"],
  ["gun-violence", "gun violence", "crime"],
  ["measles", "measles", "health"],
  ["airports", "airports", "urban"],
  ["breast-cancer", "breast cancer", "health"],
  ["homelessness", "homelessness", "society"],
  ["electric-vehicles", "electric vehicles", "energy"],
  ["alzheimers", "alzheimer's", "health"],
  ["malaria", "malaria", "health"],
  ["inflation", "inflation", "economy"],
  ["volcano", "volcano", "disasters"],
  ["data-breach", "data breach", "crime"],
  ["monsoon", "monsoon", "weather"],
  ["unemployment", "unemployment", "economy"],
  ["migration", "migration", "society"],
  ["tsunami", "tsunami", "disasters"],
  ["suicide", "suicide", "health"],
  ["natural-disasters", "natural disasters", "disasters"],
  ["housing", "housing", "urban"],
  ["air-pollution", "air pollution", "environment"],
  ["cybersecurity", "cybersecurity", "tech"],
  ["kidney-disease", "kidney disease", "health"],
  ["drowning", "drowning", "safety"],
  ["domestic-violence", "domestic violence", "crime"],
  ["hepatitis", "hepatitis", "health"],
  ["population", "population", "society"],
  ["poverty", "poverty", "economy"],
  ["smartphones", "smartphones", "tech"],
  ["drones", "drones", "tech"],
  ["protests", "protests", "society"],
  ["road-accidents", "road accidents", "safety"],
  ["drought", "drought", "environment"],
  ["plane-crash", "plane crash", "safety"],
  ["obesity", "obesity", "health"],
  ["oil-prices", "oil prices", "energy"],
  ["opioid-crisis", "opioid crisis", "health"],
  ["antimicrobial-resistance", "antimicrobial resistance", "health"],
  ["vaccine", "vaccine", "health"],
  ["robotics", "robotics", "tech"],
  ["biodiversity-loss", "biodiversity loss", "environment"],
  ["food-safety", "food safety", "food"],
  ["ransomware", "ransomware", "crime"],
  ["data-centers", "data centers", "tech"],
  ["heart-attack", "heart attack", "health"],
  ["carbon-emissions", "carbon emissions", "environment"],
  ["water-pollution", "water pollution", "environment"],
  ["crimes-against-women", "crimes against women", "crime"],
  ["5g", "5g", "tech"]
];

export function listTopics({ cluster } = {}) {
  return TOPICS.filter(([, , c]) => !cluster || c === cluster).map(([slug, topic, c]) => ({
    slug, topic, cluster: c, repo: `${HF_ORG}/${slug}${SUFFIX}`,
    url: `https://huggingface.co/datasets/${HF_ORG}/${slug}${SUFFIX}`,
  }));
}

export function tableUrl(slug, table = "sample") {
  if (!TABLES.includes(table)) throw new Error(`unknown table ${table}; choose one of ${TABLES.join(", ")}`);
  const file = table === "sample" ? `data/${slug}-news-sample.csv` : `data/${table}.csv`;
  return `https://huggingface.co/datasets/${HF_ORG}/${slug}${SUFFIX}/resolve/main/${file}`;
}

export function parseCSV(text) {
  const rows = [];
  let row = [], field = "", quoted = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (quoted) {
      if (ch === '"') { if (text[i + 1] === '"') { field += '"'; i++; } else quoted = false; }
      else field += ch;
    } else if (ch === '"') quoted = true;
    else if (ch === ",") { row.push(field); field = ""; }
    else if (ch === "\n" || ch === "\r") {
      if (ch === "\r" && text[i + 1] === "\n") i++;
      row.push(field); field = ""; rows.push(row); row = [];
    } else field += ch;
  }
  if (field !== "" || row.length) { row.push(field); rows.push(row); }
  const [head = [], ...body] = rows.filter((r) => r.length > 1 || r[0] !== "");
  return body.map((r) => Object.fromEntries(head.map((h, j) => [h, r[j] ?? ""])));
}

export async function loadTable(slug, table = "sample", { fetch: fetchImpl = globalThis.fetch } = {}) {
  const res = await fetchImpl(tableUrl(slug, table));
  if (!res.ok) throw new Error(`${HF_ORG}/${slug}${SUFFIX}: no ${table} table (HTTP ${res.status})`);
  return parseCSV(await res.text());
}

export default PrismNews;
