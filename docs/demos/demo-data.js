window.PRISM_DEMOS = [
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "ev-theme-discovery",
    "brand": "Prism News",
    "kind": "captured",
    "badge": "Captured data · 15 Oct 2026 · 93% of indexed articles",
    "sources": [
      {
        "file": "../examples/demo/ev-themes.json",
        "sha256": "a5f724109ee3b8c044fddb33cfc151d6117e24d0e7e93b9c2679db9c36324eb3",
        "kind": "captured"
      },
      {
        "file": "../examples/demo/ev-theme-headlines.json",
        "sha256": "587007905a06e7d56df937727cda193c609340ad402fe6c1dc477df1d458eb13",
        "kind": "captured"
      }
    ],
    "nav": "EV theme discovery",
    "client": "Claude Code",
    "heading": "Find what drives a topic",
    "title": "Discover the themes behind a topic",
    "prompt": "What is driving electric vehicle news in March and April 2026? Rank the themes, then show me the headlines behind the strongest one.",
    "steps": [
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/themes",
        "body": {
          "q": "electric vehicle",
          "since": "2026-03-02",
          "until": "2026-04-26",
          "limit": 5
        },
        "label": "Discover up to five themes"
      },
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/headlines",
        "body": {
          "q": "electric vehicle",
          "since": "2026-03-02",
          "until": "2026-04-26",
          "limit": 6,
          "themes": [
            "new model year updates and changes"
          ]
        },
        "label": "Read the selected theme's headlines"
      },
      {
        "type": "client",
        "label": "Chart lift and support",
        "detail": "Client-side ranking view"
      }
    ],
    "overview": {
      "type": "bars",
      "title": "Five themes behind electric-vehicle coverage",
      "labelWidth": 500,
      "subtitle": "Ranked by lift over the 30-day all-news share · 13,389 matching articles",
      "axisLabel": "Lift: theme share vs all-news share",
      "rows": [
        {
          "label": "New model year updates and changes",
          "sub": "1,388 articles · +235% vs previous period",
          "value": 392.35,
          "display": "392× lift"
        },
        {
          "label": "Hybrid vs electric vehicle reviews",
          "sub": "659 articles · -20% vs previous period",
          "value": 0,
          "display": "new vs baseline"
        },
        {
          "label": "Electric vehicle (EV) technology and…",
          "sub": "2,960 articles · +46% vs previous period",
          "value": 193.09,
          "display": "193× lift"
        },
        {
          "label": "Hybrid electric vehicle (HEV)…",
          "sub": "510 articles · +59% vs previous period",
          "value": 432.49,
          "display": "432× lift"
        },
        {
          "label": "Luxury SUV interior design & technology",
          "sub": "457 articles · +376% vs previous period",
          "value": 387.54,
          "display": "388× lift"
        }
      ],
      "stats": [
        {
          "value": "13,389",
          "label": "matching articles"
        },
        {
          "value": "9,626",
          "label": "carry theme labels"
        },
        {
          "value": "72%",
          "label": "theme coverage"
        },
        {
          "value": "5",
          "label": "suggestions (discovery cap)"
        }
      ]
    },
    "detail": {
      "type": "cards",
      "title": "Headlines for “new model year updates and changes”",
      "subtitle": "1,388 matching headlines · newest first · sentiment and priority kept",
      "items": [
        {
          "headline": "Renault developing new 1.2-litre MPFi engine for Bridger - Introduction | Autocar India",
          "meta": "autocarindia.com · 25 Apr",
          "tags": [
            {
              "text": "fair pos",
              "tone": "positive"
            },
            {
              "text": "priority 6",
              "tone": ""
            },
            {
              "text": "class 638",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Mercedes-Benz CLA EV India Launch Price, Range, Features",
          "meta": "motorbeam.com · 25 Apr",
          "tags": [
            {
              "text": "fair pos",
              "tone": "positive"
            },
            {
              "text": "priority 5",
              "tone": ""
            },
            {
              "text": "class 425",
              "tone": ""
            }
          ]
        },
        {
          "headline": "New Mercedes CLA Electric India Launch Price Rs 55 L - Up To 792 Km Range",
          "meta": "rushlane.com · 25 Apr",
          "tags": [
            {
              "text": "fair pos",
              "tone": "positive"
            },
            {
              "text": "priority 6",
              "tone": ""
            },
            {
              "text": "class 425",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Forget the new BYD Atto 3! An even newer one has just arrived | Auto Express",
          "meta": "autoexpress.co.uk · 24 Apr",
          "tags": [
            {
              "text": "slight pos",
              "tone": "positive"
            },
            {
              "text": "priority 6",
              "tone": ""
            },
            {
              "text": "class 176",
              "tone": ""
            }
          ]
        }
      ],
      "note": "Headlines omit theme metadata; the theme was selected through discovery and passed as a filter. 2 matching article(s) were unavailable from the article store at capture."
    },
    "footnote": "Lower-bound counts (1 of 14 shards offline). Lift compares with a 30-day all-news baseline ending at data_through, when ingest is thin; it is relative prominence, not reliability.",
    "takeaway": "Ask a broad topic, get ranked themes, then open the coverage behind the strongest one.",
    "evidence_summary": "Theme discovery plus headlines for the top theme",
    "guide": "../USER_GUIDE.md#discover-themes-and-read-articles"
  },
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "tariff-sentiment",
    "brand": "Prism News",
    "kind": "captured",
    "badge": "Captured data · 15 Oct 2026 · 93% of indexed articles",
    "sources": [
      {
        "file": "../examples/demo/tariff-sentiment.json",
        "sha256": "82cd4add085475ef3510dc7c1fde67205f995d754dcfb2b0a63e1fc3c4ad8239",
        "kind": "captured"
      },
      {
        "file": "../examples/demo/tariff-negative-headlines.json",
        "sha256": "b94c97ad3b27e950966727980a81960a08c282fb65dacde33d37d04e6894d943",
        "kind": "captured"
      }
    ],
    "nav": "Tariff sentiment shift",
    "client": "Codex",
    "heading": "Track how coverage turns",
    "title": "Watch the tone of a story change week by week",
    "prompt": "Track the tone of tariff coverage week by week from March to April 2026. When was it most negative, and which important headlines carried that tone?",
    "steps": [
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/sentiment",
        "body": {
          "q": "tariffs",
          "since": "2026-03-02",
          "until": "2026-04-26",
          "granularity": "weekly"
        },
        "label": "Weekly sentiment timeline"
      },
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/headlines",
        "body": {
          "q": "tariffs",
          "since": "2026-03-02",
          "until": "2026-04-26",
          "sentiment": [
            "negative"
          ],
          "priority_min": 6,
          "limit": 20
        },
        "label": "Negative headlines, priority 6+"
      },
      {
        "type": "client",
        "label": "Mark the turning point",
        "detail": "Client compares weekly negative shares"
      }
    ],
    "overview": {
      "type": "columns",
      "stacked": true,
      "title": "Tariff coverage by tone, week by week",
      "subtitle": "Articles carrying a sentiment label · weekly buckets starting Monday",
      "labels": [
        "2 Mar",
        "9 Mar",
        "16 Mar",
        "23 Mar",
        "30 Mar",
        "6 Apr",
        "13 Apr",
        "20 Apr"
      ],
      "unit": "articles per week",
      "series": [
        {
          "name": "Negative",
          "tone": "negative",
          "values": [
            1629,
            1176,
            939,
            1348,
            1788,
            1922,
            1496,
            1361
          ]
        },
        {
          "name": "Neutral",
          "tone": "neutral",
          "values": [
            63,
            44,
            49,
            101,
            101,
            91,
            77,
            96
          ]
        },
        {
          "name": "Positive",
          "tone": "positive",
          "values": [
            547,
            421,
            444,
            708,
            610,
            701,
            653,
            545
          ]
        }
      ],
      "height": 270,
      "stats": [
        {
          "value": "16,916",
          "label": "matching articles"
        },
        {
          "value": "69%",
          "label": "negative share"
        },
        {
          "value": "2.52 : 1",
          "label": "negative to positive"
        },
        {
          "value": "6 Apr",
          "label": "peak negative week (71%)"
        }
      ]
    },
    "detail": {
      "type": "cards",
      "title": "Negative tariff headlines that mattered",
      "subtitle": "sentiment = negative · priority ≥ 6 · same window · newest first",
      "items": [
        {
          "headline": "Deloitte plans benefit cuts for select US staff starting 2027: Report",
          "meta": "financialexpress.com · 26 Apr",
          "tags": [
            {
              "text": "slight neg",
              "tone": "negative"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            },
            {
              "text": "class 95",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Your guide to the California governor primary race",
          "meta": "sanluisobispo.com · 26 Apr",
          "tags": [
            {
              "text": "slight neg",
              "tone": "negative"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            },
            {
              "text": "class 20",
              "tone": ""
            }
          ]
        },
        {
          "headline": "US will have nearly 50 percent of chip market \"very soon\", Trump claims",
          "meta": "thestandard.com.hk · 26 Apr",
          "tags": [
            {
              "text": "slight neg",
              "tone": "negative"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            },
            {
              "text": "class 130",
              "tone": ""
            }
          ]
        },
        {
          "headline": "John Whelan: Irish exporters set for payback of ‘Liberation Day' tariffs",
          "meta": "irishexaminer.com · 26 Apr",
          "tags": [
            {
              "text": "slight neg",
              "tone": "negative"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            },
            {
              "text": "class 120",
              "tone": ""
            }
          ]
        }
      ],
      "note": "Baseline negative-to-positive ratio is 0.741; this window runs 3.4× the all-news norm. 11 matching article(s) were unavailable from the article store at capture."
    },
    "footnote": "Lower-bound counts (1 of 14 shards offline). Shares divide by articles carrying a sentiment label. A recent decline can reflect thinner coverage.",
    "takeaway": "See when a story turned, how far it moved from the all-news norm, and which headlines drove it.",
    "evidence_summary": "Weekly sentiment timeline plus negative headlines",
    "guide": "../USER_GUIDE.md#tone-priority-and-trends"
  },
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "ai-topic-compare",
    "brand": "Prism News",
    "kind": "captured",
    "badge": "Captured data · 15 Oct 2026 · 93% of indexed articles",
    "sources": [
      {
        "file": "../examples/demo/ai-compare.json",
        "sha256": "23a275e4134bb5b9467d6a590415324d05b238fab13d0dac1eb30e26eec5872b",
        "kind": "captured"
      },
      {
        "file": "../examples/demo/ai-regulation-trends.json",
        "sha256": "7310494c3c41c3b258e62b16ce3d499a112978f90bf464a129932994e5485a9d",
        "kind": "captured"
      },
      {
        "file": "../examples/demo/ai-investment-trends.json",
        "sha256": "999e41a0d296f878d52d5954c9bf0b15c53b5d8ead7620feba47f3e8c559bc12",
        "kind": "captured"
      }
    ],
    "nav": "Compare two topics",
    "client": "Claude Code",
    "heading": "Compare competing narratives",
    "title": "Compare two narratives over the same window",
    "prompt": "Compare AI regulation and AI investment coverage over March–April 2026. Which grew faster, how much do they overlap, and how critical is each?",
    "steps": [
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/compare",
        "body": {
          "queries": [
            {
              "name": "AI regulation",
              "filters": {
                "q": "AI regulation",
                "since": "2026-03-02",
                "until": "2026-04-26"
              }
            },
            {
              "name": "AI investment",
              "filters": {
                "q": "AI investment",
                "since": "2026-03-02",
                "until": "2026-04-26"
              }
            }
          ]
        },
        "label": "Exact union and per-query counts"
      },
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/trends",
        "body": {
          "q": "AI regulation",
          "since": "2026-03-02",
          "until": "2026-04-26",
          "granularity": "weekly"
        },
        "label": "Weekly volume: regulation"
      },
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/trends",
        "body": {
          "q": "AI investment",
          "since": "2026-03-02",
          "until": "2026-04-26",
          "granularity": "weekly"
        },
        "label": "Weekly volume: investment"
      }
    ],
    "overview": {
      "type": "lines",
      "title": "AI regulation vs AI investment, weekly",
      "subtitle": "Articles per week · identical dates and matching mode for both queries",
      "labels": [
        "2 Mar",
        "9 Mar",
        "16 Mar",
        "23 Mar",
        "30 Mar",
        "6 Apr",
        "13 Apr",
        "20 Apr"
      ],
      "unit": "articles per week",
      "height": 280,
      "series": [
        {
          "name": "AI regulation",
          "color": "#c0453b",
          "values": [
            27,
            14,
            22,
            33,
            14,
            18,
            23,
            28
          ]
        },
        {
          "name": "AI investment",
          "color": "#3b4fd8",
          "values": [
            22,
            25,
            44,
            39,
            31,
            35,
            37,
            63
          ]
        }
      ],
      "stats": [
        {
          "value": "179",
          "label": "AI regulation articles"
        },
        {
          "value": "296",
          "label": "AI investment articles"
        },
        {
          "value": "475",
          "label": "match at least one (exact union)"
        },
        {
          "value": "0",
          "label": "articles in both"
        }
      ]
    },
    "detail": {
      "type": "table",
      "title": "The comparison, measured",
      "subtitle": "Shares use the union of both queries, so they can sum past 100%",
      "headers": [
        "Query",
        "Articles",
        "Share of union",
        "Peak week",
        "Critical share"
      ],
      "widths": [
        26,
        16,
        18,
        18,
        22
      ],
      "rows": [
        [
          {
            "main": "AI regulation",
            "sub": "q = “AI regulation”"
          },
          {
            "num": "179"
          },
          {
            "num": "37.7%"
          },
          "23 Mar",
          {
            "num": "75.4%"
          }
        ],
        [
          {
            "main": "AI investment",
            "sub": "q = “AI investment”"
          },
          {
            "num": "296"
          },
          {
            "num": "62.3%"
          },
          "20 Apr",
          {
            "num": "80.7%"
          }
        ]
      ],
      "stats": [
        {
          "value": "475",
          "label": "union: match at least one"
        },
        {
          "value": "0.0%",
          "label": "of the union match both"
        },
        {
          "value": "8 weeks",
          "label": "complete periods, no partial buckets"
        }
      ],
      "note": "Second half vs first half of the window: AI regulation -14%, AI investment +28%. Overlapping articles are counted once in the union."
    },
    "footnote": "Lower-bound counts (1 of 14 shards offline). Sets may overlap. Keep dates, content-class scope and matching mode identical when comparing.",
    "takeaway": "Put two narratives on one scale, with exact overlap and per-topic criticality.",
    "evidence_summary": "Compare union counts plus weekly trends per query",
    "guide": "../USER_GUIDE.md#compare-25-named-queries"
  },
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "critical-alerts",
    "brand": "Prism News",
    "kind": "captured",
    "badge": "Captured data · 15 Oct 2026 · 93% of indexed articles",
    "sources": [
      {
        "file": "../examples/demo/semiconductor-priority.json",
        "sha256": "fd20a02eb0f8b06ec1707391014618d291e67d8f4cbc708dc2eee23981bc1c35",
        "kind": "captured"
      },
      {
        "file": "../examples/demo/semiconductor-critical.json",
        "sha256": "6041be5af4b47f00b070ba86177c86ecfa31980076646719c2dbfe10605b37a9",
        "kind": "captured"
      }
    ],
    "nav": "Critical news alerts",
    "client": "Codex",
    "heading": "Separate signal from noise",
    "title": "Surface the critical stories in a busy topic",
    "prompt": "Show how semiconductor news splits by priority in March–April 2026, then list only the critical stories rated 7 or higher.",
    "steps": [
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/priority",
        "body": {
          "q": "semiconductor",
          "since": "2026-03-02",
          "until": "2026-04-26"
        },
        "label": "Priority distribution"
      },
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/headlines",
        "body": {
          "q": "semiconductor",
          "since": "2026-03-02",
          "until": "2026-04-26",
          "priority_min": 7,
          "limit": 20
        },
        "label": "Critical headlines only"
      }
    ],
    "overview": {
      "type": "columns",
      "title": "Semiconductor coverage by priority band",
      "subtitle": "Priority 1–9 · bands 7–9 are critical",
      "unit": "articles",
      "height": 280,
      "labels": [
        "P1",
        "P2",
        "P3",
        "P4",
        "P5",
        "P6",
        "P7",
        "P8",
        "P9"
      ],
      "sublabels": [
        "",
        "",
        "",
        "",
        "",
        "",
        "critical",
        "critical",
        "critical"
      ],
      "series": [
        {
          "name": "Articles",
          "values": [
            10,
            27,
            641,
            3731,
            1407,
            1344,
            4216,
            1944,
            14
          ]
        }
      ],
      "stats": [
        {
          "value": "13,334",
          "label": "articles with a priority"
        },
        {
          "value": "6,174",
          "label": "critical (7–9)"
        },
        {
          "value": "46.3%",
          "label": "critical share (all news 40.59%)"
        },
        {
          "value": "5.79",
          "label": "mean priority"
        }
      ]
    },
    "detail": {
      "type": "cards",
      "title": "Critical semiconductor stories",
      "subtitle": "priority_min = 7 · newest first",
      "items": [
        {
          "headline": "Closing the Reality Gap: A New Architecture for 1.8-Tb/s Chiplet Governance",
          "meta": "semiwiki.com · 26 Apr",
          "tags": [
            {
              "text": "very pos",
              "tone": "positive"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            }
          ]
        },
        {
          "headline": "Intel, Advanced Micro, And Texas Instruments Are Among Top 10 Large-Cap Gainers Last Week (April 20-April",
          "meta": "benzinga.com · 26 Apr",
          "tags": [
            {
              "text": "slight pos",
              "tone": "positive"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            },
            {
              "text": "class 5",
              "tone": ""
            }
          ]
        },
        {
          "headline": "America Trembles as Transportation Secretary Announces Plans for Air Traffic Controllers to Lean on AI Tools",
          "meta": "futurism.com · 26 Apr",
          "tags": [
            {
              "text": "slight pos",
              "tone": "positive"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            },
            {
              "text": "class 50",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Samsung chip workers want 15% of AI profits and are ready to strike for it - Startup Fortune",
          "meta": "startupfortune.com · 26 Apr",
          "tags": [
            {
              "text": "slight neg",
              "tone": "negative"
            },
            {
              "text": "priority 8",
              "tone": "warn"
            },
            {
              "text": "class 130",
              "tone": ""
            }
          ]
        }
      ],
      "note": "Priority is the pipeline's urgency rating, not a reliability measure. Repeated headlines are shown once. 4 matching article(s) were unavailable from the article store at capture."
    },
    "footnote": "Lower-bound counts (1 of 14 shards offline). Critical share divides by articles carrying a priority, not by all matching articles.",
    "takeaway": "Quantify how much of a topic is urgent, then read just those stories.",
    "evidence_summary": "Priority bands plus critical headlines",
    "guide": "../USER_GUIDE.md#sentiment-and-priority"
  },
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "class-code-map",
    "brand": "Prism News",
    "kind": "captured",
    "badge": "Captured data · 15 Oct 2026 · 93% of indexed articles",
    "sources": [
      {
        "file": "../examples/demo/class-map-vehicle.json",
        "sha256": "f96ac3b5c3eda90a0ab35817848786626218f1d02c6ad00f51fd03a57ac8a907",
        "kind": "captured"
      },
      {
        "file": "../examples/demo/class-map-banking.json",
        "sha256": "3bbda726b13d6ee763547b2602c90fc73642b195ea2cd838f061f66eb5a9fa6c",
        "kind": "captured"
      }
    ],
    "nav": "GCP class code map",
    "client": "Claude Code",
    "heading": "Map topics to content classes",
    "title": "Turn a topic into GCP content-class codes",
    "prompt": "Which GCP content-class codes cover vehicles and banking? Give me the codes and full paths so I can filter headlines by class.",
    "steps": [
      {
        "type": "api",
        "method": "GET",
        "path": "/v1/classes",
        "body": {
          "q": "vehicle",
          "limit": 5
        },
        "label": "Find vehicle class codes"
      },
      {
        "type": "api",
        "method": "GET",
        "path": "/v1/classes",
        "body": {
          "q": "banking",
          "limit": 5
        },
        "label": "Find banking class codes"
      },
      {
        "type": "client",
        "label": "Use the codes as filters",
        "detail": "classes=63,42 on any news endpoint"
      }
    ],
    "overview": {
      "type": "tree",
      "title": "Content-class codes for two topics",
      "subtitle": "Up to five matches per query · integer code → full GCP path",
      "groups": [
        {
          "query": "vehicle",
          "items": [
            {
              "code": 122,
              "path": "/Autos & Vehicles/Vehicle Codes & Driving Laws/Other",
              "depth": 3,
              "parent": "/Autos & Vehicles/Vehicle Codes & Driving Laws",
              "parent_code": null,
              "articles_30d": 52
            },
            {
              "code": 63,
              "path": "/Autos & Vehicles/Motor Vehicles (By Type)/Hybrid & Alternative Vehicles",
              "depth": 3,
              "parent": "/Autos & Vehicles/Motor Vehicles (By Type)",
              "parent_code": null,
              "articles_30d": 23
            },
            {
              "code": 141,
              "path": "/Autos & Vehicles/Motor Vehicles (By Type)/Trucks, Vans & SUVs",
              "depth": 3,
              "parent": "/Autos & Vehicles/Motor Vehicles (By Type)",
              "parent_code": null,
              "articles_30d": 20
            },
            {
              "code": 189,
              "path": "/Autos & Vehicles/Motor Vehicles (By Type)/Motorcycles",
              "depth": 3,
              "parent": "/Autos & Vehicles/Motor Vehicles (By Type)",
              "parent_code": null,
              "articles_30d": 15
            },
            {
              "code": 89,
              "path": "/Autos & Vehicles/Vehicle Shopping/Vehicle Specs, Reviews & Comparisons",
              "depth": 3,
              "parent": "/Autos & Vehicles/Vehicle Shopping",
              "parent_code": null,
              "articles_30d": 14
            }
          ]
        },
        {
          "query": "banking",
          "items": [
            {
              "code": 42,
              "path": "/Finance/Banking/Other",
              "depth": 3,
              "parent": "/Finance/Banking",
              "parent_code": null,
              "articles_30d": 42
            },
            {
              "code": 180,
              "path": "/Finance/Banking/Mobile Payments & Digital Wallets",
              "depth": 3,
              "parent": "/Finance/Banking",
              "parent_code": null,
              "articles_30d": 3
            },
            {
              "code": 496,
              "path": "/Finance/Banking/Savings Accounts",
              "depth": 3,
              "parent": "/Finance/Banking",
              "parent_code": null,
              "articles_30d": 3
            },
            {
              "code": 702,
              "path": "/Finance/Banking/ATMs & Branch Locations",
              "depth": 3,
              "parent": "/Finance/Banking",
              "parent_code": null,
              "articles_30d": 1
            },
            {
              "code": 316,
              "path": "/Business & Industrial/Business Finance/Investment Banking",
              "depth": 3,
              "parent": "/Business & Industrial/Business Finance",
              "parent_code": null,
              "articles_30d": 0
            }
          ]
        }
      ],
      "note": "Use any returned code as `classes=` on headlines, trends, sentiment, themes or export."
    },
    "detail": {
      "type": "table",
      "title": "Codes ready to use as filters",
      "subtitle": "Leaf class, parent path and request parameter",
      "headers": [
        "Code",
        "Class",
        "Parent path",
        "30-day articles",
        "Filter"
      ],
      "widths": [
        9,
        30,
        32,
        13,
        16
      ],
      "rows": [
        [
          {
            "num": "122"
          },
          {
            "main": "Other"
          },
          {
            "sub": "/Autos & Vehicles/Vehicle Codes & Driving Laws"
          },
          {
            "num": "52"
          },
          {
            "tag": "classes=122"
          }
        ],
        [
          {
            "num": "63"
          },
          {
            "main": "Hybrid & Alternative Vehicles"
          },
          {
            "sub": "/Autos & Vehicles/Motor Vehicles (By Type)"
          },
          {
            "num": "23"
          },
          {
            "tag": "classes=63"
          }
        ],
        [
          {
            "num": "141"
          },
          {
            "main": "Trucks, Vans & SUVs"
          },
          {
            "sub": "/Autos & Vehicles/Motor Vehicles (By Type)"
          },
          {
            "num": "20"
          },
          {
            "tag": "classes=141"
          }
        ],
        [
          {
            "num": "189"
          },
          {
            "main": "Motorcycles"
          },
          {
            "sub": "/Autos & Vehicles/Motor Vehicles (By Type)"
          },
          {
            "num": "15"
          },
          {
            "tag": "classes=189"
          }
        ],
        [
          {
            "num": "42"
          },
          {
            "main": "Other"
          },
          {
            "sub": "/Finance/Banking"
          },
          {
            "num": "42"
          },
          {
            "tag": "classes=42"
          }
        ],
        [
          {
            "num": "180"
          },
          {
            "main": "Mobile Payments & Digital Wallets"
          },
          {
            "sub": "/Finance/Banking"
          },
          {
            "num": "3"
          },
          {
            "tag": "classes=180"
          }
        ],
        [
          {
            "num": "496"
          },
          {
            "main": "Savings Accounts"
          },
          {
            "sub": "/Finance/Banking"
          },
          {
            "num": "3"
          },
          {
            "tag": "classes=496"
          }
        ]
      ],
      "note": "30-day volumes count the 30 days ending at data_through, when ingest is thin; use them to compare classes, not as totals."
    },
    "footnote": "Lower-bound counts (1 of 14 shards offline). Class matches use the pipeline's 0.39 score threshold. One article can carry several classes.",
    "takeaway": "Find the right content-class codes by name, then filter any endpoint by them.",
    "evidence_summary": "Class discovery for two topics",
    "guide": "../USER_GUIDE.md#find-a-gcp-content-code"
  },
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "full-article-export",
    "brand": "Prism News",
    "kind": "captured",
    "badge": "Captured data · 15 Oct 2026 · 93% of indexed articles",
    "sources": [
      {
        "file": "../examples/demo/battery-export.json",
        "sha256": "d80407debcfc130ca5bdebcd9c837c88655bc2fa552bf0542bdbc135d0f16667",
        "kind": "captured"
      }
    ],
    "nav": "Full articles to CSV",
    "client": "Codex",
    "heading": "Export full articles for analysis",
    "title": "Export full article text to a spreadsheet",
    "prompt": "Export the full text of battery-storage articles from March–April 2026 to a CSV with headline, publisher, date, sentiment, priority and classes.",
    "steps": [
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/export",
        "body": {
          "q": "battery storage",
          "since": "2026-03-02",
          "until": "2026-04-26",
          "limit": 15,
          "format": "json"
        },
        "label": "Export a batch of full articles"
      },
      {
        "type": "client",
        "label": "Write the CSV locally",
        "detail": "or request format=csv directly"
      }
    ],
    "overview": {
      "type": "bars",
      "title": "Full bodies, not ledes",
      "labelWidth": 470,
      "subtitle": "5 articles delivered of 1,731 matches · characters of full text",
      "axisLabel": "Characters of article body",
      "rows": [
        {
          "label": "Fortescue to invest $952M in Pilbara…",
          "sub": "esdnews.com.au · 26 Apr",
          "value": 2034,
          "display": "2,034 chars · lede 350"
        },
        {
          "label": "EU Commission sets out AccelerateEU…",
          "sub": "pveurope.eu · 26 Apr",
          "value": 2664,
          "display": "2,664 chars · lede 349"
        },
        {
          "label": "Sick of power outages, this remote…",
          "sub": "inkl.com · 26 Apr",
          "value": 6079,
          "display": "6,079 chars · lede 340"
        },
        {
          "label": "Smartphones : l'UE va imposer des…",
          "sub": "capital.fr · 25 Apr",
          "value": 561,
          "display": "561 chars · lede 288"
        },
        {
          "label": "Adani Green Energy Posts Record 5.1…",
          "sub": "themachinemaker.com · 25 Apr",
          "value": 3017,
          "display": "3,017 chars · lede 331"
        }
      ],
      "stats": [
        {
          "value": "5",
          "label": "exports charged"
        },
        {
          "value": "10",
          "label": "unavailable, not charged"
        },
        {
          "value": "0",
          "label": "duplicates dropped, not charged"
        },
        {
          "value": "1,731",
          "label": "matching articles"
        }
      ]
    },
    "detail": {
      "type": "sheet",
      "title": "Full articles, as a CSV file",
      "subtitle": "The export's CSV columns, one row per delivered article",
      "filename": "battery-storage.csv",
      "status": "format=csv · next batch via cursor (json)",
      "headers": [
        "headline",
        "publisher",
        "published_at",
        "sentiment",
        "priority",
        "classes"
      ],
      "widths": [
        36,
        22,
        14,
        12,
        8,
        8
      ],
      "rows": [
        [
          "Fortescue to invest $952M in Pilbara Green…",
          "esdnews.com.au",
          "2026-04-26",
          {
            "tag": "very_pos",
            "tone": "positive"
          },
          "7",
          "45"
        ],
        [
          "EU Commission sets out AccelerateEU energy…",
          "pveurope.eu",
          "2026-04-26",
          {
            "tag": "very_pos",
            "tone": "positive"
          },
          "7",
          "45"
        ],
        [
          "Sick of power outages, this remote…",
          "inkl.com",
          "2026-04-26",
          {
            "tag": "slight_pos",
            "tone": "positive"
          },
          "7",
          "45"
        ],
        [
          "Smartphones : l'UE va imposer des…",
          "capital.fr",
          "2026-04-25",
          {
            "tag": "slight_pos",
            "tone": "positive"
          },
          "6",
          "40"
        ],
        [
          "Adani Green Energy Posts Record 5.1 GW…",
          "themachinemaker.com",
          "2026-04-25",
          {
            "tag": "very_pos",
            "tone": "positive"
          },
          "7",
          "45|0"
        ]
      ],
      "note": "The body column holds the complete article text; it is omitted here for width."
    },
    "footnote": "Lower-bound counts (1 of 14 shards offline). Exports are charged per delivered article. Save IDs across batches to deduplicate a full download.",
    "takeaway": "Move from a filter to full article text in a file your analysis tools can read.",
    "evidence_summary": "One full-article export batch",
    "guide": "../USER_GUIDE.md#full-articles-and-exports"
  }
];
