export declare const VERSION: string;
export declare const DEFAULT_BASE_URL: string;
export declare const DEFAULT_BUSINESS_BASE_URL: string;
export declare const HF_ORG: string;
export declare const TABLES: readonly TableName[];

export type Sentiment = "positive" | "negative" | "neutral" | string;

/** Common news filters. Any other field is passed through unchanged. */
export interface Filters {
  q?: string;
  match?: "any" | "opening" | "focused";
  since?: string;
  until?: string;
  sentiment?: Sentiment | Sentiment[];
  priority_min?: number;
  priority_max?: number;
  classes?: number | number[];
  class_prefix?: string;
  themes?: string[];
  country?: string;
  limit?: number;
  sort?: "newest" | "oldest" | "priority";
  cursor?: string;
  granularity?: "daily" | "weekly" | "monthly";
  format?: "json" | "ndjson" | "csv";
  [field: string]: unknown;
}

export interface Envelope<T = any> {
  ok: boolean;
  data: T | null;
  window?: Record<string, unknown>;
  meta?: Record<string, unknown>;
  subject?: Record<string, unknown>;
  error?: { kind: string; reason?: string };
}

export interface HeadlineItem {
  id: string;
  headline: string;
  url?: string;
  publisher?: string;
  published_at?: string;
  lede?: string;
  sentiment?: string;
  priority?: number;
  classes?: unknown[];
  country?: string;
  organizations?: string[];
  people?: string[];
  [field: string]: unknown;
}

export interface ListData<T> {
  items: T[];
  returned?: number;
  total_estimate?: number;
  next_cursor?: string | null;
  [field: string]: unknown;
}

export interface CompareQuery { name: string; filters: Filters }

export interface ClientOptions {
  /** Defaults to process.env.PRISM_API_KEY. */
  apiKey?: string;
  /** Defaults to PRISM_API_BASE or https://radar-api.fliarbi.com/news. */
  baseUrl?: string;
  /** Defaults to PRISM_BUSINESS_API_BASE or https://radar-api.fliarbi.com/business-news. */
  businessBaseUrl?: string;
  timeoutMs?: number;
  fetch?: typeof fetch;
}

export declare class PrismAPIError extends Error {
  status: number;
  kind: string | null;
  payload: unknown;
}

export declare class PrismNews {
  constructor(options?: ClientOptions);
  apiKey: string;
  baseUrl: string;
  businessBaseUrl: string;
  request<T = any>(method: string, path: string, body?: Record<string, unknown>, opts?: { business?: boolean }): Promise<Envelope<T>>;
  me(): Promise<Envelope>;
  status(): Promise<Envelope>;
  vocabulary(): Promise<Envelope>;
  overview(q: string, filters?: Filters): Promise<Envelope>;
  headlines(q: string, filters?: Filters): Promise<Envelope<ListData<HeadlineItem>>>;
  themes(q: string, filters?: Filters): Promise<Envelope<ListData<any>>>;
  themeHeadlines(themeId: string, filters?: Filters): Promise<Envelope<ListData<HeadlineItem>>>;
  sentiment(q: string, filters?: Filters): Promise<Envelope>;
  priority(q: string, filters?: Filters): Promise<Envelope>;
  trends(q: string, filters?: Filters): Promise<Envelope>;
  geography(q: string, filters?: Filters): Promise<Envelope<ListData<{ country: string; count: number; share_pct: number }>>>;
  coverage(q: string, filters?: Filters): Promise<Envelope>;
  export(q: string, filters?: Filters): Promise<Envelope>;
  /** 2-5 queries; strings become { name: s, filters: { q: s } }. Shared filters apply to all. */
  compare(queries: Array<string | CompareQuery>, filters?: Filters): Promise<Envelope>;
  article(id: string): Promise<Envelope>;
  related(id: string, filters?: Filters): Promise<Envelope<ListData<HeadlineItem>>>;
  classes(): Promise<Envelope>;
  classInfo(code: string | number): Promise<Envelope>;
  classHeadlines(code: string | number, filters?: Filters): Promise<Envelope<ListData<HeadlineItem>>>;
  /** POST /v1/business/<endpoint>, e.g. business("funding", undefined, { sector: "fintech" }). */
  business(endpoint: string, q?: string, filters?: Filters): Promise<Envelope>;
  companyNews(domain: string, filters?: Filters): Promise<Envelope<ListData<HeadlineItem>>>;
}

export type TableName =
  | "sample" | "monthly" | "countries" | "cities" | "continents" | "country_tone" | "country_trend"
  | "organisations" | "themes" | "tone_by_year" | "states_india" | "states_us" | "research_by_year"
  | "top_papers" | "patents_by_year" | "patent_offices" | "patent_cpc";

export interface Topic { slug: string; topic: string; cluster: string; repo: string; url: string }

/** The 60 open news-topic datasets (January 2019 - July 2026, CC BY-NC 4.0). */
export declare function listTopics(options?: { cluster?: string }): Topic[];
export declare function tableUrl(slug: string, table?: TableName): string;
export declare function parseCSV(text: string): Record<string, string>[];
export declare function loadTable(slug: string, table?: TableName, options?: { fetch?: typeof fetch }): Promise<Record<string, string>[]>;

export default PrismNews;
