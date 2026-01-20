# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an educational tutorial repository teaching AI-assisted development workflows. It is **documentation-first** - the repository contains teaching materials, guides, and sample data rather than application code. Students following this tutorial will build a Streamlit sales analytics dashboard as their project.

## Repository Structure

- `docs/` - Tutorial documentation (sessions, references, troubleshooting)
- `prd/` - Product Requirements Document for the tutorial project
- `data/` - Sample sales-data.csv (~1000 transactions) for the dashboard project

## Technology Stack Taught

The tutorial teaches students to use:
- **Python 3.11+** with **uv** package manager
- **Streamlit** for dashboard development
- **Pandas** for data processing, **Plotly** for visualization
- **spec-kit** for spec-driven development workflow
- **Git/GitHub** for version control
- **Jira** for task management (with MCP integration)

## Workflow Conventions

### Spec-Driven Development
Students use spec-kit to generate specifications and plans before coding:
```bash
spec-kit init    # Initialize spec-kit in project
```

### Commit Format
All commits must reference Jira issue keys:
```bash
git commit -m "ECOM-1: add sales dashboard component"
```

### MCP Integration
Claude Code connects to Jira via Model Context Protocol, enabling direct reading of project tasks during development.

## Key Files

- `docs/00-overview.md` - Tutorial objectives and what students will build
- `docs/01-session-1-setup.md` - Environment setup instructions
- `docs/04-session-2-workflow.md` - Complete development workflow guide
- `docs/06-capstone-project-dev-environment.md` - Capstone project setup
- `prd/ecommerce-analytics.md` - Full PRD for the sales dashboard project
