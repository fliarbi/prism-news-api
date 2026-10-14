window.PRISM_DEMOS = [
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "ev-theme-discovery",
    "brand": "Prism News",
    "kind": "illustrative",
    "badge": "Illustrative data · fictional articles and counts",
    "sources": [
      {
        "file": "../examples/demo/ev-themes.json",
        "sha256": "c96f14d92ac1862a42b18d613f62144063da22565aa3bacd1dc9f20d399b1b57",
        "kind": "illustrative"
      },
      {
        "file": "../examples/demo/ev-theme-headlines.json",
        "sha256": "b71f0edf7a2bb74128f44fec948dc849e7533c59fc29312c344362b4ae351618",
        "kind": "illustrative"
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
            "charging network buildout"
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
      "subtitle": "Ranked by lift over the 30-day archive share · 3,870 matching articles",
      "axisLabel": "Lift: theme share vs archive share",
      "rows": [
        {
          "label": "Charging network buildout",
          "sub": "412 articles · +25% vs previous period",
          "value": 4.1,
          "display": "4.1× lift"
        },
        {
          "label": "Battery supply agreements",
          "sub": "366 articles · +25% vs previous period",
          "value": 3.2,
          "display": "3.2× lift"
        },
        {
          "label": "EV price cuts and incentives",
          "sub": "298 articles · +25% vs previous period",
          "value": 2.7,
          "display": "2.7× lift"
        },
        {
          "label": "Autonomous driving pilots",
          "sub": "171 articles · +25% vs previous period",
          "value": 1.9,
          "display": "1.9× lift"
        },
        {
          "label": "Plant retooling and jobs",
          "sub": "143 articles · +25% vs previous period",
          "value": 1.6,
          "display": "1.6× lift"
        }
      ],
      "stats": [
        {
          "value": "3,870",
          "label": "matching articles"
        },
        {
          "value": "2,140",
          "label": "carry theme labels"
        },
        {
          "value": "55%",
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
      "title": "Headlines for “charging network buildout”",
      "subtitle": "222 matching headlines · newest first · sentiment and priority kept",
      "items": [
        {
          "headline": "Northwind Motors opens 400 fast-charging bays along the coastal corridor",
          "meta": "dailyauto.example · 24 Apr",
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
              "text": "class 63",
              "tone": ""
            }
          ]
        },
        {
          "headline": "City council approves curbside chargers for apartment districts",
          "meta": "metro-ledger.example · 22 Apr",
          "tags": [
            {
              "text": "slight pos",
              "tone": "positive"
            },
            {
              "text": "priority 5",
              "tone": ""
            },
            {
              "text": "class 63",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Charging operator Voltway raises tariffs at highway sites",
          "meta": "energywire.example · 17 Apr",
          "tags": [
            {
              "text": "slight neg",
              "tone": "negative"
            },
            {
              "text": "priority 6",
              "tone": ""
            },
            {
              "text": "class 63",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Fleet operators report longer queues at urban charging hubs",
          "meta": "logistics-today.example · 9 Apr",
          "tags": [
            {
              "text": "fair neg",
              "tone": "negative"
            },
            {
              "text": "priority 5",
              "tone": ""
            },
            {
              "text": "class 63",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Contoso Energy and Northwind sign shared charging-network deal",
          "meta": "dailyauto.example · 30 Mar",
          "tags": [
            {
              "text": "fair pos",
              "tone": "positive"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            },
            {
              "text": "class 63",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Regional grid operator studies peak load from new charging sites",
          "meta": "energywire.example · 11 Mar",
          "tags": [
            {
              "text": "none",
              "tone": "neutral"
            },
            {
              "text": "priority 5",
              "tone": ""
            },
            {
              "text": "class 63",
              "tone": ""
            }
          ]
        }
      ],
      "note": "Headlines omit theme metadata; the theme was selected through discovery and passed as a filter."
    },
    "footnote": "Lift is relative prominence against a 30-day archive baseline, not a reliability score.",
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
    "kind": "illustrative",
    "badge": "Illustrative data · fictional articles and counts",
    "sources": [
      {
        "file": "../examples/demo/tariff-sentiment.json",
        "sha256": "fd5ee4c8e20ae002fd00b8e35997539e488d43c8f445d57eb5da3b279cc0319f",
        "kind": "illustrative"
      },
      {
        "file": "../examples/demo/tariff-negative-headlines.json",
        "sha256": "230a8f54adcda8c3ef479fcc1e0f90b41396aa57296f823cdc555747e8858fe1",
        "kind": "illustrative"
      }
    ],
    "nav": "Tariff sentiment shift",
    "client": "Codex",
    "heading": "Track how coverage turns",
    "title": "Watch the tone of a story change week by week",
    "prompt": "Track the tone of tariff coverage week by week from March to April 2026. When did it turn negative, and which critical headlines drove it?",
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
          "priority_min": 7,
          "limit": 6
        },
        "label": "Critical negative headlines"
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
            520,
            610,
            1810,
            2140,
            1520,
            1180,
            930,
            840
          ]
        },
        {
          "name": "Neutral",
          "tone": "neutral",
          "values": [
            240,
            250,
            270,
            300,
            290,
            310,
            330,
            320
          ]
        },
        {
          "name": "Positive",
          "tone": "positive",
          "values": [
            450,
            480,
            900,
            980,
            840,
            720,
            630,
            600
          ]
        }
      ],
      "height": 270,
      "stats": [
        {
          "value": "18,930",
          "label": "matching articles"
        },
        {
          "value": "55%",
          "label": "negative share"
        },
        {
          "value": "1.71 : 1",
          "label": "negative to positive"
        },
        {
          "value": "23 Mar",
          "label": "peak negative week (63%)"
        }
      ]
    },
    "detail": {
      "type": "cards",
      "title": "The critical negative headlines",
      "subtitle": "sentiment = negative · priority ≥ 7 · same window",
      "items": [
        {
          "headline": "Importers warn of shelf-price rises as new tariff schedule takes effect",
          "meta": "tradeweekly.example · 24 Mar",
          "tags": [
            {
              "text": "very neg",
              "tone": "negative"
            },
            {
              "text": "priority 8",
              "tone": "warn"
            },
            {
              "text": "class 0",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Port of Eastbay reports 18% drop in container bookings after levy",
          "meta": "harbor-news.example · 26 Mar",
          "tags": [
            {
              "text": "very neg",
              "tone": "negative"
            },
            {
              "text": "priority 8",
              "tone": "warn"
            },
            {
              "text": "class 0",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Fabrikam Foods cuts outlook, citing tariff costs on packaging",
          "meta": "markets-desk.example · 31 Mar",
          "tags": [
            {
              "text": "fair neg",
              "tone": "negative"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            },
            {
              "text": "class 0",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Small exporters seek emergency credit lines amid retaliatory duties",
          "meta": "tradeweekly.example · 2 Apr",
          "tags": [
            {
              "text": "very neg",
              "tone": "negative"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            },
            {
              "text": "class 0",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Retail association files challenge against tariff expansion",
          "meta": "metro-ledger.example · 8 Apr",
          "tags": [
            {
              "text": "fair neg",
              "tone": "negative"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            },
            {
              "text": "class 0",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Electronics distributors pause orders pending tariff clarification",
          "meta": "markets-desk.example · 14 Apr",
          "tags": [
            {
              "text": "fair neg",
              "tone": "negative"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            },
            {
              "text": "class 0",
              "tone": ""
            }
          ]
        }
      ],
      "note": "Baseline negative-to-positive ratio is 0.8; this window runs 2.13× the archive norm."
    },
    "footnote": "Shares divide by articles carrying a sentiment label. A recent decline can reflect thinner coverage.",
    "takeaway": "See when a story turned, how far it moved from the archive norm, and which headlines drove it.",
    "evidence_summary": "Weekly sentiment timeline plus critical negative headlines",
    "guide": "../USER_GUIDE.md#tone-priority-and-trends"
  },
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "ai-topic-compare",
    "brand": "Prism News",
    "kind": "illustrative",
    "badge": "Illustrative data · fictional counts",
    "sources": [
      {
        "file": "../examples/demo/ai-compare.json",
        "sha256": "fcf9e175505159d55bf77efb65ffe2f92f21689829d0ed61166753c53267d27c",
        "kind": "illustrative"
      },
      {
        "file": "../examples/demo/ai-regulation-trends.json",
        "sha256": "b43b44fe62a356f6524d02b3569cd25d1bc59d6759720430836e38fa39fd4662",
        "kind": "illustrative"
      },
      {
        "file": "../examples/demo/ai-investment-trends.json",
        "sha256": "8491c9dbdea45628993208d1b0f68ee451371a28c18ca5720fef6e5e033dd14d",
        "kind": "illustrative"
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
            820,
            860,
            910,
            1460,
            1690,
            1180,
            990,
            940
          ]
        },
        {
          "name": "AI investment",
          "color": "#3b4fd8",
          "values": [
            1520,
            1610,
            1580,
            1640,
            1910,
            2230,
            2410,
            2380
          ]
        }
      ],
      "stats": [
        {
          "value": "8,850",
          "label": "AI regulation articles"
        },
        {
          "value": "15,280",
          "label": "AI investment articles"
        },
        {
          "value": "22,820",
          "label": "match at least one (exact union)"
        },
        {
          "value": "1,310",
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
            "num": "8,850"
          },
          {
            "num": "38.8%"
          },
          "30 Mar",
          {
            "num": "34.2%"
          }
        ],
        [
          {
            "main": "AI investment",
            "sub": "q = “AI investment”"
          },
          {
            "num": "15,280"
          },
          {
            "num": "67.0%"
          },
          "13 Apr",
          {
            "num": "13.6%"
          }
        ]
      ],
      "stats": [
        {
          "value": "22,820",
          "label": "union: match at least one"
        },
        {
          "value": "5.7%",
          "label": "of the union match both"
        },
        {
          "value": "8 weeks",
          "label": "complete periods, no partial buckets"
        }
      ],
      "note": "Regulation coverage spikes and fades; investment coverage climbs steadily. Overlapping articles are counted once in the union."
    },
    "footnote": "Sets may overlap. Keep dates, content-class scope and matching mode identical when comparing.",
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
    "kind": "illustrative",
    "badge": "Illustrative data · fictional articles and counts",
    "sources": [
      {
        "file": "../examples/demo/semiconductor-priority.json",
        "sha256": "1e3fef8b4d3319bdf01030b4e52bd4774f625979fdd514aef4832671baf12a68",
        "kind": "illustrative"
      },
      {
        "file": "../examples/demo/semiconductor-critical.json",
        "sha256": "e4fdc547475965599e73215d9b50b148034c04499017ccd4ee876ec7ff15aa29",
        "kind": "illustrative"
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
          "limit": 6
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
            0,
            30,
            210,
            1840,
            2630,
            1910,
            1240,
            520,
            120
          ]
        }
      ],
      "stats": [
        {
          "value": "8,500",
          "label": "articles with a priority"
        },
        {
          "value": "1,880",
          "label": "critical (7–9)"
        },
        {
          "value": "22.1%",
          "label": "critical share (archive 16.7%)"
        },
        {
          "value": "5.1",
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
          "headline": "Fab outage at Tailspin Semiconductor halts 12-inch wafer output",
          "meta": "chipwire.example · 23 Apr",
          "tags": [
            {
              "text": "very neg",
              "tone": "negative"
            },
            {
              "text": "priority 9",
              "tone": "warn"
            },
            {
              "text": "class 0",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Export licence review delays shipments of advanced lithography tools",
          "meta": "tradeweekly.example · 18 Apr",
          "tags": [
            {
              "text": "fair neg",
              "tone": "negative"
            },
            {
              "text": "priority 8",
              "tone": "warn"
            },
            {
              "text": "class 0",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Litware wins $2.1B subsidy for new packaging plant",
          "meta": "markets-desk.example · 15 Apr",
          "tags": [
            {
              "text": "fair pos",
              "tone": "positive"
            },
            {
              "text": "priority 8",
              "tone": "warn"
            },
            {
              "text": "class 0",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Memory prices jump 9% week on week as supply tightens",
          "meta": "chipwire.example · 10 Apr",
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
              "text": "class 0",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Automakers flag microcontroller shortages for third quarter",
          "meta": "dailyauto.example · 2 Apr",
          "tags": [
            {
              "text": "fair neg",
              "tone": "negative"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            },
            {
              "text": "class 0",
              "tone": ""
            }
          ]
        },
        {
          "headline": "Wide World Devices recalls modules over firmware defect",
          "meta": "chipwire.example · 27 Mar",
          "tags": [
            {
              "text": "very neg",
              "tone": "negative"
            },
            {
              "text": "priority 7",
              "tone": "warn"
            },
            {
              "text": "class 0",
              "tone": ""
            }
          ]
        }
      ],
      "note": "Priority is the pipeline's urgency rating; it is not a measure of factual reliability."
    },
    "footnote": "Critical share divides by articles carrying a priority, not by all matching articles.",
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
    "badge": "Captured data · 14 Oct 2026",
    "sources": [
      {
        "file": "../examples/demo/class-map-vehicle.json",
        "sha256": "0c33ec0acde86e71b25b82e5ce2a5a84ec20957e84f731a085f4c8bb160d3b2c",
        "kind": "captured"
      },
      {
        "file": "../examples/demo/class-map-banking.json",
        "sha256": "0360d968e9f971dae0fc6a01678c5e80f290e839e707df188bd0aa4f493428d5",
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
              "code": 63,
              "path": "/Autos & Vehicles/Motor Vehicles (By Type)/Hybrid & Alternative Vehicles",
              "depth": 3,
              "parent": "/Autos & Vehicles/Motor Vehicles (By Type)",
              "parent_code": null,
              "articles_30d": null
            },
            {
              "code": 89,
              "path": "/Autos & Vehicles/Vehicle Shopping/Vehicle Specs, Reviews & Comparisons",
              "depth": 3,
              "parent": "/Autos & Vehicles/Vehicle Shopping",
              "parent_code": null,
              "articles_30d": null
            },
            {
              "code": 121,
              "path": "/Autos & Vehicles/Vehicle Parts & Services/Vehicle Parts & Accessories",
              "depth": 3,
              "parent": "/Autos & Vehicles/Vehicle Parts & Services",
              "parent_code": null,
              "articles_30d": null
            },
            {
              "code": 122,
              "path": "/Autos & Vehicles/Vehicle Codes & Driving Laws/Other",
              "depth": 3,
              "parent": "/Autos & Vehicles/Vehicle Codes & Driving Laws",
              "parent_code": null,
              "articles_30d": null
            },
            {
              "code": 141,
              "path": "/Autos & Vehicles/Motor Vehicles (By Type)/Trucks, Vans & SUVs",
              "depth": 3,
              "parent": "/Autos & Vehicles/Motor Vehicles (By Type)",
              "parent_code": null,
              "articles_30d": null
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
              "articles_30d": null
            },
            {
              "code": 180,
              "path": "/Finance/Banking/Mobile Payments & Digital Wallets",
              "depth": 3,
              "parent": "/Finance/Banking",
              "parent_code": null,
              "articles_30d": null
            },
            {
              "code": 316,
              "path": "/Business & Industrial/Business Finance/Investment Banking",
              "depth": 3,
              "parent": "/Business & Industrial/Business Finance",
              "parent_code": null,
              "articles_30d": null
            },
            {
              "code": 496,
              "path": "/Finance/Banking/Savings Accounts",
              "depth": 3,
              "parent": "/Finance/Banking",
              "parent_code": null,
              "articles_30d": null
            },
            {
              "code": 678,
              "path": "/Finance/Banking/Money Transfer & Wire Services",
              "depth": 3,
              "parent": "/Finance/Banking",
              "parent_code": null,
              "articles_30d": null
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
        "Filter"
      ],
      "widths": [
        10,
        34,
        38,
        18
      ],
      "rows": [
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
            "tag": "classes=63"
          }
        ],
        [
          {
            "num": "89"
          },
          {
            "main": "Vehicle Specs, Reviews & Comparisons"
          },
          {
            "sub": "/Autos & Vehicles/Vehicle Shopping"
          },
          {
            "tag": "classes=89"
          }
        ],
        [
          {
            "num": "121"
          },
          {
            "main": "Vehicle Parts & Accessories"
          },
          {
            "sub": "/Autos & Vehicles/Vehicle Parts & Services"
          },
          {
            "tag": "classes=121"
          }
        ],
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
            "tag": "classes=122"
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
            "tag": "classes=180"
          }
        ],
        [
          {
            "num": "316"
          },
          {
            "main": "Investment Banking"
          },
          {
            "sub": "/Business & Industrial/Business Finance"
          },
          {
            "tag": "classes=316"
          }
        ]
      ],
      "note": "30-day article volumes were unavailable at capture time; codes and paths are complete."
    },
    "footnote": "Class matches use the pipeline's 0.39 score threshold. One article can carry several classes.",
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
    "kind": "illustrative",
    "badge": "Illustrative data · fictional articles",
    "sources": [
      {
        "file": "../examples/demo/battery-export.json",
        "sha256": "62760c9c014e9355bd7f5fa3ae052ad696e5567f7a4225a1593dd667fd6114d1",
        "kind": "illustrative"
      }
    ],
    "nav": "Full articles to CSV",
    "client": "Codex",
    "heading": "Export full articles for analysis",
    "title": "Export full article text to a spreadsheet",
    "prompt": "Export the full text of battery-recycling articles from March–April 2026 to a CSV with headline, publisher, date, sentiment, priority and classes.",
    "steps": [
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/export",
        "body": {
          "q": "battery recycling",
          "since": "2026-03-02",
          "until": "2026-04-26",
          "limit": 5,
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
      "subtitle": "5 articles delivered of 214 matches · characters of full text",
      "axisLabel": "Characters of article body",
      "rows": [
        {
          "label": "Proseware opens closed-loop battery…",
          "sub": "energywire.example · 21 Apr",
          "value": 2870,
          "display": "2,870 chars · lede 314"
        },
        {
          "label": "Recyclers push for standard battery…",
          "sub": "tradeweekly.example · 16 Apr",
          "value": 1230,
          "display": "1,230 chars · lede 314"
        },
        {
          "label": "Black-mass prices slide as new…",
          "sub": "markets-desk.example · 7 Apr",
          "value": 1845,
          "display": "1,845 chars · lede 314"
        },
        {
          "label": "Automaker signs recovered-nickel…",
          "sub": "dailyauto.example · 25 Mar",
          "value": 4305,
          "display": "4,305 chars · lede 314"
        },
        {
          "label": "Fire at storage yard prompts safety…",
          "sub": "metro-ledger.example · 12 Mar",
          "value": 820,
          "display": "820 chars · lede 314"
        }
      ],
      "stats": [
        {
          "value": "5",
          "label": "exports charged"
        },
        {
          "value": "0",
          "label": "unresolved"
        },
        {
          "value": "0",
          "label": "duplicate URLs dropped"
        },
        {
          "value": "214",
          "label": "matching articles"
        }
      ]
    },
    "detail": {
      "type": "sheet",
      "title": "Full articles, as a CSV file",
      "subtitle": "The export's CSV columns, one row per delivered article",
      "filename": "battery-recycling.csv",
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
          "Proseware opens closed-loop battery recycling line",
          "energywire.example",
          "2026-04-21",
          {
            "tag": "fair_pos",
            "tone": "positive"
          },
          "6",
          "63"
        ],
        [
          "Recyclers push for standard battery passports",
          "tradeweekly.example",
          "2026-04-16",
          {
            "tag": "slight_pos",
            "tone": "positive"
          },
          "5",
          "63"
        ],
        [
          "Black-mass prices slide as new capacity arrives",
          "markets-desk.example",
          "2026-04-07",
          {
            "tag": "slight_neg",
            "tone": "negative"
          },
          "6",
          "63"
        ],
        [
          "Automaker signs recovered-nickel supply agreement",
          "dailyauto.example",
          "2026-03-25",
          {
            "tag": "fair_pos",
            "tone": "positive"
          },
          "7",
          "63"
        ],
        [
          "Fire at storage yard prompts safety review",
          "metro-ledger.example",
          "2026-03-12",
          {
            "tag": "very_neg",
            "tone": "negative"
          },
          "7",
          "63"
        ]
      ],
      "note": "The body column holds the complete article text; it is omitted here for width."
    },
    "footnote": "Exports are charged per delivered article. Save IDs across batches to deduplicate a full download.",
    "takeaway": "Move from a filter to full article text in a file your analysis tools can read.",
    "evidence_summary": "One full-article export batch",
    "guide": "../USER_GUIDE.md#full-articles-and-exports"
  }
];
