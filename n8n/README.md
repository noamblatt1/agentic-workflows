# n8n Workflows

Exported n8n workflow JSON files for version control.

## How to use

### Export a workflow from n8n
1. Open a workflow in your n8n instance
2. Click the three dots menu → **Export** → **Download as JSON**
3. Save the `.json` file in this directory

### Import a workflow to n8n
1. In n8n, click **Add workflow** → **Import from file**
2. Select the `.json` file from this directory

## n8n Instance

- **URL:** https://vegasecurity.app.n8n.cloud
- **API access:** Configured via n8n-mcp MCP server

## Claude Code Integration

The n8n skills are installed globally (`~/.claude/skills/n8n-*`) and the n8n-mcp MCP server is configured in `~/.claude/.mcp.json`. Claude can help you build, validate, and manage n8n workflows directly.
