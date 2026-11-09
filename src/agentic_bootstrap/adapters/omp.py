from __future__ import annotations

from ..model import GeneratedFile
from .base import AdapterContext


class OmpAdapter:
    name = "omp"

    def render(self, context: AdapterContext) -> dict[str, GeneratedFile]:
        # omp natively discovers standalone AGENTS.md and .agents/skills (agents
        # provider, project scope, one-level layout) and reads root mcp.json /
        # .mcp.json as MCP fallback files. It intentionally receives no omp-native
        # settings: no .omp/AGENTS.md, .omp/RULES.md, .omp/skills, .omp/mcp.json,
        # or hooks are generated.
        return {}
