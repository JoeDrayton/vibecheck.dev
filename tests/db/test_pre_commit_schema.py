"""The V2 CHECK constraints that keep the two session kinds well-formed.

A PR session must carry its PR number and both SHAs; a pre-commit session
must carry the hash of its staged diff. These rows are written straight to the
table, bypassing the endpoints, because the endpoints can never produce them:
the point is that the database refuses them even if a future code path tries.

Kept apart from tests/db/test_migrations.py, which is pure; these need the app
lifespan to apply migrations against a real Postgres.
"""

from __future__ import annotations

import secrets

import psycopg
import pytest
from fastapi.testclient import TestClient

from app.main import app


def _insert(database_url: str, **columns) -> None:
    row = {
        "repo": f"octo/schema-{secrets.token_hex(4)}",
        "diff": "diff --git a/x b/x\n+x\n",
        "question": "q?",
        "token": secrets.token_urlsafe(16),
        "status": "pending",
        **columns,
    }
    names = ", ".join(row)
    placeholders = ", ".join(f"%({n})s" for n in row)
    with psycopg.connect(database_url) as conn:
        conn.execute(
            f"INSERT INTO sessions ({names}, expires_at) VALUES ({placeholders}, now())", row
        )
        conn.commit()


def _migrate() -> None:
    with TestClient(app):
        pass


def test_pr_session_without_pr_number_is_refused(vibecheck_env, database_url: str) -> None:
    _migrate()
    with pytest.raises(psycopg.errors.CheckViolation):
        _insert(database_url, source="pr", head_sha="1" * 40, base_sha="2" * 40)


def test_pre_commit_session_without_diff_hash_is_refused(vibecheck_env, database_url: str) -> None:
    _migrate()
    with pytest.raises(psycopg.errors.CheckViolation):
        _insert(database_url, source="pre_commit")
