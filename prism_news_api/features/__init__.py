"""features — one module per endpoint family. Each function takes the
authenticated Principal and validated parameters and returns an envelope
(or raises ApiError). No HTTP here; routers.py owns the transport."""
from . import (articles_ep, classes, export, headlines, me, priority,  # noqa: F401
               sentiment, status, themes, trends, vocabulary)
